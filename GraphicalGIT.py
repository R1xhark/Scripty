#!/usr/bin/env python3

import subprocess
import os
import pysimplegui as sg

# Define Git commands
GIT_COMMANDS = {
    'Clone': 'git clone',
    'Add': 'git add',
    'Commit': 'git commit -m',
    'Push': 'git push',
    'Pull': 'git pull',
    'Status': 'git status',
    'Log': 'git log',
    'Diff': 'git diff'
}

# Define layout for GUI
layout = [
    [sg.Text('Git Command:')],
    [sg.Combo(list(GIT_COMMANDS.keys()), default_value='Clone', key='command')],
    [sg.Text('Repository URL:')],
    [sg.InputText(key='url')],
    [sg.Text('Commit Message (for commit command only):')],
    [sg.InputText(key='message')],
    [sg.Button('Execute'), sg.Cancel()]
]

# Create the GUI window
window = sg.Window('Git Command Runner', layout)

# Run the event loop for the GUI
while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == 'Cancel':
        break

    # Get the selected Git command
    command = GIT_COMMANDS[values['command']]

    # Get the repository URL and commit message
    url = values['url']
    message = values['message']

    # Define the command to be executed
    if values['command'] in ['Clone', 'Pull', 'Status', 'Log', 'Diff']:
        cmd = f"{command} {url}"
    else:
        cmd = f"{command} && {command} {url} && {command} {message}"

    # Run the Git command and show the output
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output = result.stdout.decode() + result.stderr.decode()
    sg.popup_scrolled(output, title='Git Command Output')
    
# Close the GUI window
window.close()
