
vm oob-mgmt-server netq-1.2.0 2 10 40
vm kdc-n7k-1 cumulus-vx-3.4.3 1 2 2
vm kdc-core-1 cumulus-vx-3.4.3 1 2 2
vm kdc-mgmt-net-1 cumulus-vx-3.4.3 1 2 2
vm libdcsl1 cumulus-vx-3.4.3 1 2 2
vm ombdcsl1 cumulus-vx-3.4.3 1 2 2
vm SRDH4IT2R26DSLX1 cumulus-vx-3.4.3 1 2 2
vm SRDH4IT2R09DSLX1 cumulus-vx-3.4.3 1 2 2
vm SRDH4IT2R26DSPC1 cumulus-vx-3.4.3 1 2 2
vm SRDH4IT2R09DSPC1 cumulus-vx-3.4.3 1 2 2
vm SRDH4IT2R20DLFX1 cumulus-vx-3.4.3 1 2 2
vm SRDH4IT2R20DLFX2 cumulus-vx-3.4.3 1 2 2
vm SRDH4IT2R24DLFX1 cumulus-vx-3.4.3 1 2 2
vm SRDH4IT2R24DLFX2 cumulus-vx-3.4.3 1 2 2
vm SRDH4IT2R20DLFG1 cumulus-vx-3.4.3 1 2 2
vm SRDH4IT1R20DLFG1 cumulus-vx-3.4.3 1 2 2
vm SRDH4IT2R26MSPX1 cumulus-vx-3.4.3 1 2 2
vm SRDH4IT2R09MSPX1 cumulus-vx-3.4.3 1 2 2
vm SRDH4IT2R20MLFG1 cumulus-vx-3.4.3 1 2 2

network oob-mgmt-server eth0 10.254.0.1 255.255.0.0 public
service oob-mgmt-server ssh eth0 22 TCP public
service oob-mgmt-server http eth0 80 TCP public
service oob-mgmt-server https eth0 443 TCP public
service oob-mgmt-server http2 eth0 1337 TCP public
service oob-mgmt-server grafana eth0 3000 TCP public
service oob-mgmt-server novnc eth0 6080 TCP public
service oob-mgmt-server netq eth0 9000 TCP public
service oob-mgmt-server mesos eth0 5050 TCP public
service oob-mgmt-server marathon eth0 8080 TCP public
service oob-mgmt-server mesosapp eth0 8088 TCP public

network oob-mgmt-server eth1 10.255.7.1 255.255.255.0
network kdc-n7k-1 eth0 10.255.7.231 255.255.255.0
network kdc-core-1 eth0 10.255.7.233 255.255.255.0
network kdc-mgmt-net-1 eth0 10.255.7.235 255.255.255.0
network libdcsl1 eth0 10.255.7.252 255.255.255.0
network ombdcsl1 eth0 10.255.7.253 255.255.255.0
network SRDH4IT2R26DSLX1 eth0 10.255.7.13 255.255.255.0
network SRDH4IT2R09DSLX1 eth0 10.255.7.14 255.255.255.0
network SRDH4IT2R26DSPC1 eth0 10.255.7.11 255.255.255.0
network SRDH4IT2R09DSPC1 eth0 10.255.7.12 255.255.255.0
network SRDH4IT2R20DLFX1 eth0 10.255.7.21 255.255.255.0
network SRDH4IT2R20DLFX2 eth0 10.255.7.22 255.255.255.0
network SRDH4IT2R24DLFX1 eth0 10.255.7.23 255.255.255.0
network SRDH4IT2R24DLFX2 eth0 10.255.7.24 255.255.255.0
network SRDH4IT2R20DLFG1 eth0 10.255.7.51 255.255.255.0
network SRDH4IT1R20DLFG1 eth0 10.255.7.58 255.255.255.0
network SRDH4IT2R26MSPX1 eth0 10.255.7.201 255.255.255.0
network SRDH4IT2R09MSPX1 eth0 10.255.7.202 255.255.255.0
network SRDH4IT2R20MLFG1 eth0 10.255.7.102 255.255.255.0

autoconfig oob-mgmt-server


connect libdcsl1 swp47 ombdcsl1 swp47
connect libdcsl1 swp48 ombdcsl1 swp48
connect libdcsl1 swp5 kdc-n7k-1 swp1
connect ombdcsl1 swp5 kdc-n7k-1 swp2
connect libdcsl1 swp7 kdc-core-1 swp1
connect ombdcsl1 swp7 kdc-core-1 swp2
connect libdcsl1 swp9 kdc-mgmt-net-1 swp1
connect ombdcsl1 swp9 kdc-mgmt-net-1 swp2
connect libdcsl1 swp1 SRDH4IT2R26DSLX1 swp1
connect ombdcsl1 swp1 SRDH4IT2R09DSLX1 swp1
connect SRDH4IT2R26DSLX1 swp51 SRDH4IT2R09DSLX1 swp51
connect SRDH4IT2R26DSLX1 swp52 SRDH4IT2R09DSLX1 swp52
connect SRDH4IT2R26DSLX1 swp49 SRDH4IT2R26DSPC1 swp1
connect SRDH4IT2R09DSLX1 swp49 SRDH4IT2R26DSPC1 swp2
connect SRDH4IT2R26DSLX1 swp50 SRDH4IT2R09DSPC1 swp1
connect SRDH4IT2R09DSLX1 swp50 SRDH4IT2R09DSPC1 swp2
connect SRDH4IT2R20DLFX1 swp49 SRDH4IT2R26DSPC1 swp5
connect SRDH4IT2R20DLFX1 swp50 SRDH4IT2R09DSPC1 swp5
connect SRDH4IT2R20DLFX2 swp49 SRDH4IT2R26DSPC1 swp6
connect SRDH4IT2R20DLFX2 swp50 SRDH4IT2R09DSPC1 swp6
connect SRDH4IT2R20DLFX1 swp51 SRDH4IT2R20DLFX2 swp51
connect SRDH4IT2R20DLFX1 swp52 SRDH4IT2R20DLFX2 swp52
connect SRDH4IT2R20DLFX1 swp53s0 SRDH4IT2R20DLFG1 swp49
connect SRDH4IT2R20DLFX2 swp53s0 SRDH4IT2R20DLFG1 swp50
connect SRDH4IT2R24DLFX1 swp49 SRDH4IT2R26DSPC1 swp7
connect SRDH4IT2R24DLFX1 swp50 SRDH4IT2R09DSPC1 swp7
connect SRDH4IT2R24DLFX2 swp49 SRDH4IT2R26DSPC1 swp8
connect SRDH4IT2R24DLFX2 swp50 SRDH4IT2R09DSPC1 swp8
connect SRDH4IT2R24DLFX1 swp51 SRDH4IT2R24DLFX2 swp51
connect SRDH4IT2R24DLFX1 swp52 SRDH4IT2R24DLFX2 swp52
#connect SRDH4IT2R24DLFX1 swp53s0 SRDH4IT2R24DLFG1 swp49
#connect SRDH4IT2R24DLFX2 swp53s0 SRDH4IT2R24DLFG1 swp50
connect SRDH4IT1R20DLFG1 swp49 SRDH4IT2R26DSLX1 swp6
connect SRDH4IT1R20DLFG1 swp50 SRDH4IT2R09DSLX1 swp6
connect SRDH4IT2R26MSPX1 swp45 SRDH4IT2R26DSLX1 swp2
connect SRDH4IT2R09MSPX1 swp45 SRDH4IT2R26DSLX1 swp3
connect SRDH4IT2R26MSPX1 swp46 SRDH4IT2R09DSLX1 swp2
connect SRDH4IT2R09MSPX1 swp46 SRDH4IT2R09DSLX1 swp3
connect SRDH4IT2R26MSPX1 swp47 SRDH4IT2R09MSPX1 swp47
connect SRDH4IT2R26MSPX1 swp48 SRDH4IT2R09MSPX1 swp48 
connect SRDH4IT2R26MSPX1 swp1 SRDH4IT2R20MLFG1 swp49
connect SRDH4IT2R09MSPX1 swp1 SRDH4IT2R20MLFG1 swp50

