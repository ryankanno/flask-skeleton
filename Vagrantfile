# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant::Config.run do |config|
  config.vm.box = "flask_skeleton"
  config.vm.box_url = "http://goo.gl/wxdwM"
  config.vm.network :hostonly, "88.88.88.88"

  config.vm.provision :ansible do |ansible|
    ansible.playbook = "provisioning/playbook.yml"
    ansible.inventory_file = "provisioning/ansible_hosts"
    ansible.extra_vars = {
      ansible_ssh_private_key_file: Dir.pwd + "/provisioning/vagrant_key",
      flask_skeleton_src_path: Dir.pwd,
      flask_skeleton_install_path: "/home/vagrant/flask-skeleton",
      ansible_ssh_user_for_local_action: "vagrant"
    }
    ansible.verbose = true
  end
end
