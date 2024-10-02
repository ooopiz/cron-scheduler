#!/usr/bin/env python3

import os

print('action test')
for key, value in os.environ.items():
    print(f'{key}: {value}')