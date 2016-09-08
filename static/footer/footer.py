#!/usr/bin/env python
# -*- coding: utf-8 -*-

from app.tag import tag

def index(body):
	body.content(
		tag.footer(
			tag.div(
				tag.div(
					tag.div(
						tag.div(
							'©2016 All rights reserved'
						).attr(Class = 'footer-content')
					).attr(Class = 'col-xs-12 col-sm-12')
				).attr(Class = 'row')
			).attr(Class = 'container')
		).attr(Class = 'footer')
	, 1000)