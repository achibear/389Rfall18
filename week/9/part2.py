#!/usr/bin/env python
#-*- coding:utf-8 -*-

# importing useful libraries -- feel free to add any others you find necessary
import socket
import hashlib

host = "142.93.117.193"   # IP address or URL
port =7331      # port

# use these to connect to the service
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

# receive some data
data = s.recv(1024)
print(data)
string = data[len(data)-15:len(data)-5]
string = string.decode('utf-8')
print(string)
h = ""
if str("sha1").encode('utf-8') in data:
	print("---sha1---")
	h = hashlib.sha256(string.encode('utf-8').strip()).hexdigest()
	#h = h.encode('utf-8')
elif str("sha224").encode('utf-8') in data:
	print("---sha224---")
	h = hashlib.sha224(string.encode('utf-8').strip()).hexdigest()
	#h = h.encode('utf-8')
elif str("sha256").encode('utf-8') in data:
	print("---sha256---")
	h = hashlib.sha256(string.encode('utf-8').strip()).hexdigest()
	#h = h.encode('utf-8')
elif str("sha384").encode('utf-8') in data:
	print("---sha384---")
	h = hashlib.sha384(string.encode('utf-8').strip()).hexdigest()
	#h = h.encode('utf-8')
elif str("sha512").encode('utf-8') in data:
	print("---sha512---")
	h = hashlib.sha512(string.encode('utf-8').strip()).hexdigest()
	#h = h.encode('utf-8')
elif str("md5").encode('utf-8') in data:
	print("---md5---")
	h = hashlib.md5(string.encode('utf-8').strip()).hexdigest()
	#h = h.encode('utf-8')
else:
	print("no such hash function available")

print(h)
h = h+'\n'
h = h.encode('utf-8')
s.send(h)
data = s.recv(1024)
print(data)
while str("Find").encode('utf-8') in data:
	string = data[len(data)-15:len(data)-5]
	string = string.decode('utf-8')
	print(string)
	h = ""
	if str("sha1").encode('utf-8') in data:
		print("---sha1---")
		h = hashlib.sha1(string.encode('utf-8').strip()).hexdigest()
		#h = h.encode('utf-8')
	elif str("sha224").encode('utf-8') in data:
		print("---sha224---")
		h = hashlib.sha224(string.encode('utf-8').strip()).hexdigest()
		#h = h.encode('utf-8')
	elif str("sha256").encode('utf-8') in data:
		print("---sha256---")
		h = hashlib.sha256(string.encode('utf-8').strip()).hexdigest()
		#h = h.encode('utf-8')
	elif str("sha384").encode('utf-8') in data:
		print("---sha384---")
		h = hashlib.sha384(string.encode('utf-8').strip()).hexdigest()
		#h = h.encode('utf-8')
	elif str("sha512").encode('utf-8') in data:
		print("---sha512---")
		h = hashlib.sha512(string.encode('utf-8').strip()).hexdigest()
		#h = h.encode('utf-8')
	elif str("md5").encode('utf-8') in data:
		print("---md5---")
		h = hashlib.md5(string.encode('utf-8').strip()).hexdigest()
		#h = h.encode('utf-8')
	else:
		print("no such hash function available")
	h = h+'\n'
	h = h.encode('utf-8')
	s.send(h)
	data = s.recv(1024)
	print(data)
print(data)
# close the connection
s.close()
