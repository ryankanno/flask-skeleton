#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from flask import render_template

from config import DefaultConfig

def get_app(config=None):
    """Creates a Flask application"""
    config = config or DefaultConfig
    app = create_app(config)

    configure_app(app, config)
    configure_blueprints(app, config)
    configure_logging(app,config)
    configure_error_handlers(app,config)

    return app


def create_app(config):
    return Flask(config.PROJECT_NAME, 
        template_folder=config.TEMPLATE_DIR, 
        static_folder=config.STATIC_DIR)


def configure_app(app, config):
    app.config.from_object(config)


def configure_blueprints(app, config):
    for blueprint in config.BLUEPRINTS:
        app.register_blueprint(blueprint)


def configure_logging(app, config):
    pass


def configure_error_handlers(app, config):
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
