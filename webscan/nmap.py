#!/usr/bin/python2

import os


def get_nmap(options, ip):
    print('\t*Nmap data')
    command = 'nmap ' + options + ' ' + ip
    process = os.popen(command)
    results = str(process.read())
    return results
