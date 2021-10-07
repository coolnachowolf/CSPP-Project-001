def seperate(s):
	l = len(s)
	temp = s[0:l:2], s[1:l:2]
	return temp

print(seperate("a-c-e-g-i-")) 

# output: acegi-----