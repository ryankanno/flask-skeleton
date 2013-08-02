#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from flask import render_template

from config import Config
from apps.www import www


DEFAULT_BLUEPRINTS = (
    www,
)

def get_app(name=None, config=Config, blueprints=DEFAULT_BLUEPRINTS):
    """Creates a Flask application"""
    name = name or "foo"

    app = create_app(name, config)
    configure_app(app, config, blueprints)
    return app


def create_app(name=None, config=Config):
    template_folder = config.TEMPLATE_DIR
    static_folder = config.STATIC_DIR
    return Flask(name, 
        template_folder=template_folder, 
        static_folder=static_folder)


def configure_app(app, config, blueprints):
    app.config.from_object(config)
    configure_blueprints(app, blueprints)
    configure_error_handlers(app)


def configure_blueprints(app, blueprints):
    for blueprint in blueprints:
        app.register_blueprint(blueprint)


def configure_error_handlers(app):
    @app.errorhandler(401)
    def unauthorized(error):
        return render_template("errors/unauthorized.html"), 401

    @app.errorhandler(404)
    def not_found(error):
        return render_template("errors/not_found.html"), 404

    @app.errorhandler(500)
    def internal_server_error(error):
        return render_template("errors/internal_server_error.html"), 500

# vim: filetype=python
