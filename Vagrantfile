# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.require_version ">= 1.7.2"

Vagrant.configure(2) do |config|

  config.ssh.insert_key = true

  config.vm.box = "ubuntu/trusty64"
  config.vm.box_check_update = false
  config.vm.define "flaskskeleton.local"

  config.vm.hostname = 'flaskskeleton.local'
  config.vm.network "private_network", ip: "192.168.58.58"
  config.vm.network "forwarded_port", guest: 80, host: 50058, auto_correct: true

  config.vm.provision :ansible do |ansible|
    ansible.playbook = "provisioning/playbook.yml"
    ansible.extra_vars = {
      flask_skeleton_src_path: Dir.pwd,
      flask_skeleton_install_path: "/home/vagrant/flask-skeleton",
    }
    # ansible.verbose = 'vvvv'
  end

  config.vm.provider "virtualbox" do |vm|
    vm.name = "flaskskeleton.local"
  end
end
