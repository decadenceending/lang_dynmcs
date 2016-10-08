#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_lang_dynmcs
----------------------------------

Tests for `lang_dynmcs` module.
"""


import sys
import unittest
from contextlib import contextmanager


from lang_dynmcs import lang_dynmcs

def testaccl(Fnet):
    return Fnet/0.001
def testvel(accl):
    return 1+accl*0.01
def testpos(vel):
    return 1+vel*0.01

class TestLang_dynmcs(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_000_something(self):
        pass

    def test_command_line_interface(self):
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output
    def test_accl(self):
        self.assertEqual(testaccl(1.01), 1010)
        tests = unittest.TestLoader().loadTestsFromTestCase(TestLang_dynmcs)
        unittest.TextTestRunner().run(tests)
    def test_velocity(self):
        self.assertEqual(testvel(1010), 11.1)
        tests = unittest.TestLoader().loadTestsFromTestCase(TestLang_dynmcs)
        unittest.TextTestRunner().run(tests)
    def test_position(self):
        self.assertEqual(testpos(11.1), 1.111)
        tests = unittest.TestLoader().loadTestsFromTestCase(TestLang_dynmcs)
        unittest.TextTestRunner().run(tests)

if __name__ == '__main__':
    sys.exit(unittest.main())
