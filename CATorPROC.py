# -*- coding: utf-8 -*-
#!/usr/bin/env python3

import subprocess

def check_proc_fails():
    # Check for any proc_fails errors
    p = subprocess.Popen(["grep", "-r", "PROC_FAIL", "/var/log/"], stdout=subprocess.PIPE)
    output = p.communicate()[0].decode()
    if "PROC_FAIL" in output:
        print("Error: PROC_FAIL(0x65) ex CPU")

def check_caterr():
    # Check for any caterr() errors
    p = subprocess.Popen(["grep", "-r", "CATERR()", "/var/log/"], stdout=subprocess.PIPE)
    output = p.communicate()[0].decode()
    if "CATERR(0xEB)IERR" in output:
        print("Error: CATERR()IERR, ex MB")
    if "CATERR(0xEB)MCERR"
        print("Error: CATERR()MCERR, ex CPU")

check_proc_fails()
check_caterr()
