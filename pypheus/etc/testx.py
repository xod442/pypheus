#!/usr/bin/env python3
# coding=utf-8
# author: @netwookie.
# -*- coding: utf-8 -*-
"""
This is a test file that tests the API
"""
import urllib3
urllib3.disable_warnings()
from network import Network
from storage import Storage
from monitoring import Monitoring
import json
import requests

host='10.132.0.153'
username='xod442'
password='ilike2Rock@'
'''
nets = Network(host,username,password)
info = nets.get_all_networks()
print(info)
info = nets.network_types()
print(info)
info = nets.network_routers()
print(info)


monitor = Monitoring(host,username,password)
info = monitor.get_all_checks()
print(info)
info = monitor.get_all_incidents()
print(info)
info = monitor.get_all_alerts()
print(info)
info = monitor.get_all_contacts()
print(info['storageVolumes'])

'''
storage = Storage(host,username,password)
info = storage.get_all_volumes()
for v in info['storageVolumes']:
    print('===========================================')
    print(v)
'''
info = storage.get_all_buckets()
print(info)
info = storage.get_all_servers()
print(info)
info = storage.get_all_server_types()
print(info)
'''
