from django.conf import settings

import requests


class GooglePlacesService:
    API_KEY = settings.GOOGLE_PLACES_API_KEY
    BASE_URL = 'https://maps.googleapis.com/maps/api/'

    PLACE_DETAIL_URL = 'place/details/'

    def generate_url(self, component):
        return '{}{}json'.format(self.BASE_URL, component)

    def fetch(self, url, params={}):
        params['key'] = self.API_KEY
        return requests.get(url, params)

    def get_place(self, place_id):
        url = self.generate_url(self.PLACE_DETAIL_URL)
        response = self.fetch(url, params={'placeid': place_id})

        response.raise_for_status()
        return response.json().get('result', {})
