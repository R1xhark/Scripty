# -*- coding: utf-8 -*-
#!/usr/bin/env python3

import os
import subprocess

def check_pxe_boot():
    # Check if the network interface is up
    if "eth0" not in os.listdir("/sys/class/net"):
        print("Error>> eth0 not responding, check eth0 interface")
        return

    # Check if PXE boot is enabled in BIOS
    p = subprocess.Popen(["dmidecode", "-s", "bios-version"], stdout=subprocess.PIPE)
    output = p.communicate()[0].decode()
    if "PXE" not in output:
        print("Error>> PXE not active, please check bios settings")
        return

    # Check if DHCP server is reachable
    p = subprocess.Popen(["ping", "-c", "1", "dhcp-server"], stdout=subprocess.PIPE)
    output = p.communicate()[0].decode()
    if "1 received" not in output:
        print("Error>> DHCP connection not reachable, please check DHCP setting or psysichal connection")
        return

    # Check if TFTP server is reachable
    p = subprocess.Popen(["ping", "-c", "1", "tftp-server"], stdout=subprocess.PIPE)
    output = p.communicate()[0].decode()
    if "1 received" not in output:
        print("Error>> TFTP server connection is not reachable, please contact TFTP server admid for assistence")
        return

    print("PXE ...............................................NTF(ok)")

check_pxe_boot()
