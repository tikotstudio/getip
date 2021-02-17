import socket

def ip(ipuser, port):
	socket.gethostbyname(socket.gethostname())
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.connect((ipuser,port))
	print(s.getsockname()[0])
	s.close()

def help():
	print("To get an ip address, you need to register one line of code:\ngetip.ip (site.address, port)")