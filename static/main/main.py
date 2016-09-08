#!/usr/bin/env python
# -*- coding: utf-8 -*-

from app.tag import tag
import geojson
import json
import app.view
import config
from os import listdir
from os.path import isfile, join
import app.view

# def data():
	# path = 'main/world.geo.json-master/countries/USA/'
	# url = config.url_static + path
	# path = config.path_static + path
	# return {
		# 'url': config.url_static + 'main/world.geo.json-master/countries/USA/',
		# 'names': [f for f in listdir(path) if isfile(join(path, f))]
	# }

def index(body):
	
	body.title('GeoJSON + Flask + HTMLTags')
	body.js('js/OpenLayers.js', -2)
	body.css_link('https://unpkg.com/leaflet@0.7.7/dist/leaflet.css', -2)
	body.js_link('https://unpkg.com/leaflet@0.7.7/dist/leaflet.js', -2)
	
	file = open(config.path_static + 'main/us_state.json', 'r') #http://leafletjs.com/examples/us-states.js
	data = file.read()
	file.close()
	body.param('geojson', json.loads(data))
	
	body.content(tag.div(
		tag.div(
			tag.div(
				tag.div(
					tag.div(
						tag.span('no select').attr(Class = 'main-info-text')
					).attr(Class = 'main-info') 
				).attr(Class = 'col-xs-12 col-sm-12')
			).attr(Class = 'row') +
			tag.div(
				tag.div(
					app.view.module('block.ratio', body).index(
						body, tag.div(
							tag.div('').attr(Class = 'main-map', id = 'map')
						).attr(Class = 'main-map-parent'), 16, 9
					)
				).attr(Class = 'col-xs-12 col-sm-12')
			).attr(Class = 'row')
		).attr(Class = 'container')
	).attr(Class = 'main'))
	
	
	return app.view.module('body').index(body)