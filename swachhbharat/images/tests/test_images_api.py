import tempfile

from rest_framework import status
from rest_framework.test import APITestCase
import PIL.Image


class ImageApiTest(APITestCase):
    fixtures = ['image_fixtures.json']

    def test_get(self):
        response = self.client.get('/api/images/')
        assert response.status_code == status.HTTP_200_OK
        
        # Inserted as part of the fixture
        assert 'foo.jpg' in response.json()['results'][0]['file']

    def test_post(self):
        image = PIL.Image.new('RGB', (100, 100))
        temp_file = tempfile.NamedTemporaryFile(suffix='.jpg')
        image.save(temp_file, format='JPEG')
        with open(temp_file.name, 'rb') as data_file:
            response = self.client.post('/api/images/', 
                                        {'file': data_file}, 
                                        format='multipart')
            assert response.status_code == status.HTTP_201_CREATED