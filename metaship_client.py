import requests


def get_access_token():
    url = "https://api.metaship.ru/auth/access_token"

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
    url = "https://api.metaship.ru/v2/customer/shops"

    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + get_access_token()
    }

    response = requests.get(url, headers=headers)
    return response.json()


