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

    def test_potential_energy(self):
        Uenergy=potential_energy()
        ActLength=len(Uenergy)
        ExpLength=200
        self.assertEqual(ExpLength,ActLength)

    def test_force_net(self):
        Fnet=force_net(1,1,1,[1,2,3],0)
        self.assertTrue(Fnet>-1.9)

    def test_acceleration(self):
        accl=acceleration(10,0.1)
        acclExp=100
        self.assertEqual(accl,acclExp)

    def test_velocity(self):
        vi=velocity(1,0.01,0)
        viExp=1
        self.assertEqual(vi,viExp)

    def test_position(self):
        xi=position(0,0.01,1)
        xiExp=0.01
        self.assertEqual(xi,xiExp)
