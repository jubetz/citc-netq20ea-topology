
vm oob-mgmt-server netq-1.4.0 2 10 40
vm netq1 netq-1.3.0 2 10 40

vm UDCLAYN00001 cumulus-vx-3.6.2 1 2 2
vm UDCLAYN00002 cumulus-vx-3.6.2 1 2 2
vm SDCLAYN00001 cumulus-vx-3.6.2 1 2 2
vm SDCLAYN00002 cumulus-vx-3.6.2 1 2 2
vm LDCLAYN00005 cumulus-vx-3.6.2 1 2 2
vm LDCLAYN00006 cumulus-vx-3.6.2 1 2 2
vm LDCLAYN00007 cumulus-vx-3.6.2 1 2 2
vm LDCLAYN00008 cumulus-vx-3.6.2 1 2 2
vm BDCLAYN00001 cumulus-vx-3.6.2 1 2 2
vm BDCLAYN00002 cumulus-vx-3.6.2 1 2 2
vm RDCLAYN00001 cumulus-vx-3.6.2 1 2 2
vm RDCLAYN00002 cumulus-vx-3.6.2 1 2 2

vm CDCLAYN00010  ubuntu-16.04 2 4 4
vm XDCLAYN00009 ubuntu-16.04 2 4 4
vm YDCLAYN00005 ubuntu-16.04 2 4 4
vm CDCLAYN00014 ubuntu-16.04 2 4 4
vm XDCLAYN00011 ubuntu-16.04 2 4 4
vm YDCLAYN00011 ubuntu-16.04 2 4 4

vm fake-spine3 cumulus-vx-3.6.2 1 2 2
vm fake-spine4 cumulus-vx-3.6.2 1 2 2
vm fake-server3 ubuntu-16.04 2 4 4
vm fake-server4 ubuntu-16.04 2 4 4
vm fake-future-spine cumulus-vx-3.6.2 1 2 2
vm fake-server6 ubuntu-16.04 2 4 4
vm fake-server7 ubuntu-16.04 2 4 4
vm fake-server8 ubuntu-16.04 2 4 4
vm fake-server9 ubuntu-16.04 2 4 4


network oob-mgmt-server eth0 10.255.0.1 255.255.0.0 public
service oob-mgmt-server ssh eth0 22 TCP public
service oob-mgmt-server http eth0 80 TCP public
service oob-mgmt-server https eth0 443 TCP public
service oob-mgmt-server http2 eth0 1337 TCP public
service oob-mgmt-server grafana eth0 3000 TCP public
service oob-mgmt-server netqgui eth0 5000 TCP public
service oob-mgmt-server novnc eth0 6080 TCP public
service oob-mgmt-server netq eth0 9000 TCP public
service oob-mgmt-server mesos eth0 5050 TCP public
service oob-mgmt-server marathon eth0 8080 TCP public
service oob-mgmt-server mesosapp eth0 8088 TCP public

network oob-mgmt-server eth1 192.168.0.1 255.255.0.0
network netq1 eth0 192.168.0.2 255.255.0.0
network UDCLAYN00001 eth0 192.168.0.11
network UDCLAYN00002 eth0 192.168.0.12
network SDCLAYN00001 eth0 192.168.0.21
network SDCLAYN00002 eth0 192.168.0.22
network LDCLAYN00005 eth0 192.168.0.35
network LDCLAYN00006 eth0 192.168.0.36
network LDCLAYN00007 eth0  192.168.0.37
network LDCLAYN00008 eth0 192.168.0.38
network BDCLAYN00001 eth0 192.168.0.41
network BDCLAYN00002 eth0 192.168.0.42
network RDCLAYN00001 eth0 192.168.0.51
network RDCLAYN00002 eth0 192.168.0.52

network CDCLAYN00010 eth0 192.168.0.61
network XDCLAYN00009 eth0 192.168.0.62
network YDCLAYN00005 eth0 192.168.0.63
network CDCLAYN00014 eth0 192.168.0.64
network XDCLAYN00011 eth0 192.168.0.65
network YDCLAYN00011 eth0 192.168.0.66

network fake-spine3 eth0 192.168.0.71
network fake-spine4 eth0 192.168.0.72
network fake-server3 eth0  192.168.0.73
network fake-server4 eth0 192.168.0.74
network fake-future-spine eth0 192.168.0.75
network fake-server6 eth0 192.168.0.76
network fake-server7 eth0 192.168.0.77
network fake-server8 eth0 192.168.0.78
network fake-server9 eth0 192.168.0.79

autoconfig oob-mgmt-server

 connect leaf01 swp51 spine01 swp1
 connect leaf02 swp51 spine01 swp2
 connect leaf03 swp51 spine01 swp3
 connect leaf04 swp51 spine01 swp4
 connect leaf01 swp52 spine02 swp1
 connect leaf02 swp52 spine02 swp2
 connect leaf03 swp52 spine02 swp3
 connect leaf04 swp52 spine02 swp4
 connect leaf01 swp49 leaf02 swp49
 connect leaf01 swp50 leaf02 swp50
 connect leaf03 swp49 leaf04 swp49
 connect leaf03 swp50 leaf04 swp50
 connect spine01 swp31 spine02 swp31
 connect spine01 swp32 spine02 swp32
 connect server01 eth1 leaf01 swp1
 connect server01 eth2 leaf02 swp1
 connect server02 eth1 leaf01 swp2
 connect server02 eth2 leaf02 swp2
 connect server03 eth1 leaf03 swp1
 connect server03 eth2 leaf04 swp1
 connect server04 eth1 leaf03 swp2
 connect server04 eth2 leaf04 swp2
 connect leaf01 swp44 oob-mgmt-server eth2
 connect leaf02 swp44 oob-mgmt-server eth3
 connect leaf01 swp45 leaf01 swp46
 connect leaf01 swp47 leaf01 swp48
 connect leaf02 swp45 leaf02 swp46
 connect leaf02 swp47 leaf02 swp48
 connect leaf03 swp45 leaf03 swp46
 connect leaf03 swp47 leaf03 swp48
 connect leaf04 swp45 leaf04 swp46
 connect leaf04 swp47 leaf04 swp48
