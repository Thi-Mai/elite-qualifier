#copied

import unittest
from main import suggest

class TestUserInput(unittest.TestCase):

    def test_user_input(self):
        self.assertEqual(suggest("What is your name?"), "My name is chatbot! What's yours?")

        self.assertEqual(suggest(""), "Sorry I didn't understand that.")
    

if __name__ == '__main__':
    unittest.main()