#!/usr/bin/python3
#coding: utf-8

import re, sys, subprocess

# python3 pylord_.py <ip adress>

if len(sys.argv) != 2:
	print ('[*] Vamos no te hagas el listo\n[*] Usame bien: python3 ' + sys.argv[0] + ' <ip address>')
	sys.exit(1)

def get_ttl(ip_address):
	proc = subprocess.Popen(["/usr/bin/ping -c 1 %s" % ip_address, ""], stdout=subprocess.PIPE, shell=True)
	(out,err) = proc.communicate()
	out = out.split()
	print (out[12])

#def get_os(ttl):
#	ttl = int(ttl)
#	print (ttl)

	#if ttl >= 0 and ttl <= 64:
	#	return "Linux"
		
if __name__ == '__main__':
	ip_address = sys.argv[1]
	ttl = get_ttl(ip_address)
	#get_os(ttl)
