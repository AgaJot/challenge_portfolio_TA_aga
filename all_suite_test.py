import unittest

from unittest.loader import makeSuite


from test_cases.add_a_player_button import TestAddaPlayerButton
from test_cases.add_player_to_the_panel import TestPlayerForm
from test_cases.framework import Test
from test_cases.login_to_the_system import TestLoginPage


def full_suite():
   test_suite = unittest.TestSuite()
   test_suite.addTest(makeSuite(TestLoginPage))
   test_suite.addTest(makeSuite(TestAddaPlayerButton))
   test_suite.addTest(makeSuite(TestPlayerForm))
   test_suite.addTest(makeSuite(Test))
   return test_suite

if __name__ == '__main__':
   runner = unittest.TextTestRunner(verbosity=2)
   runner.run(full_suite())