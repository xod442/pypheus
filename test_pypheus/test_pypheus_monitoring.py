# -*- coding: utf-8 -*-
"""
Module for testing the functions in pypheus.monitoring.
"""

import os
import vcr
from unittest import TestCase
from unittest import mock
from nose.plugins.skip import SkipTest
import urllib3
urllib3.disable_warnings()
import json
import requests

from pypheus.network import Network
from pypheus.storage import Storage
from pypheus.logs import Logs
from pypheus.monitoring import Monitoring

host = os.environ['HOST']
username = os.environ['USERNAME']
password = os.environ['PASSWORD']

test = Monitoring(host,username,password)

SKIPTEST=True

#TODO TAKE OUT HARDCODED DATA LATER
my_vcr = vcr.VCR(
    serializer='json',
    cassette_library_dir='./test_pyhpecfm/fixtures/cassettes',
    record_mode='new_episodes',
    match_on=['uri', 'method'],
)

class Monitoring(TestCase):
    """
    Test Case for pypheus.monitoring functions
    """
    @vcr.use_cassette(cassette_library_dir='./test_pypheus/fixtures/cassettes')

    def test_get_all_checks(self):
        """
        Simple test to return checks.
        :return:
        """
        test_checks = test.get_all_checks()
        self.assertIs(type(test_checks['checks']), list)
        self.assertIs(type(test_checks['checks'][0]), dict)

    def test_get_all_incidents(self):
        """
        Simple test to return incidents.
        :return:
        """
        test_incidents = test.get_all_incidents()
        self.assertIs(type(test_incidents['incidents']), list)
        self.assertIs(type(test_incidents['incidents'][0]), dict)

    def test_get_all_alerts(self):
        """
        Simple test to return alerts.
        :return:
        """
        test_alerts = test.get_all_alerts()
        self.assertIs(type(test_alerts['alerts']), list)
        self.assertIs(type(test_alerts['alerts'][0]), dict)

    def test_get_all_contacts(self):
        """
        Simple test to return contacts.
        :return:
        """
        test_contacts = test.get_all_contacts()
        self.assertIs(type(test_contacts['contacts']), list)
        self.assertIs(type(test_contacts['contacts'][0]), dict)
