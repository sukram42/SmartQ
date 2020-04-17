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
    pass

def login(username, password):
    return True

def get_shops():
    return []

def get_shopinfo(shop, id_, time):
    return "xoxo"

def add_shop(shop, shopinfo):
    pass