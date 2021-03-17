import os
import re
import sys
import enum
import time
import atexit
import tarfile
import datetime
import platform
import threading

from colorama import Fore, init, AnsiToWin32


logsDate = datetime.datetime.now()
logsId = 1

screenLock = threading.Semaphore(value=1)

if os.path.exists('./logs'):

	for log in os.listdir('./logs'):

		if '.log' in log:

			with tarfile.open(f'./logs/{log[:-4]}.tar.gz', 'w:gz') as tar:

				tar.add(f'./logs/{log}', arcname=f'{log}')

			os.remove(f'./logs/{log}')


	for file in os.listdir('./logs'):

		day = re.match('^(([0-9]{4}(-[0-9]{2}){2})_[0-9]+(\.[a-zA-Z]+)*)$', file)
		
		if day.group(2) == logsDate.strftime('%Y-%m-%d'):

			logsId += 1

@enum.unique
class LogLevel(enum.Enum):

	ALL = 0
	DEBUG = 1
	INFO = 2
	WARN = 3
	ERROR = 4
	FATAL = 5
	CRITICAL = 6
	GOOD = 7
	TRACE = 8
	CLOSE = 9


"""

#
# @ Log class
#

	- do()
	
"""
class Log():
	

	"""
	
	#
	# @ Static method 'do()'
	#
	
		- loglevel: log level type @ LogLevel
		- log: string to log @ String
		- delay (Optionnal): delay after the log
		- up_spacing (Optionnal): count of space before the log
		- bottom_spacing (Optionnal): count of space after the log
		- file_log (Optionnal): define if this log must be logged into the log file as well

		=> Log a text in the terminal with defined log level (from DEBUG to FATAL)

	"""
	@staticmethod
	def do(loglevel, log, delay=0, up_spacing=0, bottom_spacing=0, file_log=True):

		global screenLock

		if loglevel.value == 1:

			level = Fore.WHITE + '[' + Fore.YELLOW + 'DEBUG' + Fore.WHITE + ']' + Fore.RESET
			levelUncoloured = '[DEBUG]'

		elif loglevel.value == 2:

			level = Fore.WHITE + '[' + "\u001b[34;1m" + "INFO" + Fore.WHITE + ']' + Fore.RESET
			levelUncoloured = '[INFO]'

		elif loglevel.value == 3:

			level = Fore.WHITE + '[' + Fore.YELLOW + "WARN" + Fore.WHITE + ']' + Fore.RESET
			levelUncoloured = '[WARN]'

		elif loglevel.value == 4:

			level = Fore.WHITE + '[' + "\u001b[31;1m" + "ERROR" + Fore.WHITE + ']' + Fore.RESET
			levelUncoloured = '[ERROR]'
		
		elif loglevel.value == 5:

			level = Fore.WHITE + '[' + "\u001b[31m" + "FATAL" + Fore.WHITE + ']' + Fore.RESET
			levelUncoloured = '[FATAL]'

		elif loglevel.value == 6:

			level = Fore.WHITE + '[' + "\u001b[31m" + "CRITICAL" + Fore.WHITE + ']' + Fore.RESET
			levelUncoloured = '[CRITICAL]'
		
		elif loglevel.value == 7:

			level = Fore.WHITE + '[' + Fore.GREEN + "GOOD" + Fore.WHITE + ']' + Fore.RESET
			levelUncoloured = '[GOOD]'

		elif loglevel.value == 8:

			level = Fore.WHITE + '[' + Fore.RED + "TRACE" + Fore.WHITE + ']' + Fore.RESET
			levelUncoloured = '[TRACE]'

		elif loglevel.value == 9:

			level = Fore.WHITE + '[' + "\u001b[31;1m" + "-" + Fore.WHITE + ']' + Fore.RESET
			levelUncoloured = '[-]'
		
		else:

			level = Fore.WHITE + '[' + Fore.YELLOW + "*" + Fore.WHITE + ']' + Fore.RESET
			levelUncoloured = '[*]'

		if delay != 0:
			time.sleep(delay)

		screenLock.acquire()

		if up_spacing > 0:
			for i in range(up_spacing):
				print('')

		if platform.system() == 'Windows':
			
			init(wrap=False)
			encode = AnsiToWin32(sys.stderr).stream

			print(f'{level} {log}', file=encode)

		else:

			print(f'{level} {log}')

		if file_log:

			if not os.path.exists('./logs'):
				os.mkdir('./logs')

			with open(f'./logs/{logsDate.strftime(f"%Y-%m-%d_{logsId}.log")}', 'a+') as f:
				f.write(f'({datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")}) {levelUncoloured} {log}\n')

		if bottom_spacing > 0:
			for i in range(bottom_spacing):
				print('')

		screenLock.release()

#
# @ Framework loading animation when loading modules
#
def LogFramework(framework):

	icon = ['/', '―', '\\', '|']

	k = 0

	for i in range(4):

		for j in range(len(framework)):

			parse = list(framework)

			parse[j] = parse[j].upper()

			parse = "".join(parse)

			sys.stdout.write(f'\r[*] {parse} {icon[k]}')
			sys.stdout.flush()

			k += 1

			if k >= len(icon):

				k = 0

			time.sleep(0.05)

	if platform.system() == "Windows":

		os.system('cls')

	else:

		os.system('clear')