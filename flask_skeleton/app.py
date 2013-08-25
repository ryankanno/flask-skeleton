#!/usr/bin/env python
# -*- coding: utf-8 -*-

from config import DefaultConfig
from extensions import cache
from extensions import mail

from flask_debugtoolbar import DebugToolbarExtension

from flask import Flask
from flask import jsonify
from flask import render_template
from flask import request

import json
import logging
import logging.config
import os


def get_app(config=None):
    """Creates a Flask application"""
    app = Flask(__name__)

    configure_app(app, config)

    configure_blueprints(app)
    configure_extensions(app)
    configure_logging(app)
    configure_error_handlers(app)

    return app


def configure_app(app, config):
    app.config.from_object(DefaultConfig)

    if 'TEMPLATE_DIR' in app.config:
        app.template_folder = app.config['TEMPLATE_DIR']

    if 'STATIC_DIR' in app.config:
        app.static_folder = app.config['STATIC_DIR']

    if config is not None:
        app.config_from_object(config)

    if 'CONFIG_ENVVAR' in app.config:
        app.config.from_envvar(app.config['CONFIG_ENVVAR'])


def configure_blueprints(app):
    blueprints = app.config['BLUEPRINTS'] if 'BLUEPRINTS' in app.config else []
    for blueprint in blueprints:
        app.register_blueprint(blueprint)


def configure_extensions(app):
    mail.init_app(app)
    cache.init_app(app)

    toolbar = DebugToolbarExtension(app)


def configure_error_handlers(app):
    @app.errorhandler(401)
    def unauthorized(error):
        if request.is_xhr:
            return jsonify(error="Unauthorized")
        return render_template("errors/unauthorized.html", error=error), 401

    @app.errorhandler(404)
    def not_found(error):
        if request.is_xhr:
            return jsonify(error="Page not found")
        return render_template("errors/not_found.html", error=error), 404

    @app.errorhandler(500)
    def internal_server_error(error):
        if request.is_xhr:
            return jsonify(error="An error has occurred")
        return render_template("errors/internal_server_error.html", error=error), 500


def configure_logging(app):
    log_ini = os.path.join(app.root_path, app.config['LOG_INI'])

    if os.path.exists(log_ini):
        with open(log_ini, 'rt') as f:
            log_config = json.load(f)
        logging.config.dictConfig(log_config)

# vim: filetype=python
