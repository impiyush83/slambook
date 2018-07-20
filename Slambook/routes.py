from flask import Flask, render_template, request, redirect, url_for, session, g, Response
from flask_uploads import configure_uploads, UploadSet, IMAGES
from models import Parent, db, Child
import os

app = Flask(__name__)
photos = UploadSet('photos', IMAGES)
app.config['UPLOADED_PHOTOS_DEST'] = 'static/img'
configure_uploads(app, photos)
# session cannot be created without this
app.secret_key = os.urandom(24)


@app.route('/')
def index():
    return render_template('login_and_sign_up.html')


@app.route('/upload', methods=['POST'])
def upload():
    if g.profile:
        try:
            fn = request.form['fname']
            sn = request.form['sname']
            # email=request.form['email']
            fcolor = request.form['fcolor']
            ffood = request.form['ffood']
            fsong = request.form['fsong']
            gender = request.form['gender']
            tel = request.form['tel']
          #  filename = photos.save(request.files['fimg'])
           # filename = 'static/img/' + filename
            # print "5"
            # print session['profile']
            obj = db.query(Parent).filter(Parent.email == session['profile']).first()
            print obj
            # image_path = filename
            db.add(Child(fn=fn, sn=sn, fcolor=fcolor, ffood=ffood, fsong=fsong, gender=gender, friend=obj, tel=tel))
            db.commit()
            print obj.childs
            print "6"
            return redirect(url_for('logged_in'))
        except:
            return redirect(url_for('add_friend'))
    else:
        return redirect(url_for('index'))


@app.route('/getsession')
def getsession():
    if 'profile' in session:
        return session['profile']
    return "Not logged in"


@app.route('/dropsession')
def dropsession():
    session.pop('profile', None)
    g.profile = None
    return 'Dropped'


@app.before_request
def before_request():
    g.profile = None
    if 'profile' in session:
        g.profile = session['profile']


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    try:
        if request.method == "POST":
            session.pop('profile', None)
            email = request.form['email']
            password = request.form['password']
            objects = db.query(Parent).filter().all()
            flag = 0
            for i in objects:
                if str(i.email).strip() == str(email).strip() and str(i.password).strip() == str(password).strip():
                    flag = 1
                    break
            if flag == 1:
                print "1"
                session['profile'] = email
                print "1"
                return redirect(url_for('logged_in'))
            else:
                print "2"
                return redirect(url_for('index'))
    except:
        print "3"
        return redirect(url_for('index'))


@app.route('/addingfriend', methods=['POST', 'GET'])
def add_friend():
    return render_template('registration.html')


@app.route('/home')
def logged_in():
    print g.profile
    if g.profile:
        friends = db.query(Child).filter(Child.email == session['profile']).all()
        len1 = len(friends)
        return render_template('homepage.html', friends=friends, len=len1)
    return redirect(url_for('index'))


@app.route('/insertuser', methods=['POST', 'GET'])
def insertuser():
    fn = request.form['fn']
    sn = request.form['sn']
    email = request.form['email']
    password = request.form['pass']
    gender = request.form['gender']
    u1 = Parent(fn=fn, sn=sn, email=email, password=password, gender=gender)
    db.add(u1)
    db.commit()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
