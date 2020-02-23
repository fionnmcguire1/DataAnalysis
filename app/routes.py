from flask import Flask,request,render_template
from app.models import User
from app import db
#app = Flask(__name__)

from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route("/home", methods=['GET'])
def home():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        new_user = User(username=username,email=email,password=password)

        try:
            db.session.add(new_user)
            db.session.commit()
            return 'Damn'
        except:
            return 'There was an issue adding your task'
    else:
        users = User.query.order_by(User.username).all()
        return render_template('index.html', users=users)
    return render_template('index.html')
