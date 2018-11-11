#!/usr/bin/env python
#-*- coding:utf-8 -*-

# importing a useful library -- feel free to add any others you find necessary
import hashlib
import string

# this will work if you place this script in your writeup folder
#wordlist = open("probable-v2-top1575.txt", 'r')

# a string equal to 'abcdefghijklmnopqrstuvwxyz'.
salts = string.ascii_lowercase

for salt in salts:
	#salt = str(salt).encode('utf-8')
	
	with open("probable-v2-top1575.txt", 'r') as f1:
		line = f1.readline()
		while line:
			#line = line.strip()
			#line = str(line).encode('utf-8')
			#line = str(line)
			m = hashlib.sha512((salt+line).encode('utf-8').strip()).hexdigest()
			m = str(m)
			with open("hashes",'r') as f2:
				line2 = f2.readline()
				line2 = line2.strip()
				while line2:
					if m == line2:
						print("-------SUCCESS------")
						print("salt: %s" %salt)
						print("password: %s" %line)
						
					
					line2 = f2.readline()
					line2 = line2.strip()
			line = f1.readline()
	
