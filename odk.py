#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os.path
import sys

# Добавляем путь до текущей дериктории, для поиска модулей в ней (нужно для wsgi)
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))

import flask
import config
import app.view

# Запуск сервера Flask
server = flask.Flask(__name__, template_folder = config.path_static)

# Главная
@server.route("/")
def hello():
	return view('main')

# статика
@server.route("/static/<path:filename>")
def stat(filename):
	return flask.send_from_directory(config.path_static, filename)

# представления
@server.route("/view/<path:path>")
def view(path):
	result = app.view.path(path)
	
	if result == False:
		return flask.abort(404)
	return result

# Ошибка 404
@server.errorhandler(404)
def page_not_found(e, message = None, text = None):
	data= {
		'url' : config.url,
		'code' : 404,
		'message': message,
		'text': text,
	}
	result = flask.render_template('error/code.html', **data)
	return result, 404
	
def run():
	global server
	server.run(config.host, config.port, True)
	

# запуск сервера если запускают этот файд
if __name__ == "__main__":
	run()

	
	
	
	
	
	
	
	