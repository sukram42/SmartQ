import os
from flask import Flask, json, request
from flask_jwt import JWT, jwt_required
from backend import *
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import safe_str_cmp

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "queuedatabase.db"))

app = Flask(__name__)

app.config['SECRET_KEY'] = 'super-secret'

#setting up the database
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Shop(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(80), nullable=False)
    category=db.Column(db.String(80), nullable=False)
    address=db.Column(db.String(80), nullable=False)
    latitude=db.Column(db.Float, nullable=False)
    longitude=db.Column(db.Float, nullable=False)
    storespace=db.Column(db.Integer, nullable=False)
    maxcapacity=db.Column(db.Integer, nullable=False)
    
    def __repr__(self):
        return "<ID: {}>".format(self.id)

class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    shopid=db.Column(db.Integer, nullable=False)
    number=db.Column(db.Integer, nullable=False)
    capacity=db.Column(db.Float, nullable=False)
    waitingtime=db.Column(db.Integer, nullable=False)
    lastupdate=db.Column(db.DateTime, nullable=False)
    
    def __repr__(self):
        return "<ID: {}>".format(self.id)
    
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(80), nullable=False)
    shopaddress=db.Column(db.String(80), nullable=False)
    login=db.Column(db.String(80), nullable=False)
    password=db.Column(db.String(80), nullable=False)
    
    def __repr__(self):
        return "<ID: {}>".format(self.id)
    
# jwt = JWT(app, authenticate, identity)

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

def get_all_users():
    users = [12] #load all users
    username_table = {u.username: u for u in users}
    userid_table = {u.id: u for u in users}
    return username_table, userid_table

def authenticate(username, password):
    username_table, _ = get_all_users()
    user = username_table.get(username, None)
    if user and safe_str_cmp(user.password.encode('utf-8'), password.encode('utf-8')):
        return user

def identity(payload):
    _, userid_table = get_all_users()
    user_id = payload['identity']
    return userid_table.get(user_id, None)



def update_database(shop, id_, peoplechange):
    pass

def register(signin_data):
    # check whether it is the correct format for signin_data
    user = User(
    name= signin_data["name"],
    shopaddress= signin_data["shopaddress"],
    login= signin_data["login"],
    password= signin_data["password"]
    )
    db.session.add(user)
    db.session.commit()
    return True

def login(username, password):
    return True

def get_shops():
    shops = Shop.query.all()
    return shops

def get_shopinfo(shop, id_, time):
    return "xoxo"

def add_shop(shop, shopinfo):
    lat = 10
    long = 10
    
    newshop = Shop(
    name=shopinfo["name"],
    category=shopinfo["category"],
    address=shopinfo["address"],
    latitude=lat,
    longitude=long,
    storespace=shopinfo["storespace"],
    maxcapacity=shopinfo["maxcapacity"]
    )
    db.session.add(newshop)
    db.session.commit()
    return True

if __name__ == '__main__':
    app.run(debug=True)