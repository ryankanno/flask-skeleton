# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.require_version ">= 1.7.2"

Vagrant.configure(2) do |config|

  config.ssh.insert_key = true

  config.vm.box = "ubuntu/trusty64"
  config.vm.box_check_update = false
  config.vm.define "flaskskeleton_vm"

  config.vm.hostname = 'flaskskeleton.local'
  config.vm.network "private_network", ip: "192.168.58.58"
  config.vm.network "forwarded_port", guest: 80, host: 50058, auto_correct: true

  config.vm.provision :ansible do |ansible|
    ansible.playbook = ENV['NGINX_UWSGI_SUPERVISOR_DEPLOYER_PATH'] + "/provisioning/ansible/site.yml"
    ansible.extra_vars = {
      nginx: {
        vhosts_conf: [
          {
            src_path: ENV['NGINX_UWSGI_SUPERVISOR_DEPLOYER_PATH'] + '/provisioning/ansible/templates/app.nginx.conf.j2',
            target_name: 'flask_skeleton.conf'
          }
        ]
      },
      uwsgi: {
        apps_conf: [
          {
            src_path: ENV['NGINX_UWSGI_SUPERVISOR_DEPLOYER_PATH'] + '/provisioning/ansible/templates/app.uwsgi.ini.j2',
            target_name: 'flask_skeleton.ini'
          }
        ]
      },
      supervisor: {
        conf: {
          path: 'supervisord.conf.j2'
        },
        apps_conf: [
          {
            src_path: ENV['NGINX_UWSGI_SUPERVISOR_DEPLOYER_PATH']  + '/provisioning/ansible/templates/app.supervisor.conf.j2',
            target_name: 'flask_skeleton.conf'
          }
        ]
      },

      application_target_root_path: "/var/www/applications/flask-skeleton",
      application: {
        name: 'flask_skeleton',
        hostname: 'flaskskeleton.com',
        user: 'www-data',
        group: 'www-data',
        port: 50058,
        src: {
          path: File.dirname(__FILE__) + '/flask_skeleton/',
          requirements_path:  File.dirname(__FILE__) + '/requirements.txt'
        },
        target: {
          app_path: "{{ application_target_root_path}}/app",
          logs_path: "{{ application_target_root_path}}/logs",
          venvs_path: "{{ application_target_root_path}}/venvs",
          static_path: "{{ application_target_root_path}}/current/flask_skeleton/apps/static"
        },
        dependencies: [
          { package: 'python2.7', version: '2.7.6-8' },
          { package: 'python-pip', version: '1.5.4-1ubuntu3' },
          { package: 'python-virtualenv', version: '1.11.4-1' },
          { package: 'python-dev', version: '2.7.5-5ubuntu3' },
        ]
      },
      deploy: {
        supervisor: {
          group: 'flask_skeleton:'
        }
      }
    }
    ansible.groups = {
      "web" => ["flaskskeleton_vm"]
    }
    ansible.limit = 'web'
  end

  config.vm.provider "virtualbox" do |vm|
    vm.name = "flaskskeleton_vm"
  end
end
