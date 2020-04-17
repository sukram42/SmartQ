from flask import Flask, render_template
from flask_jwt import JWT, jwt_required
from backend import *


app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'super-secret'

jwt = JWT(app, authenticate, identity)


@app.route('/register', methods=['GET', 'POST'])
@jwt_required()
def register():
    pass

@app.route('/signin', methods=['GET', 'POST'])
@jwt_required()
def sign():
    pass

@app.route('/<shop>/update', methods=['GET', 'POST'])
@jwt_required()
def update():
    pass

@app.route('/<shop>', methods=['GET', 'POST'])
def shopinfo():
    pass

@app.route('/', methods=['GET', 'POST'])
def hello():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)