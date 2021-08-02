import requests


def create_ya_disc_folder(params):
    token = 'token'
    url = 'https://cloud-api.yandex.net/v1/disk/resources'
    headers = {'Accept': 'application/json', "Authorization": token}
    response = requests.put(url, params=params, headers=headers)
    return response.status_code


def get_ya_disc_folder(params):
    token = 'token'
    url = 'https://cloud-api.yandex.net/v1/disk/resources'
    headers = {'Accept': 'application/json', "Authorization": token}
    response = requests.put(url, params=params, headers=headers)
    return response.status_code
