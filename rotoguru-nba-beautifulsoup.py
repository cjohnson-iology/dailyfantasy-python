#!/usr/env python

'''
rotogure-nba-beautifulsoup.py
testing parsing using bs4


'''

from bs4 import BeautifulSoup
import httplib2
import os
from urllib import urlencode


def from_file(fn):

    content = None

    if os.path.isfile(fn):
        try:
            with open(fn) as x:
                content = x.read()
        except:
            pass

    return content


def from_web():

    content = None
    handler = httplib2.Http(".cache")
    #handler = httplib2.Http()

    base_url = 'http://rotoguru1.com/cgi-bin/hoopstat-daterange.pl?'

    params = {
      'startdate': '20141028',
      'date': '20141028',
      'saldate': '20141028',
      'g': 0,
      'gameday': '20141028',
      'ha': '',
      'min': '',
      'tmptmin': 0,
      'tmptmax': 999,
      'opptmin': 0,
      'opptmax': 999,
      'gmptmin': 0,
      'gmptmax': 999,
      'sd': 0
    }

    url = base_url + urlencode(params)

    (resp, body) = handler.request(url, "GET")

    if resp.status == 200:
        content = body

    return content


if __name__ == '__main__':

    fn = 'rg.html'
    content = from_file(fn)
    soup = BeautifulSoup(content)
    print(soup.prettify())
