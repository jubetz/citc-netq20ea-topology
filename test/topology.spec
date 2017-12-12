
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

"oob-mgmt-switch" [function="oob-switch" mgmt_ip="10.255.7.254"]
 "oob-mgmt-server" [function="oob-server" mgmt_ip="10.255.7.1"]
 "kdc-n7k-1" [function="leaf" os="CumulusCommunity/cumulus-vx" version="3.4.3" memory="768" config="./helper_scripts/extra_switch_config.sh" mgmt_ip=""]
 "kdc-core-1" [function="leaf" os="CumulusCommunity/cumulus-vx" version="3.4.3" memory="768" config="./helper_scripts/extra_switch_config.sh" mgmt_ip="10.255.7.233"]
 "kdc-mgmt-net-1" [function="leaf" os="CumulusCommunity/cumulus-vx" version="3.4.3" memory="768" config="./helper_scripts/extra_switch_config.sh" mgmt_ip=""] 
 "libdcsl1" [function="exit" os="CumulusCommunity/cumulus-vx" version="3.4.3" memory="768" config="./helper_scripts/extra_switch_config.sh" mgmt_ip=""]
 "ombdcsl1" [function="exit" os="CumulusCommunity/cumulus-vx" version="3.4.3" memory="768" config="./helper_scripts/extra_switch_config.sh" mgmt_ip=""]
 ."SRDH4IT2R26DSLX1" [function="exit" os="CumulusCommunity/cumulus-vx" version="3.4.3" memory="768" config="./helper_scripts/extra_switch_config.sh" mgmt_ip=""]
 ."SRDH4IT2R09DSLX1" [function="exit" os="CumulusCommunity/cumulus-vx" version="3.4.3" memory="768" config="./helper_scripts/extra_switch_config.sh" mgmt_ip=""]
 ."SRDH4IT2R26DSPC1" [function="spine" os="CumulusCommunity/cumulus-vx" version="3.4.3" memory="768" config="./helper_scripts/extra_switch_config.sh" mgmt_ip=""]
 ."SRDH4IT2R09DSPC1" [function="spine" os="CumulusCommunity/cumulus-vx" version="3.4.3" memory="768" config="./helper_scripts/extra_switch_config.sh" mgmt_ip=""]
 ."SRDH4IT2R20DLFX1" [function="leaf" os="CumulusCommunity/cumulus-vx" version="3.4.3" memory="768" config="./helper_scripts/extra_switch_config.sh" mgmt_ip=""]
 ."SRDH4IT2R20DLFX2" [function="leaf" os="CumulusCommunity/cumulus-vx" version="3.4.3" memory="768" config="./helper_scripts/extra_switch_config.sh" mgmt_ip=""]
 ."SRDH4IT2R24DLFX1" [function="leaf" os="CumulusCommunity/cumulus-vx" version="3.4.3" memory="768" config="./helper_scripts/extra_switch_config.sh" mgmt_ip=""]
 ."SRDH4IT2R24DLFX2" [function="leaf" os="CumulusCommunity/cumulus-vx" version="3.4.3" memory="768" config="./helper_scripts/extra_switch_config.sh" mgmt_ip=]
 ."SRDH4IT2R20DLFG1" [function="leaf" os="CumulusCommunity/cumulus-vx" version="3.4.3" memory="768" config="./helper_scripts/extra_switch_config.sh" mgmt_ip=""]
 ."SRDH4IT1R20DLFG1" [function="leaf" os="CumulusCommunity/cumulus-vx" version="3.4.3" memory="768" config="./helper_scripts/extra_switch_config.sh" mgmt_ip=""]
 ."SRDH4IT2R26MSPX1" [function="spine" os="CumulusCommunity/cumulus-vx" version="3.4.3" memory="768" config="./helper_scripts/extra_switch_config.sh" mgmt_ip=""]
 ."SRDH4IT2R09MSPX1" [function="spine" os="CumulusCommunity/cumulus-vx" version="3.4.3" memory="768" config="./helper_scripts/extra_switch_config.sh" mgmt_ip=""]
 ."SRDH4IT2R20MLFG1" [function="leaf" os="CumulusCommunity/cumulus-vx" version="3.4.3" memory="768" config="./helper_scripts/extra_switch_config.sh" mgmt_ip=""]




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

network oob-mgmt-server eth1 10.255.7.254 255.255.255.0
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
