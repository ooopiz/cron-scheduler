#!/usr/bin/env python3

import os
import requests


env_token = os.environ.get('SUPER_VAR')
if not env_token:
  raise ValueError('Token missing ...')


#token_list = token_env.split(';')
#for token in token_list:
#    headers = {"Authorization": "Bearer " + token}
#    payload = {'message': 'hello2'}
#    url = 'https://notify-api.line.me/api/notify'
#    response = requests.post(url, headers=headers, data=payload)