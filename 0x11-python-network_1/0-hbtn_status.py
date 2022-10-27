#!/usr/bin/python3

import urllib.requestwith urllib.request.urlopen('https://alx-intranet.hbtn.io/status

') as response:
   html = response.read()
