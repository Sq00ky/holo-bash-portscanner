#!/usr/bin/python3
import socket
host = "1.1.1.1"
portList = [21,22,53,80,443,3306,8443,8080]

for port in portList:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		s.connect((host,port))
		print("Port ", port, " is open")
	except:
		print("Port ", port, " is closed")
