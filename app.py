#!/usr/bin/env python
# -*- coding: utf-8 -*-

import flask
import config

import static.main.main

import app.view
from app.tag import tag
from app.body import Body

server = flask.Flask(__name__, template_folder = config.path_static)


@server.route("/")
def hello():
	return view('main')

# статика
@server.route("/static/<path:filename>")
def stat(filename):
	return flask.send_from_directory(config.path_static, filename)

# выполнение скриптов
@server.route("/view/<path:path>")
def view(path):
	result = app.view.path(path)
	
	if result == False:
		return flask.abort(404)
	return result
	
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
	
# запуск сервера если запускают этот файд
if __name__ == "__main__":
	server.run(config.host, config.port, True)

	
	
	
	
	
	
	
	