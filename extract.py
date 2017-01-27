import re
import sys
import socket
import requests

IP_REGEX = re.compile('\\b(?:[0-9]{1,3}\\.){3}[0-9]{1,3}\\b')
IP_INFO_URL = 'http://freegeoip.net/json/{}'


def get_ip_addrs(file):
    ip_addrs = {}
    lines = file.readlines()
    sys.stdout.write("{} line file read, analyzing".format(len(lines)))
    sys.stdout.flush()
    for line in lines:
        match = IP_REGEX.findall(line)
        if len(match) > 0 and match[0] not in ip_addrs.keys():
            try:
                host = socket.gethostbyaddr(match[0])
            except socket.herror:
                host = ['UNKNOWN']
            ip_addrs[match[0]] = [host[0], get_country(match[0])]
            sys.stdout.write(".")
            sys.stdout.flush()
    return ip_addrs


def get_country(ip_addr):
    resp = requests.get(IP_INFO_URL.format(ip_addr))
    host_info = resp.json()
    return host_info['country_name']


def print_ips(ip_addrs):
    for ip, hostname in ip_addrs.iteritems():
        print(ip + '\t' + hostname[1] + '\t' + hostname[0])


if __name__ == '__main__':
    filename = sys.argv[1]
    with open(filename) as f:
        ip_addrs = get_ip_addrs(f)
    print('\n\nIP Addresses found in {}:'.format(filename))
    print_ips(ip_addrs)
