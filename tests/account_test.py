import unittest
from src.account import *
from src.profile import *

class TestAccount(unittest.TestCase):

    def setUp(self):

        # Creating some objects to use in the tests
        self.profile_1 = Profile("harrisonF", "myP@assword")
        self.profile_2 = Profile("markH", "anotherP@ssword")

        self.account_1 = Account("Jane", "Smith", "janes@email.com")

    # Test an Account has a first name

    def test_account_has_first_name(self):
        self.assertEqual("Jane", self.account_1.first_name)

    # Test an Account has a last name

    def test_account_has_last_name(self):
        self.assertEqual("Smith", self.account_1.last_name)

    # Test an Account has an email address

    def test_account_has_email_address(self):
        self.assertEqual("janes@email.com", self.account_1.email_address)

    # Test an Account can add a Profile

    def test_account_can_add_profile(self):
        self.account_1.add_profile(self.profile_1)
        self.assertEqual(1, len(self.account_1.profiles))

    # Test an Account can remove a given Profile

    def test_account_can_remove_profile(self):
        self.account_1.add_profile(self.profile_1)
        self.account_1.add_profile(self.profile_2)
        self.account_1.remove_profile(self.profile_1)
        self.assertEqual(1, len(self.account_1.profiles))

    # Test an Account can return a list of Profiles

   
