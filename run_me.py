#!/usr/bin/python

import os
import sys
from hashlib import md5
from subprocess import check_output, Popen

RESOLVER = '/etc/resolv.conf'
DNS_CONF_NEW = 'nameserver 127.0.0.1\nsearch localdomain'
DNS_CONF_OLD = 'nameserver 8.8.8.8\nsearch localdomain'


def install_iptables():
	Popen('iptables -A INPUT  -p tcp --dport 22 -j ACCEPT', shell=True)
	Popen('iptables -A OUTPUT -p tcp --sport 22 -j ACCEPT', shell=True)
	Popen('iptables -A INPUT  -p tcp -d 127.0.0.1/8 -j ACCEPT', shell=True)
	Popen('iptables -A OUTPUT -p tcp -d 127.0.0.1/8 -j ACCEPT', shell=True)
	Popen('iptables -A OUTPUT -p tcp --dport 0:32768 -j REJECT --reject-with tcp-reset', shell=True)
def restore_iptables():
	Popen('iptables -F', shell=True)

def install_dns():
	with open(RESOLVER, 'w+') as fp:
		fp.write(DNS_CONF_NEW)
def restore_dns():
	with open(RESOLVER, 'w+') as fp:
		fp.write(DNS_CONF_OLD)

def install_server():
	Popen('python bin/tuf_dns.py &', shell=True)
	Popen('nodejs bin/tuf_web.js 80 &', shell=True)
	Popen('nodejs bin/tuf_web.js 81 &', shell=True)
def restore_server():
	for pid in check_output('pgrep -f "tuf_dns.py"', shell=True).splitlines():
		Popen('kill -9 %s 2>/dev/null;true'%pid, shell=True)

	for pid in check_output('pgrep -f "tuf_web.js"', shell=True).splitlines():
		Popen('kill -9 %s 2>/dev/null;true'%pid, shell=True)
	
def _md5_file(f):
	with open(f, 'rb') as fp:
		c = fp.read()
	return _md5(c)
def _md5(data):
	return md5(data).hexdigest()

if __name__ == '__main__':
	'''
	This script will change your IPTABLES and DNS config
	Be awared before you change it
	'''
	print 'Read the source code'
	exit()

	m = sys.argv[1]
	if m == 'install':
		install_dns()
		install_iptables()
		install_server()
	elif m == 'restore':
		restore_dns()
		restore_iptables()
		restore_server()