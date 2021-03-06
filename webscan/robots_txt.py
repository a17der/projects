#!/usr/bin/python2

import urllib2
import io


def get_robots_txt(url):
    print('\t*Getting robots.txt')
    if url.endswith('/'):
        path = url
    else:
        path = url + '/'
    req = urllib2.urlopen(path + 'robots.txt', data=None)
    data = io.TextIOWrapper(req, encoding='utf-8')
    return data.read()
