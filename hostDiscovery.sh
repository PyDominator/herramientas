#!/bin/bash

for i in $(seq 2 254); do
	timeout 1 bash -c "ping -c 1 192.168.0.19 > /dev/null 2>&1" && echo -e "[*] HOST: 192.168.0.$i \n[*] STATUS: ACTIVE \n "
done
