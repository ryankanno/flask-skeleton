#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

class Config(object):
    DEBUG = True
    PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
    PROJECT_NAME = "flask_skeleton"

    TEMPLATE_DIR = os.path.join(PROJECT_ROOT, 'apps', 'templates')
    STATIC_DIR   = os.path.join(PROJECT_ROOT, 'apps', 'static')

# vim: filetype=python
