sudo apt-get install -qy  python-dev libssl-dev  sshpass build-essential libffi-dev
sudo pip install setuptools --upgrade
sudo pip install ansible --upgrade
rm -rf ansible-push-keys
sudo mkdir /etc/ansible
sudo cp hosts /etc/ansible/hosts
sudo cp ansible.cfg /etc/ansible/ansible.cfg
sudo chmod -R 777 /etc/ansible
git clone https://github.com/cumulusnetworks/ansible-push-keys
cd ansible-push-keys; cat /etc/dhcp/dhcpd.hosts | grep 'host .* {' | cut -d " " -f 2 >> hosts
cd ansible-push-keys; ansible-playbook push-keys.yml --extra-vars 'ansible_ssh_pass=CumulusLinux!' --extra-vars 'ansible_become_pass=CumulusLinux!'
rm -rf ansible-push-keys
ansible-playbook setup.yaml
git clone -b netq2-ea-evpn https://github.com/CumulusNetworks/cldemo-netq/ ~/evpn
sudo systemctl enable cts-kubectl-config.service
sudo systemctl start cts-kubectl-config.service &
