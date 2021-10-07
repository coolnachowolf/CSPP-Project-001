def seperate(s):
    for i in range(len(s)):
        temp = s[i]
        if temp == ' ':
            return s[i:] + ' ' + s[:i]
        
print(seperate("Donald Knuth"))