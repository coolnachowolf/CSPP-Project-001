def fullname(s):
    for i in range(len(s)):
        temp = s[i]
        if temp == ' ':
            return s[:i]
        
print(fullname("Donald Knuth"))