import datetime
import traceback
from org.heather.api.tools import Tools


LATENCIES = {}


class LatencyCalculator():


	@staticmethod
	def begin(uid):

		global LATENCIES

		try:

			LATENCIES[uid] = {}
			LATENCIES[uid]['begin'] = datetime.datetime.now()
			LATENCIES[uid]['end'] = None
			LATENCIES[uid]['result'] = {}
			LATENCIES[uid]['result']['begin'] = {}
			LATENCIES[uid]['result']['begin']['unix_timestamp'] = Tools.convert_to_unix(LATENCIES[uid]['begin'])
			LATENCIES[uid]['result']['begin']['utc'] = LATENCIES[uid]['begin'].astimezone().isoformat()
			LATENCIES[uid]['result']['begin']['datetime'] = LATENCIES[uid]['begin'].strftime('%d-%m-%Y - %H:%M:%S')
			LATENCIES[uid]['result']['end'] = {}
			LATENCIES[uid]['result']['end']['unix_timestamp'] = None
			LATENCIES[uid]['result']['end']['utc'] = None
			LATENCIES[uid]['result']['end']['datetime'] = None
			LATENCIES[uid]['result']['latency'] = {}
			LATENCIES[uid]['result']['latency']['ms'] = None
			
			return True

		except:

			return False


	@staticmethod
	def end(uid):

		global LATENCIES

		try:

			LATENCIES[uid]['end'] = datetime.datetime.now()

			LATENCIES[uid]['result']['end'] = {}
			LATENCIES[uid]['result']['end']['unix_timestamp'] = Tools.convert_to_unix(LATENCIES[uid]['end'])
			LATENCIES[uid]['result']['end']['utc'] = LATENCIES[uid]['end'].astimezone().isoformat()
			LATENCIES[uid]['result']['end']['datetime'] = LATENCIES[uid]['end'].strftime('%d-%m-%Y - %H:%M:%S')
			LATENCIES[uid]['result']['latency']['ms'] = (LATENCIES[uid]['end'] - LATENCIES[uid]['begin']).total_seconds() * 1000

			return True

		except:

			return False


	@staticmethod
	def result(uid):

		global LATENCIES

		try:
			result = LATENCIES[uid]['result']

			del LATENCIES[uid]

			return result

		except:

			return None


	@staticmethod
	def get_begin(uid):

		global LATENCIES

		try:

			return LATENCIES[uid]['begin']
		
		except:

			return None 


	@staticmethod
	def get_end(uid):

		global LATENCIES

		try:

			return LATENCIES[uid]['end']
		
		except:

			return None 