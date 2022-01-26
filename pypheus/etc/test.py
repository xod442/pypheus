#!/usr/bin/env python3
# coding=utf-8
# author: @netwookie.
# -*- coding: utf-8 -*-
"""
This is a test file that gets a token
"""
import urllib3
urllib3.disable_warnings()
from auth import Auth
import json
import requests

host='10.132.0.153'
username='xod442'
password='ilike2Rock@'

my_token = Auth(host,username,password)

url = 'https://' + host + '/api/networks'

cred = "BEARER " + my_token.access_token

headers = {
    'Authorization':cred,
    'Accept': 'application/json'
}

response = requests.get(url, headers=headers, verify=False)
# response = requests.get(provision_types_url, headers=headers)
print(response.text)
