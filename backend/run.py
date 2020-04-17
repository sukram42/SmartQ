from flask import Flask, json, request
from flask_jwt import JWT, jwt_required
from backend import *


app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'super-secret'

# jwt = JWT(app, authenticate, identity)

success = True

@app.route('/register', methods=['GET', 'POST'])
@jwt_required()
def register():
    data=[1,2,3]
    
    if success:
        return app.response_class(response=json.dumps(data),status=200,mimetype='application/json')
    return app.response_class(response=json.dumps("Access not allowed"),status=401,mimetype='application/json')

@app.route('/signin', methods=['GET', 'POST'])
@jwt_required()
def sign():
    data=[1,2,3]
    
    if success:
        return app.response_class(response=json.dumps(data),status=200,mimetype='application/json')
    return app.response_class(response=json.dumps("Access not allowed"),status=401,mimetype='application/json')

@app.route('/<shop>/update', methods=['GET', 'POST'])
@jwt_required()
def update(shop):
    data=[1,2,3]
    
    if success:
        return app.response_class(response=json.dumps(data),status=200,mimetype='application/json')
    return app.response_class(response=json.dumps("Access not allowed"),status=401,mimetype='application/json')

@app.route('/<shop>', methods=['GET', 'POST'])
def shopinfo(shop):
    data=[1,2,3]
    
    if success:
        return app.response_class(response=json.dumps(data),status=200,mimetype='application/json')
    return app.response_class(response=json.dumps("Access not allowed"),status=401,mimetype='application/json')

@app.route('/', methods=['GET', 'POST'])
def hello():
    data=[1,2,3]
    
    if request.method == 'GET':
        data=[2,3,4]
    
    if success:
        return app.response_class(response=json.dumps(data),status=200,mimetype='application/json')
    return app.response_class(response=json.dumps("Access not allowed"),status=401,mimetype='application/json')

if __name__ == '__main__':
    app.run(debug=True)