#!/usr/bin/python3

import requests

url = "http://natas5.natas.labs.overthewire.org/"

s = requests.Session()
s.auth = ('natas5', 'iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq')
r = s.get(url)


print(r.headers)
