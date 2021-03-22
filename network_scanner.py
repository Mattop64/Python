#!/usr/bin/env python

import scapy.all as scapy
import optparse

def get_range():
    parser = optparse.OptionParser()
    parser.add_option("-r", "--range", dest="range", help="Enter the range of addresses you would like to scan")
    (options, arguments) = parser.parse_args()
    if not options.range:
        parser.error("[-] Please enter a range of addresses to scan")
    return options

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    clients_list = []
    for element in answered:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        clients_list.append(client_dict)
    return clients_list

def print_results(results_list):
    print("IP\t\t\tMAC\n-----------------------------------------")
    for client in results_list:
        print(client["ip"] + "\t\t" + client["mac"])

range = get_range()
scan_result = scan(range.range)
print_results(scan_result)