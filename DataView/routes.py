import DataView
from flask import Flask


app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('DataView/', methods=['GET','POST'])
@app.route('DataView/index')
def index():
    return "<h3>Hello, World!</h3>"
