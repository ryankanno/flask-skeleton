Flask-Skeleton
==============

This is an opinionated Flask application that I model most of my projects
after.  **This project is no longer being maintained. (see below)**

## 2015-09-03

I’ve redone flask-skeleton as a Cookiecutter @ https://github.com/ryankanno/cookiecutter-flask. This repo will no longer be maintained.

## Dependencies

* [Bower](http://bower.io)

## Libraries used

* Flask
* Flask-Bcrypt
* Flask-Cache
* Flask-DebugToolBar
* Flask-Mail
* Flask-SeaSurf
* Flask-Script
* [Bootstrap 3](http://getbootstrap.com)

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

The skeleton has been integrated with
[ansible-nginx-uwsgi-supervisor-deployer](http://github.com/ryankanno/ansible-nginx-uwsgi-supervisor-deployer).  
To test out the installation in Vagrant, you'll ideally want to clone the following projects into the same parent directory:

* [ansible-nginx-uwsgi-supervisor-deployer](http://github.com/ryankanno/ansible-nginx-uwsgi-supervisor-deployer)
* [ansible-nginx-uwsgi-supervisor](http://github.com/ryankanno/ansible-nginx-uwsgi-supervisor)
* [ansible-roles](http://github.com/ryankanno/ansible-roles)

After checking those three projects out, you'll need to do two things:

* Create an ansible.cfg ([example](http://github.com/ryankanno/flask-skeleton/tree/master/ansible.cfg.example)) with the roles_path pointed to the parent directory from above
* `export NGINX_UWSGI_SUPERVISOR_DEPLOYER_PATH=<path_to_where_you_checked_out_ansible-nginx-uwsgi-supervisor-deployer>`


To provision the machines, you'll want to make sure the Vagrantfile contains
the following line:

`ansible.playbook = ENV['NGINX_UWSGI_SUPERVISOR_DEPLOYER_PATH'] + "/provisioning/ansible/site.yml"`

then run the following command:

* `vagrant up`

To deploy new changes to flask-skeleton, you'll want to run the following command:

* `vagrant provision`
