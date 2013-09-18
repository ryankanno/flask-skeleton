# flask-skeleton

Here be dragons.

This is an opinionated Flask application I model most of my projects after.

It's stable, but always in a state of flux. :D

## Dependencies

* [Bower](http://bower.io)

## Libraries used

* Flask
* Flask-Bcrypt
* Flask-Cache
* Flask-DebugToolBar
* Flask-Mail
* Flask-Restful
* Flask-SeaSurf
* Flask-Script
* [Bootstrap 3](http://getbootstrap)

## Install

* `pip install -r requirements.txt`
* Create log file `etc/logging.ini.json` (use etc/logging.ini.json.example as a template)
* `python manage.py runserver`

### Docker

To test the skeleton w/ Docker, build the image with the included Dockerfile,
then run the following command.

* `sudo docker build -t "YOUR_IMAGE_NAME" .`
* `sudo docker run YOUR_IMAGE_NAME runserver -t 0.0.0.0`

#### Example

* `sudo docker build -t ryankanno/flask_skeleton .`
* `sudo docker run ryankanno/flask_skeleton runserver -t 0.0.0.0`

### Vagrant

WIP
