#!/usr/bin/python2

from urlparse import urlparse


def get_domain_name(url):
    print('\t*Getting domain name')
    parsed_uri = urlparse(url)
    # domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
    domain_name = '{uri.netloc}'.format(uri=parsed_uri)
    domain_name = domain_name[4:]
    return domain_name
