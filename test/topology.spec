
vm oob-mgmt-server netq-1.0.0 2 10 40
vm leaf01 cumulus-vx-3.3.2 1 2 2
vm leaf02 cumulus-vx-3.3.2 1 2 2
vm spine01 cumulus-vx-3.3.2 1 2 2
vm spine02 cumulus-vx-3.3.2 1 2 2
vm server01 ubuntu-16.04 2 4 4
vm server02 ubuntu-16.04 2 4 4

network oob-mgmt-server eth0 10.255.0.1 255.255.0.0 public
service oob-mgmt-server ssh 10.255.0.1 22 TCP public
service oob-mgmt-server http 10.255.0.1 80 TCP public
service oob-mgmt-server https 10.255.0.1 443 TCP public
service oob-mgmt-server http2 10.255.0.1 1337 TCP public
service oob-mgmt-server grafana 10.255.0.1 3000 TCP public
service oob-mgmt-server novnc 10.255.0.1 6080 TCP public
service oob-mgmt-server netq 10.255.0.1 9000 TCP public
service oob-mgmt-server mesos 10.255.0.1 5050 TCP public
service oob-mgmt-server marathon 10.255.0.1 8080 TCP public
service oob-mgmt-server mesosapp 10.255.0.1 8088 TCP public

network oob-mgmt-server eth1 192.168.0.254 255.255.0.0
network leaf01 eth0 192.168.0.11 255.255.0.0
network leaf02 eth0 192.168.0.12 255.255.0.0
network spine01 eth0 192.168.0.21 255.255.0.0
network spine02 eth0 192.168.0.22 255.255.0.0
network server01 eth0 192.168.0.31 255.255.0.0
network server02 eth0 192.168.0.32 255.255.0.0

autoconfig oob-mgmt-server

 connect leaf01 swp51 spine01 swp1
 connect leaf02 swp51 spine01 swp2
 connect leaf01 swp52 spine02 swp1
 connect leaf02 swp52 spine02 swp2
 connect leaf01 swp49 leaf02 swp49
 connect leaf01 swp50 leaf02 swp50
 connect spine01 swp31 spine02 swp31
 connect spine01 swp32 spine02 swp32
 connect server01 eth1 leaf01 swp1
 connect server01 eth2 leaf02 swp1
 connect server02 eth1 leaf01 swp2
 connect server02 eth2 leaf02 swp2
 connect leaf01 swp45 leaf01 swp46
 connect leaf01 swp47 leaf01 swp48
 connect leaf02 swp45 leaf02 swp46
 connect leaf02 swp47 leaf02 swp48
