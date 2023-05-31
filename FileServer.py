# -*- coding: utf-8 -*-
#!/usr/bin/env python3

import subprocess
import socket

# Install Samba
subprocess.run(['yum', '-y', 'install', 'samba'])

# Enable and start the Samba service
subprocess.run(['systemctl', 'enable', '--now', 'smb'])

# Configure the Samba service
smb_conf = """
[global]
workgroup = WORKGROUP
security = user
map to guest = bad user

[files]
path = /srv/samba
read only = no
guest ok = yes
"""
with open('/etc/samba/smb.conf', 'w') as f:
    f.write(smb_conf)

# Create a directory for the file server
subprocess.run(['mkdir', '/srv/samba'])

# Set permissions for the file server directory
subprocess.run(['chmod', '777', '/srv/samba'])

# Display the IP address for clients to connect
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
print(f"File server running at smb://{ip_address}/files")