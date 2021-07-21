#!/bin/bash

# ./portScan.sh <ip adress>

if [ $1 ]; then
	ip_addres=$1
	for port in $(seq 1 65535); do
		timeout 1 bash -c "echo ' ' > /dev/tcp/$ip_addres/$port" 2>/dev/null && echo "[*] el puerto $port esta abierto"
	done; wait

else
	echo -e "\n [*] Uso: ./portScan.sh <ip adress>\n"
exit 1
fi
