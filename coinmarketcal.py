import json
import requests as r


def getCoins():
    coins = r.get("https://coinmarketcal.com/api/coins")
    return json.loads(coins.text)


def getCategories():
    categories = r.get("https://coinmarketcal.com/api/categories")
    return json.loads(categories.text)


def getEvents(page=None, max=None, dateRangeStart=None, dateRangeEnd=None,
              coins=None, categories=None, sortBy=None, showOnly=None):
    params = {
            "page": page,
            "max": max,
            "dateRangeStart": dateRangeStart,
            "dateRangeEnd": dateRangeEnd,
            "coins": coins,
            "categories": categories,
            "sortBy": sortBy,
            "showOnly": showOnly,
             }

    url = "https://coinmarketcal.com/api/events"
    events = r.get(url, params=params)
    return json.loads(events.text)
