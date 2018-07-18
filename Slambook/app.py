from string import lower

from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import String, and_
from sqlalchemy_wrapper import SQLAlchemy

app = Flask(__name__)

db = SQLAlchemy('sqlite:///slambook.db')


class Parent(db.Model):
    __tablename__ = "parent"

    fn = db.Column(String)
    sn = db.Column(String)
    email = db.Column(String, primary_key=True)
    password = db.Column(String)
    gender = db.Column(String)


db.create_all()


@app.route('/')
def index():
    return render_template('login_and_sign_up.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    try:
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
            return redirect(url_for('logged_in'))
        else:
            print "2"
            return redirect(url_for('index'))
    except:
        print "3"
        return redirect(url_for('index'))


@app.route('/home')
def logged_in():
    return render_template('login_and_sign_up.html')


@app.route('/insertuser', methods=['POST', 'GET'])
def insertuser():
    fn = request.form['fn']
    sn = request.form['sn']
    email = request.form['email']
    password = request.form['pass']
    gender = request.form['gender']
    print gender
    u1 = Parent(fn=fn, sn=sn, email=email, password=password, gender=gender)
    db.add(u1)
    db.commit()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
