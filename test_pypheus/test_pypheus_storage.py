# -*- coding: utf-8 -*-
"""
Module for testing the functions in pypheus.storage.
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

class Storage(TestCase):
    """
    Test Case for pypheus.storage functions
    """
    @vcr.use_cassette(cassette_library_dir='./test_pypheus/fixtures/cassettes')

    def get_all_volumes(self):
        """
        Simple test to return volumes.
        :return:
        """
        store = Storage(host,username,password)
        test_storage = store.get_all_volumes()
        self.assertIs(type(test_storage), list)
        self.assertIs(type(test_storage[0]), dict)

    def get_all_buckets(self):
        """
        Simple test to return buckets.
        :return:
        """
        store = Storage(host,username,password)
        test_storage = store.get_all_buckets()
        self.assertIs(type(test_storage), list)
        self.assertIs(type(test_storage[0]), dict)

    def get_all_servers(self):
        """
        Simple test to return storage servers.
        :return:
        """
        store = Storage(host,username,password)
        test_storage = store.get_all_servers()
        self.assertIs(type(test_storage), list)
        self.assertIs(type(test_storage[0]), dict)

    def get_all_server_types(self):
        """
        Simple test to return storage server-types.
        :return:
        """
        store = Storage(host,username,password)
        test_storage = store.get_all_server_types()
        self.assertIs(type(test_storage), list)
        self.assertIs(type(test_storage[0]), dict)

    v
