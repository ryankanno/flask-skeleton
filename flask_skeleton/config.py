#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from apps.www import www

class DefaultConfig(object):
    DEBUG        = True
    PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
    PROJECT_NAME = "flask_skeleton"
    SECRET_KEY   = "please_change_me"

    TEMPLATE_DIR = os.path.join(PROJECT_ROOT, 'apps', 'templates')
    STATIC_DIR   = os.path.join(PROJECT_ROOT, 'apps', 'static')

    BLUEPRINTS   = (www,)

# vim: filetype=python
