#!/usr/bin/env python3

import pysmart

# Get a list of all connected drives
drives = pysmart.disks()

# Iterate over each drive and check for errors
for drive in drives:
    # Check if the drive supports SMART
    if not drive.supports_smart:
        print(f"{drive.name} does not support SMART")
        continue

    # Check the overall health of the drive
    if drive.health_status == "OK":
        print(f"{drive.name} is healthy")
    else:
        print(f"{drive.name} is reporting a health status of {drive.health_status}")

    # Check the drive's error log
    error_log = drive.error_log()
    if error_log:
        print(f"{drive.name} has {len(error_log)} errors in its error log:")
        for error in error_log:
            print(f"- {error}")
    else:
        print(f"{drive.name} has no errors in its error log")