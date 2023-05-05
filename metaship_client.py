import requests

uri = "https://api.metaship.ru/"


def get_access_token():
    url = uri + "auth/access_token"

    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    data = {
        "client_id": "****",
        "client_secret": "****",
        "grant_type": "client_credentials"
    }

    response = requests.post(url, headers=headers, data=data)
    access_token = response.json()["access_token"]

    return access_token


def get_shops():
    url = uri + "v2/customer/shops"

    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + get_access_token()
    }

    response = requests.get(url, headers=headers)
    return response.json()


def get_warehouses():
    url = uri + "v2/customer/warehouses"

    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + get_access_token()
    }

    response = requests.get(url, headers=headers)
    return response.json()


def create_shop():
    url = uri + "v2/customer/shops"

    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + get_access_token()
    }

    data = dict(name="Test", uri="Test", phone="74958885566", sender="Test")

    response = requests.post(url, headers=headers, json=data)
    return response.json()
