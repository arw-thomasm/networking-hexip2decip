# This script converts an hex IP address to an decimal ip address
import sys

def convert(ip_hex: str):

    ip_dec = []

    if len(ip_hex) == 0:
        exit(1)

    parts_hex = [ip_hex[i:i + 2] for i in range(0, len(ip_hex), 2)]

    for octet in range(len(parts_hex)):
        ip_dec.append(int(parts_hex[octet], 16))

    ip_dec_str = '.'.join(str(e) for e in ip_dec)

    return ip_dec_str

def userinput():
    
    hex_ip = str(input("Hexdecimal IP address? "))
    return hex_ip

if __name__ == '__main__':

    ip_hex = userinput()
    ip_dec = convert(ip_hex)

    print("Hex IP: " + ip_hex + " converts to Decimal IP: " + ip_dec)

