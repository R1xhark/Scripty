#!/usr/bin/env python3

import subprocess
import sys

# Check CPU info
def check_cpu_info():
    print("CPU Info:")
    cmd = "lscpu"
    subprocess.run(cmd.split())

# Check memory usage
def check_memory_usage():
    print("\nMemory Usage:")
    cmd = "free -h"
    subprocess.run(cmd.split())

# Check disk usage
def check_disk_usage():
    print("\nDisk Usage:")
    cmd = "df -h"
    subprocess.run(cmd.split())

# Check system temperature
def check_system_temperature():
    print("\nSystem Temperature:")
    cmd = "sensors"
    subprocess.run(cmd.split())

# Check hardware sensors
def check_hardware_sensors():
    print("\nHardware Sensors:")
    cmd = "sensors-detect --auto"
    subprocess.run(cmd.split())
    cmd = "sensors"
    subprocess.run(cmd.split())

if __name__ == "__main__":
    check_cpu_info()
    check_memory_usage()
    check_disk_usage()
    check_system_temperature()
    check_hardware_sensors()
