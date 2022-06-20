from google_images_download import google_images_download as gid
import os, errno, time
import unittest

class TestGoogleImagesDownload(unittest.TestCase):
    def test_download(self):
        start_time = time.time()
        argumnets = {
            "keywords": "Polar bears",
            "limit": 5,
            "print_urls": False,
            "proxy": "socks5://127.0.0.1:1080"
        }

        response = gid.googleimagesdownload()
        response.download(argumnets)