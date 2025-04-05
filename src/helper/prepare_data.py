from dataclasses import dataclass
import requests
import json
from typing import Literal
from urllib.parse import urlencode
from decouple import config


TwelveDataAPIKEY = config("TwelveDataAPIKEY", default=None, cast=str)



@dataclass
class TwelveDataAPI:
    pair_name: str = "EUR/USD"
    interval: Literal["15min", "1h", "4h", "1day", "1week"] = "15min"
    api_key: str = ""

    def get_api_key(self):
        return self.api_key or TwelveDataAPIKEY

    def get_params(self):
        return {
            "apikey": self.get_api_key(),
            "symbol": self.pair_name,
            "interval": self.interval,
            
        }

    def generate_url(self, pass_auth=False):
        path = "/query"
        url = f"https://api.twelvedata.com/time_series"
        params = self.get_params()
        encoded_params = urlencode(params)
        url = f"{url}?{encoded_params}"
        if pass_auth:
            api_key = self.get_api_key()
            url += f"&api_key={api_key}"
        return url

    def fetch_data(self):
        headers = {}
        url = self.generate_url()
        response = requests.get(url, headers=headers)
        response.raise_for_status() # not 200/201
        return response.json()['values']

        

        


