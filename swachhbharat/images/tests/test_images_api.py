import tempfile

from rest_framework import status
from rest_framework.test import APITestCase
from django.core.files import File
import PIL.Image

from swachhbharat.images.models import Image


class ImageApiTest(APITestCase):

    def create_image(self, suffix='.jpg'):
        """
        Helper method to create a temporary image.
        image_name is NOT the full path.
        :returns: (image_name, file_handle)
        """
        image = PIL.Image.new('RGB', (100, 100))
        temp_file = tempfile.NamedTemporaryFile(suffix=suffix)
        image_name = temp_file.name.split('/')[-1]
        image.save(temp_file.name)
        return image_name, temp_file

    def setUp(self):
        # Insert ten random images.
        self.inserted_images = []
        for _ in range(10):
            image_name, image_file = self.create_image()
            django_file = File(image_file)
            django_file.name = image_name
            image = Image(file=django_file)
            image.save()
            self.inserted_images += image_name

    def test_list_action(self):
        response = self.client.get('/api/images/')
        assert response.status_code == status.HTTP_200_OK

        # Verify that all the fixture images are returned
        returned_urls = set(result['file'] for result in response.json()['results'])
        for image_name in self.inserted_images:
            assert any(image_name in url for url in returned_urls)

    def test_create_action(self):
        _, temp_file = self.create_image()
        with open(temp_file.name, 'rb') as data_file:
            response = self.client.post('/api/images/', 
                                        {'file': data_file}, 
                                        format='multipart')
            assert response.status_code == status.HTTP_201_CREATED

    def test_retrieve_action(self):
        response = self.client.get('/api/images/1/')
        assert response.status_code == status.HTTP_200_OK
        assert self.inserted_images[0] in response.json()['file']

    def test_update_action(self):
        image_name, temp_file = self.create_image()
        with open(temp_file.name, 'rb') as data_file:
            response = self.client.put('/api/images/1/',
                                       {'file': data_file},
                                       format='multipart')
            assert response.status_code == status.HTTP_200_OK
            assert image_name in response.json()['file']

    def test_delete_action(self):
        response = self.client.delete('/api/images/1/')
        assert response.status_code == status.HTTP_204_NO_CONTENT

        response = self.client.get('/api/images/1/')
        assert response.status_code == status.HTTP_404_NOT_FOUND