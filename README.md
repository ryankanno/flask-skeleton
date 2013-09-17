# Flask-skeleton

This is an opinionated Flask application I model most of my projects after.

## Dependencies

* [Bower](http://bower.io)

## Libraries

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
