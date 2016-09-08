#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json 
import sys
import config
import time
import datetime
from app.tag import tag, Tag, Node

class Body:
	pass
	
	class Generate:
		pass
		
		def __init__(self):
			self._id = 999999
			self.prioritet = {
				'charset': -100,
				'ga': -99,
				'ya': -98,
				'title': -97,
				'keywords': -96,
				'description': -95,
				'image': -94,
				'favicon': -93,
				'css': 100,
			}
			
		def __getattr__(self, name):
			if name == 'id':
				self._id += 1
				return str(self._id)
			else:
				raise AttributeError
	
	def __init__(self):
		self.data = {
			'head': {},
			'css': {},
			'js': {},
			'content': {},
		}
		self.generate = Body.Generate()
		self._params = {}

	def head(self, node, id = None, priority = 0):
		if id is None:
			id = self.generate.id
		else:
			id = str(id)
			
		self.data['head'][id] = {
			'node': node, 
			'priority': priority,
			'id': self.generate.id,
		}

	def meta_name(self, name, content, priority = 0):
		self.head(tag.meta().attr(name = name, content = content), 'name_' + name, priority)
		
	def meta_property(self, property, content, priority = 0):
		self.head(tag.meta().attr(property = property, content = content), 'property_' + property, priority)
		
	def charset(self, charset):
		self.head(tag.meta().attr(charset = 'utf-8'), 'charset', self.generate.prioritet['charset'])

	def title(self, title):
		self.head(tag.title(title), 'title', self.generate.prioritet['title'])
		self.meta_name('title', title, self.generate.prioritet['title'])
		self.meta_name('twitter:title', title, self.generate.prioritet['title'])
		self.meta_property('og:title', title, self.generate.prioritet['title'])
		
	def keywords(self, keywords):
		if type(keywords) in (list, dict, tuple):
			keywords = ', '.join([word for word in keywords])
			
		self.meta_name('keywords', keywords, self.generate.prioritet['keywords'])
		self.meta_property('og:keywords', keywords, self.generate.prioritet['keywords'])
		
	def description(self, description):
		self.meta_name('description', description, self.generate.prioritet['description'])
		self.meta_property('og:description', description, self.generate.prioritet['description'])
		
	def image(self, src):
		self.meta_property('og:image', src, self.generate.prioritet['image'])
		self.meta_property('twitter:image:src', src, self.generate.prioritet['image'])

	def favicon(self, src):
		self.head(tag.link().attr(rel = 'shortcut icon', type = 'image/x-icon'), 'favicon', self.generate.prioritet['favicon'])

	def ga(self, key):
		'''
		Google Analitics
		'''
		code = (
			'(function(i,s,o,g,r,a,m){i[\'GoogleAnalyticsObject\']=r;i[r]=i[r]||function(){'
			'(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),'
			'm=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)'
			'})(window,document,\'script\',\'//www.google-analytics.com/analytics.js\',\'ga\');'
			'ga(\'create\', ' + json.dumps(key) + ', \'auto\');'
			'ga(\'send\', \'pageview\');' 
		)
		t = tag.script(code, escape = False).attr(type = 'text/javascript')
		self.head(t, 'ga', self.generate.prioritet['ga'])


	def ya(self, key):
		'''
		Yandex Metrika
		'''
		code = (
			'(function(d,w,c){(w[c]=w[c]||[]).push(function(){try{' 
			'w.yaCounter' + json.dumps(key) + '=new Ya.Metrika({ id:' + json.dumps(key) +
			',clickmap:true,trackLinks:true,accurateTrackBounce:true,webvisor:true});}catch(e){}}' 
			');var n=d.getElementsByTagName("script")[0],s=d.createElement("script"),f=function()' 
			'{n.parentNode.insertBefore(s,n);};s.type="text/javascript";s.async=true;s.src="https' 
			'://mc.yandex.ru/metrika/watch.js";if(w.opera=="[object Opera]"){d.addEventListener("' 
			'DOMContentLoaded",f,false);}else{f();}})(document,window,"yandex_metrika_callbacks");'
		)
		t = (
			tag.script(code, escape = False).attr(type = 'text/javascript') +
			tag.noscript(
				tag.div(
					tag.img().attr(
						src = 'https://mc.yandex.ru/watch/' + str(key), 
						style = 'position:absolute; left:-9999px;'
					)
				)
			)
		)
		self.head(t, 'ya', self.generate.prioritet['ya'])

	def css(self, path, priority = 0):
		self.css_link(config.url_static + path, priority)
		
	def css_link(self, href, priority = 0):
		self.data['css'][href] = {
			'node': tag.link().attr(type = 'text/css', rel = 'stylesheet', href = href), 
			'priority': priority,
			'id': self.generate.id,
		}

	def js(self, path, priority = 0):
		self.js_link(config.url_static + path, priority)
		
	def js_link(self, src, priority = 0):
		self.data['js'][src] = {
			'node': tag.script('').attr(type = 'text/javascript', src = src), 
			'priority': priority,
			'id': self.generate.id,
		}
		
	def content(self, node, priority = 0):
		self.data['content'][self.generate.id] = {
			'node': node, 
			'priority': priority,
			'id': self.generate.id,
		}
	
	def param(self, name, value):
		self._params[name] = value
		
	
	def get(self, index):
		tags = Tag()
		result = [self.data[index][key] for key in self.data[index]]
		result.sort(key = lambda item: (item['priority'], item['id']))
		for item in result:
			tags.append(item['node'])
		return tags
		
	def __str__(self):
		
		head = self.get('head')
		css = self.get('css')
		js = self.get('js')
		content = self.get('content')
		
		params_code = '$_PARAMS=' + json.dumps(self._params)
		
		
		return str(
			tag.doctype().attr('html') +
			tag.html(
				tag.head(head + css) +
				tag.body(
					tag.div(content).attr(Class = "body-content")
				)+
				tag.script(params_code, escape = False).attr(type = 'text/javascript') +
				js
			) +
			(
				tag.__(
					'\n'
					'\tAuthor: uginroot@gmail.com\n'
					'\tGenerateDate: ' + str(datetime.datetime.now()) + '\n'
					'\tVersion: ' + str(sys.version) + '\n'
				)
			)
		)








