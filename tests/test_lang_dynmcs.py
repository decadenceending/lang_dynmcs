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
    def test_velocity(self):
        self.assertEqual(position(xi=1,dtime=0.01), 1.01)
        tests = unittest.TestLoader().loadTestsFromTestCase(TestLang_dynmcs)
        unittest.TextTestRunner().run(tests)
    def test_position(self):
        self.assertEqual(velocity(vi=1,dtime=0.01), 1.01)
        tests = unittest.TestLoader().loadTestsFromTestCase(TestLang_dynmcs)
        unittest.TextTestRunner().run(tests)
    def test_force(self):
        self.assertEqual(forcenet(m=0.0001,vnext=1.02,vi=1,dtime=0.01), 0.0001)
        tests = unittest.TestLoader().loadTestsFromTestCase(TestLang_dynmcs)
        unittest.TextTestRunner().run(tests)

if __name__ == '__main__':
    sys.exit(unittest.main())
