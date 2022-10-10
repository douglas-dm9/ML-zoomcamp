#!/usr/bin/env python
# coding: utf-8

import requests


url = 'http://localhost:9696/predict'


client = {"reports": 0, "share": 0.001694, "expenditure": 0.12, "owner": "yes"}

response = requests.post(url, json=client).json()
print(response)
