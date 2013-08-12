#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from flask import render_template

from config import DefaultConfig
from extensions import cache
from extensions import mail


# TODO: Figure out how to set template path, etc
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


def configure_error_handlers(app):
    @app.errorhandler(401)
    def unauthorized(error):
        if request.is_xhr:
            return jsonfiy(error="Unauthorized")
        return render_template("errors/unauthorized.html", error=error), 401

    @app.errorhandler(404)
    def not_found(error):
        if request.is_xhr:
            return jsonfiy(error="Page not found")
        return render_template("errors/not_found.html", error=error), 404

    @app.errorhandler(500)
    def internal_server_error(error):
        if request.is_xhr:
            return jsonfiy(error="An error has occurred")
        return render_template("errors/internal_server_error.html", error=error), 500


def configure_logging(app):
    pass

# vim: filetype=python
