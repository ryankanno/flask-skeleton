#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask.ext.script import Manager
from flask_skeleton.app import get_app

app = get_app("foo")
manager = Manager(app)


if __name__ == "__main__":
    manager.run()

# vim: filetype=python
