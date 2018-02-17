""" dnsproj.py

Author: Anthony Panisales

- Finds DNS resource records from a domain name

- Example usage: python dnsproj.py -a yahoo.com

- Code for DNS queries inspired by this source:
    https://www.adampalmer.me/iodigitalsec/2014/11/21/performing-dns-queries-python/

"""

from __future__ import print_function
from future.utils import python_2_unicode_compatible
import argparse
import dns.resolver

def query(resRecType, domainName):
    print("\t" + resRecType)
    print("-----------------")
    myResolver = dns.resolver.Resolver()
    myAnswers = myResolver.query(domainName, resRecType)
    for rdata in myAnswers:
        print(rdata)

def all(domainName):
    rrTypes = ["A", "MX", "NS", "TXT"]
    for rrType in rrTypes:
        query(rrType, domainName)
        print("\n")

parser = argparse.ArgumentParser()
parser.add_argument('-a', '--address', default=False, help="Finds (address record) resource records")
parser.add_argument('-m', '--mx', default=False, help="Finds (mail exchange record) resource records")
parser.add_argument('-n', '--ns', default=False, help="Finds (name server record) resource records")
parser.add_argument('-t', '--txt', default=False, help="Finds (text record) resource records")
parser.add_argument('-e', '--entire', default=False, help="Finds all types of resource records available in this program")

if __name__ == '__main__':
    args = parser.parse_args()
    try:
        if args.address is not False:
            query("A", args.address)
        elif args.mx is not False:
            query("MX", args.mx)
        elif args.ns is not False:
            query("NS", args.ns)
        elif args.txt is not False:
            query("TXT", args.txt)
        elif args.entire is not False:
            all(args.entire)
    except:
        print("Query failed")
