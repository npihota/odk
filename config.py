import os

host = '127.0.0.1'
port = 80
protocol = 'http'

path = path_static = None
url = url_static = url_view = None

def init():
	global protocol
	global host
	global port
	global path
	global path_static
	global url
	global url_static
	global url_view
	
	if protocol == 'http' and port == 80:
		url = protocol + '://' + host + '/'
		
	elif protocol == 'https' and port == 443:
		url = protocol + '://' + host + '/'
		
	else:
		url = protocol + '://' + host + ':' + str(port) + '/'
		

	path = os.path.split(__file__)[0] + '/'
	path_static = path + 'static/'

	url = url
	url_static = url + 'static/'
	url_view = url + 'view/'

init()

if os.path.isfile(path + '.config.py'):
	file = open(path + '.config.py', 'r')
	code = file.read()
	file.close()
	exec(code)
	init()

	