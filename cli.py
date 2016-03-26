#!/usr/bin/python

from optparse import OptionParser
from sys import exit
import os
import pycurl

progvers = 0.1

KEY = os.environ['TIM_KEY']
URL = os.environ['TIM_URL']


class BuildOpts:
    def __init__(self):
        self.collect_opts()
        self.validate_options()

    def collect_opts(self):
        epilog = ("ENV_VARS: TIM_KEY,TIM_URL")
        self.parser = OptionParser(version=progvers,
                                   usage=("usage: %prog [-r]"),
                                   epilog = epilog
                                   )
        self.parser.description = ('TeamPass,search passwords with CLI')
        self.parser.add_option("-r",
                               "--request",
                               dest="request",
                               default='find',
                               help="specify the request e.g. find")
        self.parser.add_option("-i",
                               "--item",
                               dest="item",
                               default="*",
                               help="specify teh search criteria e.g. *\
                               for all")
        (options, args) = self.parser.parse_args()
        self.options = options
        return options

    def validate_options(self):
        valid_request = ["find", "get"]
        if not self.options.request in valid_request:
            print self.options.request + " is not a valid request"
            self.parser.print_help()
            exit(1)


class BUILD_URL:
    def __init__(self, opts):
        self.REQUEST_URL = ''
        self.REQUEST = opts.request
        self.build_url()

    def build_url(self, REQUEST):
        self.REQUEST_URL = (os.environ['TIM_URL'] +
                    '/api/index.php' +
                    REQUEST+'?apikey=' +
                    KEY)


b = BuildOpts()
options = b.options

c = pycurl.Curl()
#c.setopt(pycurl.URL, URL)
#c.perform()
