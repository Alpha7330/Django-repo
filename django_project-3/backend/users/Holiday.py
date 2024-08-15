
import requests

class HolidayService:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = 'https://holidayapi.com/v1/'

    def get_holidays(self, country, year):
        endpoint = 'holidays'
        params = {
            'country': country,
            'year': year,
            'key': self.api_key,
            'pretty': True
        }

        response = requests.get(f'{self.base_url}{endpoint}',params=params)
        # response.raise_for_status()
        # return response.json()
        return response

    def get_countries(self):
        endpoint = 'countries'
        params = {
            'key': self.api_key,
            'pretty': True
        }
        response = requests.get(f'{self.base_url}{endpoint}', params=params)
        response.raise_for_status()
        return response.json()

   
