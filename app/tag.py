#!/usr/bin/env python
# -*- coding: utf-8 -*-

import text
import sys

def teg_clear(tag):
	return str(tag).replace('_', '-').lower().strip()

class Node: 
	pass
	def __init__(self, name, text = None, escape = True):
		self._name = teg_clear(name)
		self._text = text
		self._escape = escape
		self._attrs = {}
	
	def text(self, _text):
		self._text = _text
		return self
		
	def attr(self, *args, **argsw):
		for attr in args:
			self._attrs[teg_clear(attr)] = True
		
		for attr in argsw:
			value = argsw[attr]
			attr = teg_clear(attr)
			if value == False or value == None:
				if attr in self._attrs:
					del self._attrs[attr]
			else:
				self._attrs[attr] = value
		return self
	
	def __str__(self):
		params = [];
		for attr in self._attrs:
			if self._attrs[attr] == True:
				params.append(teg_clear(attr))
			else:
				params.append(teg_clear(attr) + '="' + text.html_encode(self._attrs[attr]) + '"')
		
		_text = self._text
		if isinstance(_text, (Node, Tag)):
			_text = str(_text)
		elif self._escape == True:
			pass
			#_text = text.html_encode(self._text)
		
		data = {
			'params': ' '.join(params),
			'name': self._name,
			'text': _text
		}
		if self._name == '--':
			return '<!--%(text)s-->' % data
		elif self._name == 'doctype':
			return '<!doctype %(params)s>' % data
		elif self._text == None and len(params) == 0:
			return '<%(name)s/>' % data
		elif self._text == None:
			return '<%(name)s %(params)s/>' % data
		elif len(params) == 0:
			return '<%(name)s>%(text)s</%(name)s>' % data
		else:
			return '<%(name)s %(params)s>%(text)s</%(name)s>' % data
		
	def __add__(self, other):
		new_tag = Tag()
		new_tag.append(self)
		new_tag.append(other)
		return new_tag
		
	def __radd__(self, other):
		new_tag = Tag()
		new_tag.append(other)
		new_tag.append(self)
		return new_tag

class Tag: 
	pass
	def __init__(self):
		self.childs = [];
		
	def append(self, node):
		if isinstance(node, Tag):
			for child_node in node.childs:
				self.append(child_node)
		elif isinstance(node, (list, tuple)):
			for child_node in node:
				self.append(child_node)
		elif isinstance(node, dict):
			for key in node:
				self.append(node[key])
		else: 
			self.childs.append(node)
		return self
		
	def __add__(self, other):
		new_tag = Tag();
		new_tag.append(self)
		new_tag.append(other)
		return new_tag;
		
	def __radd__(self, other):
		new_tag = Tag();
		new_tag.append(other)
		new_tag.append(self)
		return new_tag;
		
	def __str__(self):
		strs = [];
		for child in self.childs:
			c = child
			c = str(child)
			if not isinstance(child, (Node, Tag)):
				c = text.html_encode(c)
			strs.append(c)
		return ''.join(strs)
		
	def text(self, text):
		for child in self.childs:
			child.text(text)
		return self
			
	def attr(self, *args, **argsw):
		for child in self.childs:
			child.attr(*args, **argsw)
		return self
			
		

class Get:
	def __getattr__(self, __name__):
		n = {'name': __name__}
		def get(text = None, escape = True):
			node = Node(n['name'], text, escape)
			return node
		return get

tag = Get()








