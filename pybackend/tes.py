import unittest
import file_manipulation


class MyTestCase(unittest.TestCase):
    def test_something(self):
        f = open("testing.txt", "r")
        links = f.read()
        links = links.split(',')
        down = file_manipulation

        for i in links:
            down.Download(i, 'name', 'pybackend/MP3-Files/testing')

        expSongs = ""
        self.assertEqual(down.show_songs('pybackend/MP3-Files/testing'), expSongs)  # add assertion here
