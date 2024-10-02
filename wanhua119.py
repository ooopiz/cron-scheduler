#!/usr/bin/env python3

import requests
from datetime import datetime, timedelta
import pytz
import os


def main():
    env_token = os.environ.get('LINE_TOKENS')
    if not env_token:
        raise ValueError('Token missing ...')

    taipei_timezone = pytz.timezone('Asia/Taipei')
    now = datetime.now(taipei_timezone)
    time_shift = now - timedelta(minutes=120)

    url = "https://service119.tfd.gov.tw/service119/citizenCase/caseList"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.post(url, headers=headers)
    data = response.json()
    wanhua_events = list(filter(
        lambda x: '萬華區' in x['csPlaceFuzzy'] and datetime.strptime(x['inTime'], "%Y/%m/%d %H:%M:%S").replace(tzinfo=taipei_timezone) > time_shift,
        data['rows']))

    if len(wanhua_events) == 0:
        print('No events in 30 minutes')
        return

    message = "\nhttps://service119.tfd.gov.tw/service119/accCase"
    for case in wanhua_events:
        message += f"\n{case['inTime']} {case['csPlaceFuzzy']}, {case['csKindName']} {case['caseStatus']}"

    print(message)

    token_list = env_token.split(';')
    for token in token_list:
        headers = {"Authorization": "Bearer " + token}
        payload = {'message': message}
        url = 'https://notify-api.line.me/api/notify'
        response = requests.post(url, headers=headers, data=payload)


if __name__ == "__main__":
    main()
