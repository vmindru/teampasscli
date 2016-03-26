#!/usr/bin/python

from optparse import OptionParser
from sys import exit
import StringIO
import os
import pycurl

progvers = 0.1

KEY = os.environ['TIM_KEY']
url = os.environ['TIM_URL']


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
                               "--action",
                               dest="action",
                               default='find',
                               help="specify the action e.g. find")
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
        valid_action = ["find", "get"]
        if not self.options.action in valid_action:
            print self.options.action + " is not a valid action"
            self.parser.print_help()
            exit(1)


class URL:
    def __init__(self, options):
        self.request_url = ''
        self.request = options.request
        self.build_url()
    def build_request(self):
        request = '/'+self.options.action+'/'+'/'+'vmindru'+self.options.item

    def build_url(self):
        self.request_url = (os.environ['TIM_URL'] +
                            '/api/index.php' +
                            self.request+'?apikey=' +
                            KEY)
        return self.request_url


class MAIN:
    def __init__(self):
        mOpts = BuildOpts()
        self.options = mOpts.options
        self.url = URL(self.options)

    def curl_request(self, url, options):
        c = pycurl.Curl()
        b = StringIO.StringIO()
        c.setopt(pycurl.URL, url)
        c.setopt(pycurl.WRITEFUNCTION, b.write)
        c.setopt(pycurl.FOLLOWLOCATION, 1)
        c.setopt(pycurl.MAXREDIRS, 5)
        c.perform()
        html = b.getvalue()
        return html

if __name__ == "__main__":
    m = MAIN()
    print m.curl_request()
