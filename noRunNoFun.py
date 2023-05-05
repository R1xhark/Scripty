#!/usr/bin/env python3

import os

# pokud ma soubor koncovku .py nebo .sh nastav prava aby byly scripty spustitelne pouze rootem
for filename in os.listdir():
    if filename.endswith('.py'|'.sh'):
        os.chmod(filename, 0o700)
