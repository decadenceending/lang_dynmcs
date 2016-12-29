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
from click.testing import CliRunner

from lang_dynmcs import lang_dynmcs
from lang_dynmcs import cli
from lang_dynmcs import *


class TestLang_dynmcs(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_000_something(self):
        pass

    def test_command_line_interface(self):
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'lang_dynmcs.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output

    def test_acceleration(self):
        acclExp=100
        self.assertEqual(acceleration(10,0.1),acclExp)
