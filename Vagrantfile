# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  config.hostmanager.enabled = true
  config.hostmanager.manage_host = true
  config.hostmanager.manage_guest = true

  config.vm.define "fedora-messaging-git-hook" do |fedora-messaging-git-hook|
    fedora-messaging-git-hook.vm.box_url = "https://download.fedoraproject.org/pub/fedora/linux/releases/38/Cloud/x86_64/images/Fedora-Cloud-Base-Vagrant-38-1.6.x86_64.vagrant-libvirt.box"
    fedora-messaging-git-hook.vm.box = "f38-cloud-libvirt"
    fedora-messaging-git-hook.vm.hostname = "fedora-messaging-git-hook.tinystage.test"

    fedora-messaging-git-hook.vm.synced_folder '.', '/vagrant', disabled: true
    fedora-messaging-git-hook.vm.synced_folder ".", "/home/vagrant/fedora-messaging-git-hook", type: "sshfs"


    fedora-messaging-git-hook.vm.provider :libvirt do |libvirt|
      libvirt.cpus = 2
      libvirt.memory = 2048
    end

    fedora-messaging-git-hook.vm.provision "ansible" do |ansible|
      ansible.playbook = "devel/ansible/playbook.yml"
      ansible.config_file = "devel/ansible/ansible.cfg"
      ansible.verbose = true
    end
  end
end
