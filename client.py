import socket
import threading
import os
import time

def sending(s):
	while(1):
		try:
			msg = raw_input()
			s.send(msg.encode('utf-8'))
			if('q' in msg):
				s.close()
				break
		except:
			break

def listening(s):
	while(1):
		try:
			msg = s.recv(2048)
			print(msg + "(server)")
			if('q' in msg):
				s.close()
				break
		except:
			break
def Main():
	print("clients")
	host = '127.0.0.1'#'192.168.137.1' #'ServerIP'
	port = 8006
	s = socket.socket()
	s.connect((host,port))
	
	sending_ = threading.Thread(target = sending, args = (s, ))
	listening_ = threading.Thread(target = listening, args = (s, ))
	
	sending_.start()
	listening_.start()
	
if __name__ == '__main__':
	Main()
