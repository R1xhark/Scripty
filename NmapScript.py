# -*- coding: utf-8 -*-
#!/usr/bin/env python3

import nmap
import subprocess

def install_nmap():
    print("nmap is not installed. Installing...")
    subprocess.call(["sudo", "apt-get", "update"])
    subprocess.call(["sudo", "apt-get", "install", "nmap"])

def check_nmap():
    p = subprocess.Popen(["which", "nmap"], stdout=subprocess.PIPE)
    output = p.communicate()[0].decode()
    if "nmap" not in output:
        install_nmap()

def scan_network(ip_range):
    nm = nmap.PortScanner()
    nm.scan(hosts=ip_range, arguments='-sn')

    for host in nm.all_hosts():
        print("Found device: %s (%s)" % (host, nm[host]['vendor']))

if __name__ == '__main__':
    # Check if nmap is installed
    check_nmap()

    # Set the IP range to scan
    ip_range = '192.168.1.0/24'

    # Perform the network scan
    scan_network(ip_range)
