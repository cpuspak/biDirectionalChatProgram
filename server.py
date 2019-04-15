import socket
import threading
import os
import time

def sending(c,addr):
	while(1):
		try:
			msg = raw_input()
			c.send(msg.encode('utf-8'))
			if('q' in msg):
				c.close()
				break
		except:
			break

def listening(c,addr):
	while(1):
		try:
			msg = c.recv(2048)
			print(msg+"(client)")
			if('q' in msg):
				c.close()
				break
		except:
			break
	
	
def Main():
	host = socket.gethostbyname('0.0.0.0')
	port = 8006
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
	s.bind((host,port))
	s.listen(5)
	c,addr = s.accept()
	print("Connected to ip : "+ str(addr))
	
	sending_ = threading.Thread(target = sending, args = (c, addr))
	listening_ = threading.Thread(target = listening, args = (c, addr))
	
	sending_.start()
	listening_.start()
	
if __name__ == '__main__':
	Main()
