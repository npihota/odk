#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import logging
logging.basicConfig(stream = sys.stderr)
sys.path.insert(0, os.path.split(__file__)[0] + '/')

from odk import app as application
