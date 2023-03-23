#!/usr/bin/env python3
#
# This is an example of sending DNS queries over HTTPS (DoH) with dnspython.
import httpx

import dns.message
import dns.query
import dns.rdatatype


def doh(where: str, qname: str, verify: bool = False):
    with httpx.Client(verify=False) as client:
        q = dns.message.make_query(qname, dns.rdatatype.A)
        r = dns.query.https(q, where, session=client)
        # print(r)


def main():
    where = "https://192.168.88.195:853/dns-query"
    where = "https://dns.cloudflare.com/dns-query"
    qname = "louie.lu"
    with httpx.Client(verify=False) as client:
        q = dns.message.make_query(qname, dns.rdatatype.A)
        r = dns.query.https(q, where, session=client)


if __name__ == "__main__":
    main()
