#!/usr/bin/env python
# -*- coding: utf-8 -*-

from app.tag import tag

def index(body):
	body.content(
		tag.header(
			tag.div(
				tag.div(
					tag.div(
						tag.div(
							tag.h1('Print GEOJson to map')
						).attr(Class = 'header-content')
					).attr(Class = 'col-xs-12 col-sm-12')
				).attr(Class = 'row')
			).attr(Class = 'container')
		).attr(Class = 'header')
	, -1000)