import yaml
import logging
import signal
logging.basicConfig(level=logging.WARNING, format ='%(asctime)s %(message)s')
logger = logging.getLogger()
def sign(sig, frame):
	def read_config(filename, key_list):
		file_read = open (filename, 'r')
		for x in yaml.load_all(file_read, Loader=yaml.FullLoader):
			cfg = x
			logging.debug(x)
			return True, cfg
	status, result= read_config('file_yaml.yaml', ['first-name', 'middle-name', 'last-name'])
	if not status:
		print(result)
	cfg = result
	logging.warning('your name is ' + cfg['first-name'] + ' ' + cfg['middle-name']  + ' ' + cfg['last-name'])
	signal.alarm(10)
signal.signal(signal.SIGALRM, sign)
signal.alarm(10)
def sign_info(sig, frame):
        logger.setLevel(logging.INFO)
signal.signal(signal.SIGIOT, sign_info)
def sign_debug(sig, frame):
        logger.setLevel(logging.DEBUG)
signal.signal(signal.SIGBUS, sign_debug)
while True:
	pass
