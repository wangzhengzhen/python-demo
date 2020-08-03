#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import urllib
import urllib.request

def get(url):
    res = urllib.requests.get(url)
    result = res.text
    print(result)

def post(url):
    user_agent = "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"
    values = {'name': '111'}
    headers = { 'User-Agent': userAgent }
    data = urllib.parse.urlencode(values)
    req = urllib.request.Request(url+'?'+data)
    response = urllib.request.urlopen(req)
    the_page = response.read()
    print(the_page)
    print(the_page.decode('UTF8'))
