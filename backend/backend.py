from werkzeug.security import safe_str_cmp


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
    lat = 
    long = 
    
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