# Author: mfuellbier
# This file is part of python-coinmarketcal.
#
# python-coinmarketcal is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# python-coinmarketcal is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with python-coinmarketcal.  If not, see <http://www.gnu.org/licenses/>.

import logging
import json
import requests
import datetime

logger = logging.getLogger('python-coinmarketcal')


class Coinmarketcal:

    def __init__(self, id, secret):
        self.id = id
        self.secret = secret

    @property
    def token(self):
        if not getattr(self, '_token', None):
            self._token = self.get_token(self.id, self.secret)
        if datetime.now() > self._token['expires_at']:
            self._token = self.get_token(self.id, self.secret)
        return self._token['access_token']

    def get_token(self, id, secret):
        # Get the id and secret from
        # https://api.coinmarketcal.com/developer/register
        payload = {
            'grant_type': 'client_credentials',
            'client_id': id,
            'client_secret': secret}
        url = "https://api.coinmarketcal.com/oauth/v2/token"
        try:
            events =requests.post(url, data=payload)
            result = json.loads(events.text)
            result['expires_at'] = (
                datetime.datetime.now()
                + datetime.timedelta(seconds=result['expires_in']))
        except json.decoder.JSONDecodeError:
            logger.debug("JSONDecodeError")
            result = []
        logger.debug(result)
        return result

    def get_coins(self):
        payload = {'access_token': self.token}
        url = "https://api.coinmarketcal.com/v1/coins"
        try:
            events =requests.get(url, params=payload)
            result = json.loads(events.text)
        except json.decoder.JSONDecodeError:
            logger.debug("JSONDecodeError")
            result = []
        return result

    def get_categories(self):
        payload = {'access_token': self.token}
        url = "https://api.coinmarketcal.com/v1/categories"
        try:
            events =requests.get(url, params=payload)
            result = json.loads(events.text)
        except json.decoder.JSONDecodeError:
            logger.debug("JSONDecodeError")
            result = []
        return result

    def get_events(self, page=None, max=None,
                  dateRangeStart=None, dateRangeEnd=None,
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
            'access_token': self.token}

        url = "https://api.coinmarketcal.com/v1/events"
        try:
            events =requests.get(url, params=payload)
            result = json.loads(events.text)
        except json.decoder.JSONDecodeError:
            logger.debug("JSONDecodeError")
            result = []
        return result
