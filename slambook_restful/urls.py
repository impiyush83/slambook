from slambook_restful.resource.customer_homepage import CustomerHomepage
from slambook_restful.resource.customer_login import CustomerLogin
from slambook_restful.resource.customer_logout import CustomerLogout
from slambook_restful.resource.customer_signup import CustomerSignUp
from slambook_restful.resource.index import Index
from slambook_restful.utils import URLS

urls = [
    URLS(resource=Index, endpoint=['/'], name="showcases_homepage"),
    URLS(resource=CustomerSignUp, endpoint=['user/signup'], name="signup_user"),
    URLS(resource=CustomerLogin, endpoint=['user/login'], name="customer_login"),
    URLS(resource=CustomerHomepage, endpoint=['user/home'], name="customer_homepage"),
    URLS(resource=CustomerLogout, endpoint=['user/logout'], name="unsets_jwt_cookie"),
]

#
# @app.route('/enter_secret_key', methods=['POST', 'GET'])
# def enter_secret_key():
#     if g.profile:
#         try:
#             return render_template('enter_secret_key.html')
#         except:
#             return redirect(url_for('logged_in'))
#     else:
#         return redirect(url_for('index'))
#
#
# @app.route('/create_secret_key', methods=['POST', 'GET'])
# def create_secret_key():
#     print(session['profile'])
#     if session['profile']:
#         try:
#             import random
#             import string
#             random = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(32)])
#             # print(random
#             obj = db.query(Parent).filter(Parent.email == session['profile']).first()
#             # print(obj.email
#             db.add(Secret(email=obj.email, secret_key=random))
#             db.commit()
#             # print("2"
#             return render_template('copy_secret_key.html', random=random)
#         except:
#             return redirect(url_for('logged_in'))
#     else:
#         return redirect(url_for('index'))
#
#
# @app.route('/check_secret_key', methods=['POST', 'GET'])
# def check_secret_key():
#     if g.profile:
#         try:
#             secret_key = request.form['secret_key']
#             owner_of_secret_key = db.query(Secret).filter(Secret.secret_key == secret_key).all()
#             if len(owner_of_secret_key) == 1:
#                 return render_template('remote_register.html', owner_of_secret_key=owner_of_secret_key[0].email)
#             else:
#                 return redirect(url_for('logged_in'))
#         except:
#             return redirect(url_for('logged_in'))
#     else:
#         return redirect(url_for('index'))
#
#
# @app.route('/remote_upload', methods=['POST'])
# def remote_upload():
#     if g.profile:
#         try:
#             fn = request.form['fname']
#             sn = request.form['sname']
#             # email=request.form['email']
#             fcolor = request.form['fcolor']
#             ffood = request.form['ffood']
#             fsong = request.form['fsong']
#             gender = request.form['gender']
#             tel = request.form['tel']
#             secret_key_object = request.form['secret_key']
#             # print(secret_key_object
#             # print(secret_key_object
#             # print(session['profile']
#             if str(secret_key_object) != str(session['profile']):
#                 obj_of_referer = db.query(Parent).filter(Parent.email == str(secret_key_object)).first()
#                 # print("333"
#                 db.add(
#                     Child(fn=fn, sn=sn, fcolor=fcolor, ffood=ffood, fsong=fsong, gender=gender, friend=obj_of_referer,
#                           tel=tel))
#                 db.commit()
#                 db.delete(db.query(Secret).filter(Secret.email == secret_key_object).first())
#                 db.commit()
#                 return redirect(url_for('logged_in'))  # success page
#             else:
#                 return redirect(url_for('logged_in'))
#         except:
#             return redirect(url_for('index'))
#     else:
#         return redirect(url_for('index'))
#
#
#
#
#
# @app.route('/upload', methods=['POST'])
# def upload():
#     if g.profile:
#         try:
#             fn = request.form['fname']
#             sn = request.form['sname']
#             # email=request.form['email']
#             fcolor = request.form['fcolor']
#             ffood = request.form['ffood']
#             fsong = request.form['fsong']
#             gender = request.form['gender']
#             tel = request.form['tel']
#             #  filename = photos.save(request.files['fimg'])
#             # filename = 'static/img/' + filename
#             # print("5"
#             # print(session['profile']
#             obj = db.query(Parent).filter(Parent.email == session['profile']).first()
#             # print(obj
#             # image_path = filename
#             db.add(Child(fn=fn, sn=sn, fcolor=fcolor, ffood=ffood, fsong=fsong, gender=gender, friend=obj, tel=tel))
#             db.commit()
#             # print(obj.childs
#             # print("6"
#             return redirect(url_for('logged_in'))
#         except:
#             return redirect(url_for('add_friend'))
#     else:
#         return redirect(url_for('index'))
#
#
# @app.route('/getsession')
# def getsession():
#     if 'profile' in session:
#         return session['profile']
#     return "Not logged in"
#
#
# @app.route('/dropsession')
# def dropsession():
#     session.pop('profile', None)
#     g.profile = None
#     return 'Dropped'
#
#
# @app.before_request
# def before_request():
#     g.profile = None
#     if 'profile' in session:
#         g.profile = session['profile']
#
#
# @app.route('/logout')
# def logout():
#     session.clear()
#     return redirect(url_for('index'))
#
#
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     try:
#         if request.method == "POST":
#
#             # session.pop('profile', None)
#             email = request.form['email']
#             password = request.form['password']
#             objects = db.query(Parent).filter().all()
#             flag = 0
#             for i in objects:
#                 if str(i.email).strip() == str(email).strip() and str(i.password).strip() == str(password).strip():
#                     flag = 1
#                     break
#             if flag == 1:
#                 # print("1"
#                 session['profile'] = email
#                 # print("1"
#                 return redirect(url_for('logged_in'))
#             else:
#                 # print("2"
#                 return redirect(url_for('index'))
#     except:
#         print("3")
#         return redirect(url_for('index'))
#
#
# @app.route('/addfriend', methods=['POST', 'GET'])
# def add_friend():
#     if g.profile:
#         return render_template('registration.html')
#     else:
#         return redirect(url_for('index'))
#
#
# @app.route('/home')
# def logged_in():
#     try:
#         # print(session['profile']
#         # print("lg1"
#         if session['profile']:
#             # print("lg1"
#             friends = db.query(Child).filter(Child.email == session['profile']).all()
#             # print(friends
#             len1 = len(friends)
#             # print("lg1"
#             object_to_check_secret_key_created = db.query(Secret).filter(Secret.email == session['profile']).all()
#             lenx = len(object_to_check_secret_key_created)
#             return render_template('homepage.html', friends=friends, len=len1, lenx=lenx)
#         # print("lg1"
#         return redirect(url_for('index'))
#     except:
#         return redirect(url_for('index'))
#
#

