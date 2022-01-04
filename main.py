#!/usr/bin/env python

# This script converts an hex IP address to an decimal ip address

import sys

__author__ = "Thomas Marko"
__copyright__ = "Copyright 2018, Thomas Marko"
__credits__ = ["Thomas Marko"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Thomas Marko"
__email__ = "office@berge.priv.at"
__status__ = "Development"

ip_hex = sys.argv[1]
ip_dec = []

if len(ip_hex) == 0:
    exit(1)

parts_hex = [ip_hex[i:i + 2] for i in range(0, len(ip_hex), 2)]

for octet in range(len(parts_hex)):
    ip_dec.append(int(parts_hex[octet], 16))

ip_dec_str = '.'.join(str(e) for e in ip_dec)

print "Hex IP: " + ip_hex + " entspricht dezimal " + ip_dec_str
