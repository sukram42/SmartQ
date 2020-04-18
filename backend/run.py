from flask import Flask, json, request
from flask_jwt import JWT, jwt_required
from backend import *


app = Flask(__name__)

app.config['SECRET_KEY'] = 'super-secret'

# jwt = JWT(app, authenticate, identity)

success = True

@app.route('/register', methods=['GET', 'POST'])
# @jwt_required()
def register_user():
    
    if request.method == "POST":
        signin_data = request.json
        register(signin_data)
        
        return app.response_class(response=json.dumps("User was added"),status=200,mimetype='application/json')
    return app.response_class(response=json.dumps("Service unavailable"),status=503,mimetype='application/json')

@app.route('/signin', methods=['GET', 'POST'])
# @jwt_required()
def login_user():
    
    if request.method == "POST":
        username, password = request.json["login"], request.json["password"]
        access_granted = login(username, password)
        
        if access_granted:
            return app.response_class(response=json.dumps("Access granted"),status=200,mimetype='application/json')
        return app.response_class(response=json.dumps("Access denied"),status=401,mimetype='application/json')
    return app.response_class(response=json.dumps("Service unavailable"),status=503,mimetype='application/json')

@app.route('/<shop>/update', methods=['GET', 'POST'])
# @jwt_required()
def update(shop):
    
    if request.method == "POST":
        id_, peoplechange = request.json["id"], request.json["people_change"]
        update_database(shop, id_, peoplechange)
        return app.response_class(response=json.dumps(f"Updated {shop}\'s number of people"),status=200,mimetype='application/json')
    return app.response_class(response=json.dumps("Service unavailable"),status=503,mimetype='application/json')

@app.route('/<shop>', methods=['GET', 'POST'])
def shopinfo(shop):
    
    if request.method == "GET":
        id_, time = request.json["id"], request.json["time"]
        shopinfo = get_shopinfo(shop, id_, time)
        return app.response_class(response=json.dumps(shopinfo),status=200,mimetype='application/json')
    elif request.method == "POST":
        shopinfo = request.json
        add_shop(shop, shopinfo)
        return app.response_class(response=json.dumps(f"{shop}\'s data was added in database"),status=200,mimetype='application/json')
    return app.response_class(response=json.dumps("Service unavailable"),status=503,mimetype='application/json')

@app.route('/', methods=['GET', 'POST'])
def hello():
    
    if request.method == "GET":
        shops = get_shops()
        return app.response_class(response=json.dumps(shops),status=200,mimetype='application/json')
    return app.response_class(response=json.dumps("Service unavailable"),status=503,mimetype='application/json')

if __name__ == '__main__':
    app.run(debug=True)