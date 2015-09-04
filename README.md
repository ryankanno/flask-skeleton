# flask-skeleton

This is an opinionated Flask application that I model most of my projects
after.

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
[Ansible-Flask](http://github.com/ryankanno/ansible-flask).  You'll need to
clone that project into a directory of your choice.

To test the skeleton with [Ansible-Flask](http://github.com/ryankanno/ansible-flask),
the Vagrantfile is looking for an environment variable named ANSIBLE_FLASK_PATH
that contains the path to the [Ansible-Flask](http://github.com/ryankanno/ansible-flask) project.

To provision the machines, you'll want to make sure the Vagrantfile contains
the following line:

`ansible.playbook = ENV['ANSIBLE_FLASK_PATH'] + "/provisioning/ansible/site.yml"`

then run the following command:

* `ANSIBLE_FLASK_PATH=/path/to/ansible-flask/on/your/machine vagrant up`

To deploy new changes to the code, you'll want to make sure the Vagrantfile contains
the following line:

`ansible.playbook = ENV['ANSIBLE_FLASK_PATH'] + "/provisioning/ansible/deploy.yml"`

then run the following command:

* `ANSIBLE_FLASK_PATH=/path/to/ansible-flask/on/your/machine vagrant provision`
