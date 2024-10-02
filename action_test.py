#!/usr/bin/env python3

import os
import requests


for key, value in os.environ.items():
    print(f'{key}: {value}')

token_env = os.environ.get('SUPER_VAR')
token_list = token_env.split(';')
for token in token_list:
    headers = {"Authorization": "Bearer " + token}
    payload = {'message': 'hello2'}
    url = 'https://notify-api.line.me/api/notify'
    response = requests.post(url, headers=headers, data=payload)