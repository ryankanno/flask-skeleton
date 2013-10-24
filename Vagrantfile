# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant::Config.run do |config|
  config.vm.box = "flask_skeleton"
  config.vm.box_url = "http://goo.gl/wxdwM"
  config.vm.network :hostonly, "88.88.88.88"

  config.vm.provision :ansible do |ansible|
    ansible.playbook = "provisioning/playbook.yml"
    ansible.inventory_file = "provisioning/ansible_hosts"
    ansible.extra_vars = { ansible_ssh_private_key_file: Dir.pwd + "/provisioning/vagrant_key"}
    ansible.verbose = true
  end
end
