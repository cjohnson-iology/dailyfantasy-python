#!/usr/env python

'''
#rotoguru-nba.py

This is the bootstrap script for getting all of the 2014-15 (and future season when applicable)
salary and player data from rotoguru.net

Uses the RotoGuruParser and RotoGuruScraper classes.

Right now saves values to pickle file until I figure out what I want to do with them

'''

import datetime
import logging
import pickle
import sys
import time
sys.path.append("/home/sansbacon/workspace/dailyfantasy-python/lib")
from RotoGuruParser import RotoGuruParser
from RotoGuruScraper import RotoGuruScraper


def date_list(d1, d2):
    # need to first determine if date object or datestring
    if isinstance(d1, basestring):
        earlier = datetime.datetime.strptime(d1, '%Y%m%d')

    if isinstance(d2, basestring):
        later = datetime.datetime.strptime(d2, '%Y%m%d')

    # calculate difference between two dates
    # then have to add one to season.days to get the earliest date in the list
    season = later - earlier
    return [later - datetime.timedelta(days=x) for x in range(0, season.days+1)]

def setup_logging():
    # setup logging
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger

# main program
pages = {}
stats = {}
s = RotoGuruScraper()
p = RotoGuruParser()
logger = setup_logging()

for day in date_list('20141028', '20141031'):

    daystr = datetime.datetime.strftime(day, "%Y%m%d")
    extra_params = {
        'startdate': daystr,
        'date': daystr,
        'saldate': daystr,
        'gameday': daystr
    }

    content, url = s.nba_players(extra_params=extra_params)
    pages[day] = {'url': url, 'content': content}
    players = p.nba_players(content)
    stats[day] = players
    time.sleep(1)

pickle.dump(pages, open("pages2.p", "wb"))
pickle.dump(stats, open("stats2.p", "wb"))
