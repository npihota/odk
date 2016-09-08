#!/usr/bin/env python
# -*- coding: utf-8 -*-

def code(text, list, encode = True):
	'''
	Замена всех вхождений в строке text 
	из кортежа list[n][0] на list[n][1],
	или наоборот если encode == False
	'''
	text = str(text)
	first, second =  (0,1) if encode else (1,0)
	for item in list:
		text = text.replace(item[first], item[second])
	return text
	
'''
Набор символов для замены в html
'''
html_encode_chars = (
	#('&', '&#38;'),
	('"', '&#34;'),
	("'", '&#39;'),
	('<', '&#60;'),
	('>', '&#62;'),
)

def html_encode(text):
	global html_encode_chars
	return code(text, html_encode_chars, True)
	
def html_decode(text):
	global html_encode_chars
	return code(text, html_encode_chars, False)

	
'''
Набор символов для замены в get параметрах url 
'''
url_encode_chars = (
	('%', '%25'), 
	(' ', '%20'),
	('!', '%21'), 
	('*', '%2A'), 
	("'", '%27'), 
	('(', '%28'), 
	(')', '%29'), 
	(';', '%3B'), 
	(':', '%3A'), 
	('@', '%40'), 
	('&', '%26'), 
	('=', '%3D'), 
	('+', '%2B'), 
	('$', '%24'), 
	(',', '%2C'), 
	('/', '%2F'), 
	('?', '%3F'), 
	('#', '%23'), 
	('[', '%5B'), 
	(']', '%5D'), 
)
def url_encode(data):
	global url_encode_chars
	return code(text, url_encode_chars, True)
	
def url_decode(data):
	global url_encode_chars
	return code(text, url_encode_chars, False)