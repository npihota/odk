#!/usr/bin/env python
# -*- coding: utf-8 -*-

from app.tag import tag
import app.body
import app.view

def index(body):
	
	if not isinstance(body, app.body.Body):
		return ''
	
	body.charset('utf-8')
	# body.js_link('https://ajax.googleapis.com/ajax/libs/jquery/3.1.0/jquery.min.js')
	# body.js_link('http://openlayers.org/api/OpenLayers.js')
	
	body.js('js/jquery.min.js', -1000)
	body.js('js/bootstrap-3.3.7-dist/js/bootstrap.min.js', -1000)
	body.css('js/bootstrap-3.3.7-dist/css/bootstrap.min.css', -1000)
	body.css('js/bootstrap-3.3.7-dist/css/bootstrap-theme.min.css', -1000)
	
	body.css('css/reset.css', -100)
	body.css('css/ico.css', -100)
	body.css('css/block.css', -100)
	body.css('body/body.css', -100)
	
	body.meta_name('viewport', 'width=device-width, initial-scale=1')
	
	app.view.module('header', body).index(body)
	app.view.module('footer', body).index(body)
	
	return str(body)