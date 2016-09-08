#!/usr/bin/env python
# -*- coding: utf-8 -*-

import config
from app.tag import tag
from pprint import pprint

def index(body):
	strs = []
	for attr in dir(config):
		strs.append("obj.%s = %s" % (attr, getattr(config, attr)))
	return '\n'.join(strs)
