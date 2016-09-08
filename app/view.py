#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os.path
import config
import importlib
import app.body

def escape(path):
	return path.replace('//', '/').rstrip('/')

def path(path):

	# имя файла
	_, name = os.path.split(path)
	# имя модуля
	module_name = escape(path).replace('/', '.')
	
	mod = module(module_name)
	if mod == False:
		return False
	else:
		return body(mod, escape(path + '/' + name))

def module(pakage, body = None):
	path = (pakage + '.' + pakage.split('.').pop()).replace('.', '/')
	pakage = 'static.' + pakage + '.' + pakage.split('.').pop()
	try:
		module = importlib.import_module(pakage)
		load(path, body)
		return module
	except ImportError:
		path_current = []
		path_end = pakage.split('.')
		path_end.pop()
		for dir_name in path_end:
			path_current.append(dir_name)
			path_current_str = config.path + '/'.join(path_current)
			if not os.path.isdir(path_current_str):
				print('app.static.module path not found', path_current_str)
				return False
			
			if not os.path.isfile(path_current_str + '/__init__.py'):
				open(path_current_str + '/__init__.py', 'w').close()
		try:
			module = importlib.import_module(pakage)
			load(path, body)
			return module
		except ImportError:
			return False
			
def load(path, body = None):
	print(path)
	if body == None:
		return
	
	if os.path.isfile(config.path_static + path + '.css'):
		body.css(path + '.css', -1)
	
	if os.path.isfile(config.path_static + path + '.js'):
		body.js(path + '.js', -1)
	
	
def body(module, path):
	body = app.body.Body()
	if os.path.isfile(config.path_static + path + '.css'):
		body.css(path + '.css', -1)
	
	if os.path.isfile(config.path_static + path + '.js'):
		body.js(path + '.js', -1)
	
	return module.index(body)