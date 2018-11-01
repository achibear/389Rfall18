#!/usr/bin/env python2

import sys
import struct
import binascii

# You can use this method to exit on failure conditions.
def bork(msg):
    sys.exit(msg)


# Some constants. You shouldn't need to change these.
MAGIC = 0xdeadbeef
VERSION = 1
PNG = "\x89\x50\x4E\x47"
PNG2 = "\x0d\x0a\x1a\x0a"
if len(sys.argv) < 2:
    sys.exit("Usage: python2 stub.py input_file.fpff")

# Normally we'd parse a stream to save memory, but the FPFF files in this
# assignment are relatively small.
with open(sys.argv[1], 'rb') as fpff:
    data = fpff.read()

# Hint: struct.unpack will be VERY useful.
# Hint: you might find it easier to use an index/offset variable than
# hardcoding ranges like 0:8
magic, version = struct.unpack("<LL", data[0:8])
time,name1 = struct.unpack("<LL", data[8:16])
name2,sc = struct.unpack("<LL", data[16:24])

if magic != MAGIC:
    bork("Bad magic! Got %s, expected %s" % (hex(magic), hex(MAGIC)))

if version != VERSION:
    bork("Bad version! Got %d, expected %d" % (int(version), int(VERSION)))

print("------- HEADER -------")
print("MAGIC: %s" % hex(magic))
print("VERSION: %d" % int(version))
print("Time: %d" % int(time))
print("name1: %s" % hex(name1))
print("name2: %s" % hex(name2))
print("section numbers: %s" % hex(sc))

# We've parsed the magic and version out for you, but you're responsible for
# the rest of the header and the actual FPFF body. Good luck!

print("-------  BODY  -------")
print(len(data))
sec1type,sec1len = struct.unpack("<LL", data[24:32])
print("sec 1 type: %s" %hex(sec1type))
print("sec 1 slen: %s" %hex(sec1len))
s1v1, s1v2 = struct.unpack("<LL", data[32:40])
s1v3, s1v4 = struct.unpack("<LL", data[40:48])
s1v5, s1v6 = struct.unpack("<LL", data[48:56])
s1v7, s1v8 = struct.unpack("<LL", data[56:64])
s1v9, s1v10 = struct.unpack("<LL", data[64:72])
s1v11, s1v12 = struct.unpack("<LL", data[72:80])
s1v13 = struct.unpack("<H", data[80:82])
s1v14 = struct.unpack("<B", data[82:83])
print("sec 1 val: %s" %hex(s1v1))
print("sec 1 val: %s" %hex(s1v2))
print("sec 1 val: %s" %hex(s1v3))
print("sec 1 val: %s" %hex(s1v4))
print("sec 1 val: %s" %hex(s1v5))
print("sec 1 val: %s" %hex(s1v6))
print("sec 1 val: %s" %hex(s1v7))
print("sec 1 val: %s" %hex(s1v8))
print("sec 1 val: %s" %hex(s1v9))
print("sec 1 val: %s" %hex(s1v10))
print("sec 1 val: %s" %hex(s1v11))
print("sec 1 val: %s" %hex(s1v12))
print("sec 1 val: %X" %s1v13)
print("sec 1 val: %X" %s1v14)

sec2type = struct.unpack("<L", data[83:87])
sec2len = struct.unpack("<L", data[87:91])
s2v1, s2v2 = struct.unpack("<LL", data[91:99])
s2v3, s2v4 = struct.unpack("<LL", data[99:107])
s2v5, s2v6 = struct.unpack("<LL", data[107:115])
s2v7, s2v8 = struct.unpack("<LL", data[115:123])
s2v9, s2v10 = struct.unpack("<LL", data[123:131])
s2v11, s2v12 = struct.unpack("<LL", data[131:139])
s2v13, s2v14 = struct.unpack("<LL", data[139:147])
s2v15 = struct.unpack("<L", data[147:151])
print("sec 2 type: %X" %sec2type)
print("sec 2 len: %X" %sec2len)
print("sec 2 val: %s" %hex(s2v1))
print("sec 2 val: %s" %hex(s2v2))
print("sec 2 val: %s" %hex(s2v3))
print("sec 2 val: %s" %hex(s2v4))
print("sec 2 val: %s" %hex(s2v5))
print("sec 2 val: %s" %hex(s2v6))
print("sec 2 val: %s" %hex(s2v7))
print("sec 2 val: %s" %hex(s2v8))
print("sec 2 val: %s" %hex(s2v9))
print("sec 2 val: %s" %hex(s2v10))
print("sec 2 val: %s" %hex(s2v11))
print("sec 2 val: %s" %hex(s2v12))
print("sec 2 val: %s" %hex(s2v13))
print("sec 2 val: %s" %hex(s2v14))
print("sec 2 val: %X" %s2v15)

sec3type,sec3len = struct.unpack("<LL", data[151:159])
s3v1, s3v2 = struct.unpack("<LL", data[159:167])
s3v3, s3v4 = struct.unpack("<LL", data[167:175])

print("sec 3 type: %s" %hex(sec3type))
print("sec 3 len : %d" %int(sec3len))
print("sec 3 val: %s" %hex(s3v1))
print("sec 3 val: %s" %hex(s3v2))
print("sec 3 val: %s" %hex(s3v3))
print("sec 3 val: %s" %hex(s3v4))

sec4type,sec4len = struct.unpack("<LL", data[175:183])
s4v1 = struct.unpack("<L", data[183:187])
print("sec 4 type: %s" %hex(sec4type))
print("sec 4 len: %s" %hex(sec4len))
print("sec4 val: %X" %s4v1)

sec5type,sec5len = struct.unpack("<LL", data[187:195])
s5v1, s5v2 = struct.unpack("<LL", data[195:203])
s5v3, s5v4 = struct.unpack("<LL", data[203:211])
s5v5, s5v6 = struct.unpack("<LL", data[211:219])
s5v7, s5v8 = struct.unpack("<LL", data[219:227])
s5v9, s5v10 = struct.unpack("<LL", data[227:235])
s5v11, s5v12 = struct.unpack("<LL", data[235:243])
s5v13, s5v14 = struct.unpack("<LL", data[243:251])
s5v15 = struct.unpack("<L", data[251:255])
print("sec 5 type: %s" %hex(sec5type))
print("sec 5 len: %s" %hex(sec5len))
print("sec 5 val: %s" %hex(s5v1))
print("sec 5 val: %s" %hex(s5v2))
print("sec 5 val: %s" %hex(s5v3))
print("sec 5 val: %s" %hex(s5v4))
print("sec 5 val: %s" %hex(s5v5))
print("sec 5 val: %s" %hex(s5v6))
print("sec 5 val: %s" %hex(s5v7))
print("sec 5 val: %s" %hex(s5v8))
print("sec 5 val: %s" %hex(s5v9))
print("sec 5 val: %s" %hex(s5v10))
print("sec 5 val: %s" %hex(s5v11))
print("sec 5 val: %s" %hex(s5v12))
print("sec 5 val: %s" %hex(s5v13))
print("sec 5 val: %s" %hex(s5v14))
print("sec 5 val: %X" %s5v15)


sec6type,sec6len = struct.unpack("<LL",data[255:263])
print("sec 6 type: %s" %hex(sec6type))
print("sec 6 len: %d" %int(sec6len))
f = open("s6 result.txt","w")
for i in range(991):
	s6v,= struct.unpack("<B",data[263+i:264+i])
	f.write(chr(s6v))
	print(chr(s6v))
f.close()
s6v2, = struct.unpack("<B",data[1252:1253])
s6v3, = struct.unpack("<B", data[1253:1254])
print(chr(s6v2))
print(chr(s6v3))
print("end s6")

sec7type, sec7len = struct.unpack("<LL", data[1254:1262])
s7v1, s7v2 = struct.unpack("<LL",data[1262:1270])
s7v3, s7v4 = struct.unpack("<LL",data[1270:1278])
print("sec 7 type: %s" %hex(sec7type))
print("sec 7 len: %d" %int(sec7len))
print("sec 7 val: %s" %hex(s7v1))
print("sec 7 val: %s" %hex(s7v2))
print("sec 7 val: %s" %hex(s7v3))
print("sec 7 val: %s" %hex(s7v4))

sec8type, sec8len = struct.unpack("<LL", data[1278:1286])
print("sec 8 type: %s" %hex(sec8type))
print("sec 8 len: %d" %int(sec8len))
f = open("s8.png","wb")
f2 = open("s8result.txt","wb")
#PNG = binascii.unhexlify(PNG)
#PNG2 = binascii.unhexlify(PNG2)
f.write(PNG)
f.write(PNG2)
#out=[]
for i in range(245614):
	s8v,=struct.unpack("<B",data[1286+i:1287+i])
	if i<5:
		print("s8: %X" %s8v)
	f2.write(data[1286+i])
	f.write(data[1286+i])
	
	

FOOT = [0x49, 0x45, 0x4e, 0x44]
FOOT2 = [0xae, 0x42, 0x60, 0x82]
#FOOT = binascii.unhexlify(FOOT)
#FOOT2 = binascii.unhexlify(FOOT2)
#f.write(out)
f.write(FOOT)
f.write(FOOT2)	
f.close()
f2.close()

sec9type, sec9len = struct.unpack("<LL", data[246900:246908])
print("sec 9 type: %s" %hex(sec9type))
print("sec 9 len: %d" %int(sec9len))
f = open("s9 result.txt","w")
for i in range(22):
	s9v,= struct.unpack("<B",data[246908+i:246909+i])
	f.write(chr(s9v))
	
f.close()


sec10type, sec10len = struct.unpack("<LL", data[246930:246938])
print("sec 10 type: %s" %hex(sec10type))
print("sec 10 len: %d" %int(sec10len))
f = open("s10 result.txt","w")
for i in range(45):
	s10v,= struct.unpack("<B",data[246938+i:246939+i])
	f.write(chr(s10v))
	
f.close()


sec11type, sec11len = struct.unpack("<LL", data[246983:246991])
print("sec 11 type: %s" %hex(sec11type))
print("sec 11 len: %d" %int(sec11len))
s11v1, s11v2 = struct.unpack("<LL", data[246991:246999])
s11v3, s11v4 = struct.unpack("<LL", data[246999:247007])
s11v5, s11v6 = struct.unpack("<LL", data[247007:247015])
s11v7, s11v8 = struct.unpack("<LL", data[247015:247023])
s11v9, s11v10 = struct.unpack("<LL", data[247023:247031])
s11v11, s11v12 = struct.unpack("<LL", data[247031:247039])
print("sec 11 val: %s" %hex(s11v1))
print("sec 11 val: %s" %hex(s11v2))
print("sec 11 val: %s" %hex(s11v3))
print("sec 11 val: %s" %hex(s11v4))
print("sec 11 val: %s" %hex(s11v5))
print("sec 11 val: %s" %hex(s11v6))
print("sec 11 val: %s" %hex(s11v7))
print("sec 11 val: %s" %hex(s11v8))
print("sec 11 val: %s" %hex(s11v9))
print("sec 11 val: %s" %hex(s11v10))
print("sec 11 val: %s" %hex(s11v11))
print("sec 11 val: %s" %hex(s11v12))



