import os
import pathlib
import argparse

from org.heather.setup import Setup
from org.heather.api.log import Log, LogLevel


# Argument Prser
parser = argparse.ArgumentParser()
parser.add_argument('-setup', help='Start the JHeather setup wizard.', action="store_true")
parser.add_argument('-fullreset', help='To do', action="store_true")
parser.add_argument('-resetconfig', '-rc', help='To do', action="store_true")
parser.add_argument('-nocolor', help='To do', action="store_true")
parser.add_argument('-force', help='To do', action="store_true")
parser.add_argument('-restore', help='To do', action="store_true")
parser.add_argument('-debug', help='To do', action="store_true")
args = parser.parse_args()


# Startup process
is_setup = Setup.is_config_valid(os.path.dirname(__file__))
Log.do(LogLevel.WARN, "test")

# Start main setup wizard
if not is_setup:

    Setup.wizard()

# Process to main integrity verification
else:

    print('dat')