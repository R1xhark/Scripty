# -*- coding: utf-8 -*-
#!/usr/bin/env python3

import socket
import netifaces

# Install vsftpd package
subprocess.run(['sudo', 'yum', '-y', 'install', 'vsftpd'])

# Backup the original vsftpd.conf file
subprocess.run(['sudo', 'cp', '/etc/vsftpd/vsftpd.conf', '/etc/vsftpd/vsftpd.conf.orig'])

# Configure vsftpd to allow anonymous login
with open('/etc/vsftpd/vsftpd.conf', 'a') as f:
    f.write('anonymous_enable=YES\n')
    f.write('anon_root=/var/ftp/pub\n')
    f.write('anon_upload_enable=YES\n')
    f.write('anon_mkdir_write_enable=YES\n')
    f.write('local_enable=NO\n')
    f.write('write_enable=NO\n')

# Restart vsftpd service
subprocess.run(['sudo', 'systemctl', 'restart', 'vsftpd'])

# Get the IP address for connecting
def get_ip():
    interfaces = netifaces.interfaces()
    for interface in interfaces:
        addrs = netifaces.ifaddresses(interface)
        if socket.AF_INET in addrs:
            ip = addrs[socket.AF_INET][0]['addr']
            if not ip.startswith('127.'):
                return ip

ip = get_ip()
if ip:
    print(f'FTP server is running on {ip}. Connect using "ftp://{ip}"')
else:
    print('Failed to get IP address')
