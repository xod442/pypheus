# -*- coding: utf-8 -*-
"""
Module for testing the functions in pypheus.network.
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

SKIPTEST=True

#TODO TAKE OUT HARDCODED DATA LATER
my_vcr = vcr.VCR(
    serializer='json',
    cassette_library_dir='./test_pyhpecfm/fixtures/cassettes',
    record_mode='new_episodes',
    match_on=['uri', 'method'],
)

class Networks(TestCase):
    """
    Test Case for pypheus.network get_all_networks function
    """
    @vcr.use_cassette(cassette_library_dir='./test_pypheus/fixtures/cassettes')

    def get_all_networks(self):
        """
        Simple test to return networks. URL has an ID parameter that is optional
        :return:
        """
        nets = Network(host,username,password)
        test_networks = nets.get_all_networks()
        self.assertIs(type(test_networks), list)
        self.assertIs(type(test_networks[0]), dict)

    def get_network_types(self):
        """
        Simple test to return network-types. URL has an ID parameter that is optional
        :return:
        """
        nets = Network(host,username,password)
        test_networks = nets.network_types()
        self.assertIs(type(test_networks), list)
        self.assertIs(type(test_networks[0]), dict)

    def get_network_routers(self):
        """
        Simple test to return network-routers. URL has an ID parameter that is optional
        :return:
        """
        nets = Network(host,username,password)
        test_networks = nets.network_routers()
        self.assertIs(type(test_networks), list)
        self.assertIs(type(test_networks[0]), dict)
