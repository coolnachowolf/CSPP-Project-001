def count(s1, s2):
    a = s1.lower()
    b = s2.lower()
    if b in a:
        return a.count(b)
    return 0

print(count("MissiSSippi", "Ss"))

# output: 2