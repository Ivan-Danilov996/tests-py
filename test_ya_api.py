import unittest

from ya_api import create_ya_disc_folder, get_ya_disc_folder


class TestApi(unittest.TestCase):
    def test_create_ya_disc_folder(self):
        self.assertEqual('201', create_ya_disc_folder({'path': 'new folder'}))

    def test_get_ya_disc_folder(self):
        self.assertEqual('200', get_ya_disc_folder({'path': 'new folder'}))
