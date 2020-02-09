import DataView
from flask import Flask, request,render_template,url_for
from flask_sqlalchemy import SQLAlchemy
from DataView.models import User


app = Flask(__name__)
app.config["DEBUG"] = True
# app.config['SQLAlCHEMY_DATABASE_URI'] = 'sqlite:///dataanalysis.db'
# db = SQLAlchemy(app)



@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        new_user = User(username=username,email=email,password=password)

        try:
            db.session.add(new_user)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue adding your task'
    else:
        users = User.query.order_by(User.date_created).all()
        return render_template('index.html', users=users)
    return render_template('index.html')


if __name__ == "__main__":
    app.run()
    app.config['debug'] == True
