#!/usr/bin/python2

import os


def get_ip_address(url):
    print('\t*Getting ip address')
    command = 'host ' + url
    process = os.popen(command)
    results = str(process.read())
    marker = results.find('has address') + 12
    return results[marker:].splitlines()[0]
