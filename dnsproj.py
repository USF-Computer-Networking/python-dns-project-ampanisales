""" dnsproj.py

Author: Anthony Panisales

- Finds DNS resource records from a domain name

- Finds the hostname of an IP address

- Example usage: python dnsproj.py -a yahoo.com

- Example usage: python dnsproj.py -p 8.8.8.8

- Code for DNS queries inspired by this source:
    https://www.adampalmer.me/iodigitalsec/2014/11/21/performing-dns-queries-python/

"""

from __future__ import print_function
from future.utils import python_2_unicode_compatible
import argparse
import dns.resolver

def queryDNS(resRecType, domainName):
    print("\t" + resRecType)
    print("-----------------")
    myResolver = dns.resolver.Resolver()
    myAnswers = myResolver.query(domainName, resRecType)
    for rdata in myAnswers:
        print(rdata)

def queryAllTypes(domainName):
    rrTypes = ["A", "MX", "NS", "TXT"]
    for rrType in rrTypes:
        queryDNS(rrType, domainName)
        print("\n")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--address', default=False, help="Finds (address record) resource records")
    parser.add_argument('-m', '--mx', default=False, help="Finds (mail exchange record) resource records")
    parser.add_argument('-n', '--ns', default=False, help="Finds (name server record) resource records")
    parser.add_argument('-t', '--txt', default=False, help="Finds (text record) resource records")
    parser.add_argument('-e', '--entire', default=False, help="Finds all types of resource records available in this program")
    parser.add_argument('-p', '--ptr', default=False, help="Finds the hostname of an IP address")
    args = parser.parse_args()
    try:
        if args.address is not False:
            queryDNS("A", args.address)
        elif args.mx is not False:
            queryDNS("MX", args.mx)
        elif args.ns is not False:
            queryDNS("NS", args.ns)
        elif args.txt is not False:
            queryDNS("TXT", args.txt)
        elif args.entire is not False:
            queryAllTypes(args.entire)
        elif args.ptr is not False:
            queryDNS("PTR", '.'.join(reversed(args.ptr.split("."))) + ".in-addr.arpa")
        else:
            parser.print_help()
    except:
        print("Query failed")
