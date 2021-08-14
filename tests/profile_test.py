import unittest
from src.profile import *
from src.movie import *

class TestProfile(unittest.TestCase):

    def setUp(self):

        # Creating some objects to use in the tests
        self.movie_1 = Movie("The Fugitive", "Andrew Daivs", 9)
        self.movie_2 = Movie("Hunger Games", "Gary Ross", 7)

        self.profile_1 = Profile("harrisonF", "myP@assword")

    # Test a Profile has a username

    def test_profile_has_username(self):
        self.assertEqual("harrisonF", self.profile_1.username)

    # Test a Profile has a password

    def test_profile_has_password(self):
        self.assertEqual("myP@assword", self.profile_1.password)

    # Test a Profile can add a favourite Movie

    def test_profile_can_add_favourite_movie(self):
        self.profile_1.add_favourite_movie(self.movie_1)
        self.assertEqual(1, len(self.profile_1.favourite_movies))

    # Test a Profile can remove a given Movie from favourites

    def test_profile_can_remove_favourite_movie(self):
        self.profile_1.add_favourite_movie(self.movie_1)
        self.profile_1.remove_favourite_movie(self.movie_1)
        self.assertEqual(0, len(self.profile_1.favourite_movies))

    # Test a Profile can return a list of Favourites

    # def test_profile_can_return_favourite_movies(self):
    #     self.profile_1.add_favourite_movie(self.movie_1)
    #     self.assertEqual(self.movie_1, self.profile_1.return_favourite_movies())
