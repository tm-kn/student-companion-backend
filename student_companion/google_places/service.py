import tempfile

from django.conf import settings

from PIL import Image
import requests


class GooglePlacesService:
    API_KEY = settings.GOOGLE_PLACES_API_KEY
    BASE_URL = 'https://maps.googleapis.com/maps/api/'

    PLACE_DETAIL_URL = 'place/details/json'
    PLACE_PHOTO_URL = 'place/photo'

    def generate_url(self, component):
        return '{}{}'.format(self.BASE_URL, component)

    def fetch(self, url, params={}, **kwargs):
        params['key'] = self.API_KEY
        return requests.get(url, params, **kwargs)

    def get_place(self, place_id):
        url = self.generate_url(self.PLACE_DETAIL_URL)
        response = self.fetch(url, params={
            'placeid': place_id
        })

        response.raise_for_status()

        if response.json().get('status', '') != 'OK':
            raise Exception('Place with that ID not found')

        return response.json().get('result', {})

    def get_place_photo(self, photo_reference, max_width=400, max_height=400):
        url = self.generate_url(self.PLACE_PHOTO_URL)
        response = self.fetch(url, params={'photoreference': photo_reference,
                                           'maxwidth': max_width,
                                           'maxheight': max_height},
                              stream=True)

        response.raise_for_status()

        lf = tempfile.NamedTemporaryFile()

        for block in response.iter_content(1024 * 8):
            if not block:
                break

            lf.write(block)

        return lf
