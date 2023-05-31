# -*- coding: utf-8 -*-
#!/usr/bin/env python3

import subprocess
import time
import os
import sys
import signal
import psutil
import pyshark
import pysimplegui as sg

# Define colors for alerts
COLOR_RED = '#FF0000'
COLOR_YELLOW = '#FFFF00'

# Define alert thresholds
CPU_THRESHOLD = 80
LOGIN_THRESHOLD = 5

# Define system commands
SYSSTAT_COMMAND = 'sar -P ALL 1 1'
LOGWATCH_COMMAND = 'logwatch --detail High'
TRIPWIRE_COMMAND = 'tripwire --check'
NMAP_COMMAND = 'nmap -sS -sV --version-all -T4 -p- localhost'

# Start subprocesses to monitor system performance and generate reports
sysstat_process = subprocess.Popen(SYSSTAT_COMMAND.split(), stdout=subprocess.PIPE)
logwatch_process = subprocess.Popen(LOGWATCH_COMMAND.split(), stdout=subprocess.PIPE)

# Define function to parse Sysstat output
def parse_sysstat_output(output):
    cpu_usage = []
    for line in output.decode().split('\n'):
        if line.startswith('Average:'):
            cpu_usage = [int(x) for x in line.split()[2:]]
    return cpu_usage

# Define function to parse Logwatch output
def parse_logwatch_output(output):
    login_attempts = 0
    for line in output.decode().split('\n'):
        if line.startswith(' Failed logins from:'):
            login_attempts = int(line.split()[-1])
    return login_attempts

# Define function to parse Tripwire output
def parse_tripwire_output(output):
    file_changes = []
    for line in output.decode().split('\n'):
        if line.startswith('+'):
            file_changes.append(line.strip())
    return file_changes

# Define function to parse Nmap output
def parse_nmap_output(output):
    open_ports = []
    for line in output.decode().split('\n'):
        if 'open' in line:
            open_ports.append(line.strip())
    return open_ports

# Define function to update alerts
def update_alerts():
    # Check CPU usage
    cpu_usage = parse_sysstat_output(sysstat_process.stdout.read())
    for i, usage in enumerate(cpu_usage):
        if usage > CPU_THRESHOLD:
            cpu_alerts[i].update(text=f'CPU{i} usage: {usage}%', background_color=COLOR_RED)
        else:
            cpu_alerts[i].update(text=f'CPU{i} usage: {usage}%')

    # Check login attempts
    login_attempts = parse_logwatch_output(logwatch_process.stdout.read())
    if login_attempts > LOGIN_THRESHOLD:
        login_alert.update(text=f'Failed login attempts: {login_attempts}', background_color=COLOR_RED)
    else:
        login_alert.update(text=f'Failed login attempts: {login_attempts}')

    # Check file system changes
    file_changes = parse_tripwire_output(subprocess.run(TRIPWIRE_COMMAND.split(), stdout=subprocess.PIPE))
    if file_changes:
        file_alert.update(text='\n'.join(file_changes), background_color=COLOR_YELLOW)
    else:
        file_alert.update(text='No file system changes detected')

    # Check open ports
    open_ports = parse_nmap_output(subprocess.run(NMAP_COMMAND.split(), stdout=subprocess.PIPE))
    if open_ports:
        port_alert.update(text='\n'.join(open_ports), background_color=COLOR_YELLOW)
    else:
        port_alert.update(text='No open ports detected')

import pysimplegui as sg

# Define GUI layout
layout = [
    [sg.Text('System Performance', font=('Helvetica', 18))],
    [sg.Text('')],
    [sg.Text('CPU Usage', font=('Helvetica', 14))],
    [sg.Text('CPU0: '), sg.Text('', key='cpu0')],
    [sg.Text('CPU1: '), sg.Text('', key='cpu1')],
    [sg.Text('CPU2: '), sg.Text('', key='cpu2')],
    [sg.Text('CPU3: '), sg.Text('', key='cpu3')],
    [sg.Text('')],
    [sg.Text('Login Attempts', font=('Helvetica', 14))],
    [sg.Text(''), sg.Text('', key='login_attempts')],
    [sg.Text('')],
    [sg.Text('File System Changes', font=('Helvetica', 14))],
    [sg.Multiline('', key='file_changes', size=(60, 10), font=('Helvetica', 10))],
    [sg.Text('')],
    [sg.Text('Open Ports', font=('Helvetica', 14))],
    [sg.Multiline('', key='open_ports', size=(60, 10), font=('Helvetica', 10))],
]

window = sg.Window('Server Monitor', layout)

while True:
    event, values = window.Read(timeout=1000)

    if event is None:
        break

    # Check CPU usage
    cpu_usage = parse_sysstat_output(sysstat_process.stdout.read())
    for i, usage in enumerate(cpu_usage):
        window.Element(f'cpu{i}').Update(f'{usage}%')

    # Check login attempts
    login_attempts = parse_logwatch_output(logwatch_process.stdout.read())
    window.Element('login_attempts').Update(f'Failed login attempts: {login_attempts}')

    # Check file system changes
    file_changes = parse_tripwire_output(subprocess.run(TRIPWIRE_COMMAND.split(), stdout=subprocess.PIPE))
    if file_changes:
        window.Element('file_changes').Update('\n'.join(file_changes))
    else:
        window.Element('file_changes').Update('No file system changes detected')

    # Check open ports
    open_ports = parse_nmap_output(subprocess.run(NMAP_COMMAND.split(), stdout=subprocess.PIPE))
    if open_ports:
        window.Element('open_ports').Update('\n'.join(open_ports))
    else:
        window.Element('open_ports').Update('No open ports detected')

window.Close()
