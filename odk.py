#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os.path
import sys

# Добавляем путь до текущей дериктории, для поиска модулей в ней (нужно для wsgi)
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))

import flask
import config
from app import view as app_view

# Запуск сервера Flask
app = flask.Flask(__name__, template_folder = config.path_static)

# Главная
@app.route("/")
def hello():
	return view('main')

# статика
@app.route("/static/<path:filename>")
def stat(filename):
	return flask.send_from_directory(config.path_static, filename)

# представления
@app.route("/view/<path:path>")
def view(path):
	result = app_view.path(path)
	
	if result == False:
		return flask.abort(404)
	return result

# Ошибка 404
@app.errorhandler(404)
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
	global app
	app.run(config.host, config.port, True)
	

# запуск сервера если запускают этот файд
if __name__ == "__main__":
	run()

	
	
	
	
	
	
	
	