import requests
from parser.auto_ru.settings import headers, url_listing, url_geo


def auto_send_request_listing(params, hdr=headers):

    response = requests.post(url_listing, json=params, headers=hdr)
    data = response.json()

    return data


def auto_first_send_request_geo(params, hdr=headers):

    geo_list = []
    response = requests.post(url_geo, json=params, headers=hdr)
    data = response.json()
    for city in data:
        geo_list.append(city['name'])

    return geo_list
