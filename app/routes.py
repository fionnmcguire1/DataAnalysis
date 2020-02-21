import DataView
from flask import Flask


app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET','POST'])
@app.route('/index')
def index():
    return "<h3>Hello, World!</h3>"
