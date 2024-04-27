from requests import Session
from cookies import login_cookie

session = Session()

API_URL = "http://127.0.0.1:8000"


def loginApi(email, password):
    data = {
        "username": email,
        "password": password,
        # "grant_type": "",
        # "scope": "",
        # "client_id": "",
        # "client_secret": ""
    }
    login_response = session.post(
        API_URL + "/auth/token", data=data
    )

    if login_response.status_code == 200:
        token = login_response.json()["access_token"]
        login_cookie(token)
    else:
        return login_response.json()


def registerApi(username, email, password):
    register_response = session.post(
        API_URL + "/auth/register",
        json={"name": username, "email": email, "password": password},
    )

    if register_response.status_code == 200:
        loginApi(email, password)
    else:
        return register_response.json()


def getTemplateAllApi():
    response = session.get(
        API_URL + '/template/all'
    )
    return response.json()


def getTemplateByIdApi(id):
    response = session.get(
        API_URL + f'/template/get/{id}'
    )
    return response.json()


def getFact():
    response = session.get(
        API_URL + '/fact'
    )
    return response.json()


def getTierListsAllApi():
    response = session.get(
        API_URL + '/tierlist/all'
    )
    return response.json()


def getTierListByIdApi(id):
    response = session.get(
        API_URL + f'/tierlist/get/{id}'
    )
    return response.json()


def getItemByIdApi(id):
    response = session.get(
        API_URL + f'/item/get/{id}'
    )
    return response.json()


def creteItemApi(name, desc, price, picture):
    data = {
        'name': name,
        'description': desc,
        'price': price,
        "picture": picture
    }
    response = session.post(
        API_URL + f'/item/get/{id}', json=data
    )
    if response.status_code != 200:
        return response.json()


def rankItemApi(item_id, tierlist_id, tier):
    response = session.post(
        API_URL + f'/item/rank/?item_id={item_id}&tierlist_id={tierlist_id}&tier={tier}'
    )

    if response.status_code != 200:
        return response.json()
