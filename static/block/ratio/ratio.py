#!/usr/bin/env python
# -*- coding: utf-8 -*-

from app.tag import tag
import app.view

def index(body, content = None, w = 1, h = 1):
	w = float(w)
	h = float(h)
	
	a_prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
	
	while True:
		n = False
		
		for i_prime in a_prime:
			if w % i_prime == w % i_prime == 0:
				w /= i_prime
				h /= i_prime
				n = True
				break
				
		if n == False:
			break
		
	f_percent = (h / w) * 100
	
	print()
	
	return tag.div(
		tag.div('').attr(Class = 'block-ratio-before', style = 'padding-top:' + str(f_percent) + '%') +
		tag.div(content).attr(Class = 'block-ratio-content')
	).attr(Class = 'block-ratio block-ratio-' + str(w) + 'x' + str(h))
	