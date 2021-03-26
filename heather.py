import os
import pathlib
import argparse

from org.heather.setup import Setup
from org.heather.api.log import Log, LogLevel


# Argument Parser
parser = argparse.ArgumentParser()
parser.add_argument('-setup', help='Start the JHeather setup wizard.', action="store_true")
parser.add_argument('-fullreset', help='To do', action="store_true")
parser.add_argument('-resetconfig', '-rc', help='To do', action="store_true")
parser.add_argument('-nocolor', help='To do', action="store_true")
parser.add_argument('-force', help='To do', action="store_true")
parser.add_argument('-restore', help='To do', action="store_true")
parser.add_argument('-debug', help='To do', action="store_true")
args = parser.parse_args()

Log.do(LogLevel.ALL, 'Heather Project (C) 2021 - dev-1.0.0')

# Startup process
is_setup = Setup.is_config_valid(os.path.dirname(__file__))


# Start main setup wizard
if not is_setup or args.setup:

    Setup.wizard(os.path.dirname(__file__))

# Process to main integrity verification
else:

    print('dat')
