#!/usr/bin/python2

import os


def get_whois(url):
    print('\t*Getting whois')
    command = 'whois ' + url
    process = os.popen(command)
    results = str(process.read())
    return results
