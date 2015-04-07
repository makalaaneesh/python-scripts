val="g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
#val="map"
l=[]
for let in val:
	if (ord(let) >=97 and ord(let) <=122):
		if (ord(let) +2)>122:
			l.append(chr(((ord(let)+2)%122)+96))
		else:
			l.append(chr((ord(let)+2)))
	else:
		l.append(let)


print ''.join(l)



