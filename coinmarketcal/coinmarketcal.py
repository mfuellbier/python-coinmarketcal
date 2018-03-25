import json
import requests as r


def getToken(id, secret):
    # Get the id and secret from https://api.coinmarketcal.com/developer/register
    payload = {'grant_type': 'client_credentials', 'client_id': id, 'client_secret': secret}
    url = "https://api.coinmarketcal.com/oauth/v2/token"
    try:
        events = r.post(url, data=payload)
        result = json.loads(events.text)
    except json.decoder.JSONDecodeError:
        print("JSONDecodeError")
        result = []
    return result


def getCoins(token):
    payload = {'access_token': token}
    url = "https://api.coinmarketcal.com/v1/coins"
    try:
        events = r.get(url, params=payload)
        result = json.loads(events.text)
    except json.decoder.JSONDecodeError:
        print("JSONDecodeError")
        result = []
    return result


def getCategories(token):
    payload = {'access_token': token}
    url = "https://api.coinmarketcal.com/v1/categories"
    try:
        events = r.get(url, params=payload)
        result = json.loads(events.text)
    except json.decoder.JSONDecodeError:
        print("JSONDecodeError")
        result = []
    return result


def getEvents(token, page=None, max=None, dateRangeStart=None, dateRangeEnd=None,
              coins=None, categories=None, sortBy=None, showOnly=None):
    payload = {
            "page": page,
            "max": max,
            "dateRangeStart": dateRangeStart,
            "dateRangeEnd": dateRangeEnd,
            "coins": coins,
            "categories": categories,
            "sortBy": sortBy,
            "showOnly": showOnly,
            'access_token': token,
             }

    url = "https://api.coinmarketcal.com/v1/events"
    try:
        events = r.get(url, params=payload)
        result = json.loads(events.text)
    except json.decoder.JSONDecodeError:
        print("JSONDecodeError")
        result = []
    return result
