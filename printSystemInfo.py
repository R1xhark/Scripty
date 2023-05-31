# -*- coding: utf-8 -*-

import subprocess

# Run the systeminfo command
systeminfo_process = subprocess.Popen(['systeminfo'], stdout=subprocess.PIPE, universal_newlines=True)
output, error = systeminfo_process.communicate()

# Print the output
print(output)