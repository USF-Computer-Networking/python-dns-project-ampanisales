""" dnsproj.py

Author: Anthony Panisales

- Finds DNS resource records from a domain name

- Code for DNS queries inspired by this source:
	https://www.adampalmer.me/iodigitalsec/2014/11/21/performing-dns-queries-python/

"""

from __future__ import print_function
from future.utils import python_2_unicode_compatible
import argparse
import dns.resolver

def query(resRecType, domainName):
    myResolver = dns.resolver.Resolver()
    myAnswers = myResolver.query(domainName, resRecType)
    for rdata in myAnswers:
        print(rdata)

parser = argparse.ArgumentParser()
parser.add_argument('-a', default=False, help="Finds (address record) resource records")
parser.add_argument('-m', default=False, help="Finds (mail exchange record) resource records")
parser.add_argument('-n', default=False, help="Finds (name server record) resource records")
parser.add_argument('-t', default=False, help="Finds (text record) resource records")

if __name__ == '__main__':
    args = parser.parse_args()
    try:
        if args.a is not False:
            query("A", args.a)
        elif args.m is not False:
            query("MX", args.m)
        elif args.n is not False:
            query("NS", args.n)
        elif args.t is not False:
            query("TXT", args.t)
    except:
        print("Error: Invalid domain name")
