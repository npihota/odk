#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os.path

activate_this = os.path.dirname(os.path.realpath(__file__))
execfile(activate_this, dict(__file__ = activate_this))

from odk import add as application