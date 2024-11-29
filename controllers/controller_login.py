from flask import Blueprint, request,render_template
from databases.db import db
from models.user import User
from werkzeug.security import check_password_hash

user_bp = Blueprint('user', __name__)

@user_bp.route('/login', methods= ['GET','POST'])
def user_login():
    print("si esta llegando")
    if request.method == 'GET':
        return render_template('login.html')
    else: 
        username = request.form["username"]
        password = request.form["password"]
    list_user = User.query.all()
    for user in list_user:
        if user.username == username and user.password == password:
            if user.is_admin == True:                        
                return render_template('tabla.html', dogs = dogs )
            else:
                return render_template('welcome.html', user = username)    
    return render_template('login.html')

@user_bp.route('/auth', methods=['GET','POST'])
def authenticate_user(username, password):
    user = User.get_by_username(username)
    if user and check_password_hash(user.password,password):
        return user
    else:
        return None