import unittest
from src.movie import Movie

class TestMovie(unittest.TestCase):

    def setUp(self):
        self.movie = Movie("Grease", "Amy Gallacher", 4)

    def test_movie_has_name(self):
        self.assertEqual("Grease", self.movie.title)

    def test_movie_has_director(self):
        self.assertEqual("Amy Gallacher", self.movie.director)

    def test_movie_has_rating(self):
        self.assertEqual(4, self.movie.rating)