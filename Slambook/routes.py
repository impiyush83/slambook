from string import lower

from flask import Flask, render_template, request, redirect, url_for, session
from sqlalchemy import String, and_
from sqlalchemy_wrapper import SQLAlchemy
from models import Parent, Child, db

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('login_and_sign_up.html')


@app.route('/logout')
def logout():
    session.clear()
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
            session['profile'].append(email)
            print "1"
            return redirect(url_for('logged_in'))
        else:
            print "2"
            return redirect(url_for('index'))
    except:
        print "3"
        return redirect(url_for('index'))


@app.route('/addingfriend')
def add_friend():
    return render_template('registration.html')


@app.route('/home')
def logged_in():
    return render_template('homepage.html')


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
