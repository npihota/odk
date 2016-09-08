import os

host = '127.0.0.1'
port = 80
protocol = 'http'


if protocol == 'http' and port == 80:
	url = protocol + '://' + host + '/'
	
elif protocol == 'https' and port == 443:
	url = protocol + '://' + host + '/'
	
else:
	url = protocol + '://' + host + ':' + str(port) + '/'
	

path = os.path.dirname(os.path.realpath(__file__)) + '/'
path_static = path + 'static/'

url = url
url_static = url + 'static/'
url_view = url + 'view/'


if os.path.isfile(path + '.config.py'):
	file = open(path + '.config.py', 'r')
	code = file.read()
	file.close()
	exec(code)