import tempfile

from rest_framework import status
from rest_framework.test import APITestCase
import PIL.Image


class ImageApiTest(APITestCase):
    fixtures = ['image_fixtures.json']

    def test_list_action(self):
        response = self.client.get('/api/images/')
        assert response.status_code == status.HTTP_200_OK

        # Inserted as part of the fixture
        assert 'foo.jpg' in response.json()['results'][0]['file']

    def test_create_action(self):
        image = PIL.Image.new('RGB', (100, 100))
        temp_file = tempfile.NamedTemporaryFile(suffix='.jpg')
        image.save(temp_file, format='JPEG')
        with open(temp_file.name, 'rb') as data_file:
            response = self.client.post('/api/images/', 
                                        {'file': data_file}, 
                                        format='multipart')
            assert response.status_code == status.HTTP_201_CREATED

    def test_retrieve_action(self):
        response = self.client.get('/api/images/1/')
        assert response.status_code == status.HTTP_200_OK
        assert 'foo.jpg' in response.json()['file']

    def test_update_action(self):
        image = PIL.Image.new('RGB', (100, 100))
        temp_file = tempfile.NamedTemporaryFile(suffix='.jpg')
        image.save(temp_file, format='JPEG')
        with open(temp_file.name, 'rb') as data_file:
            response = self.client.put('/api/images/1/',
                                       {'file': data_file},
                                       format='multipart')
            assert response.status_code == status.HTTP_200_OK
            assert temp_file.name.split('/')[-1] in response.json()['file']

    def test_delete_action(self):
        response = self.client.delete('/api/images/1/')
        assert response.status_code == status.HTTP_204_NO_CONTENT

        response = self.client.get('/api/images/1/')
        assert response.status_code == status.HTTP_404_NOT_FOUND
