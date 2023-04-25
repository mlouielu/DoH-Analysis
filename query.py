import time

import dns.resolver
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from doh import doh


def udp(dns_server: str, qname: str):
    # Create a resolver object
    resolver = dns.resolver.Resolver()
    resolver.nameservers = [dns_server]

    # Send a DNS query for the A record of the domain
    answer = resolver.query(qname, "A")

    # for ip_address in answer:
    #    print(ip_address)


def firefox_headless(url: str):
    options = Options()
    options.add_argument("-headless")

    with webdriver.Firefox(options=options) as driver:
        driver.get(url)


def verify():
    for i in range(100):
        doh("https://dns.cloudflare.com/dns-query", "louie.lu", True)
        doh("https://dns.cloudflare.com/dns-query", "google.com", True)
        doh("https://dns.cloudflare.com/dns-query", "cs.unc.edu", True)


def unverify():
    for i in range(100):
        doh("https://dns.cloudflare.com/dns-query", "louie.lu", False)
        doh("https://dns.cloudflare.com/dns-query", "google.com", False)
        doh("https://dns.cloudflare.com/dns-query", "cs.unc.edu", False)


def baseline():
    for i in range(100):
        doh("https://192.168.88.195:853/dns-query", "louie.lu", False)
        doh("https://192.168.88.195:853/dns-query", "google.com", False)
        doh("https://192.168.88.195:853/dns-query", "cs.unc.edu", False)


def test(url):
    for i in range(100):
        doh(f"https://{url}/dns-query", "louie.lu", False)
        doh(f"https://{url}/dns-query", "google.com", False)
        doh(f"https://{url}/dns-query", "cs.unc.edu", False)


def test_udp(server):
    for i in range(100):
        udp(server, "louie.lu")
        udp(server, "google.com")
        udp(server, "cs.unc.edu")


def test_firefox_headless(server, target_url):
    for i in range(10):
        # XXX: Setup the DNS server??
        print(f"{i}th firefox headless")
        firefox_headless(target_url)


def main():
    verify()


if __name__ == "__main__":
    main()
