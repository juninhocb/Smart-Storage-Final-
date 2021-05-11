s = "Joao   "
x = ""
t = ""

print(len(s))
x = s.rstrip()
print(len(x))
'''
for i in s:
    x = s.rstrip('\n')

print(len(x))


for j in s:
    if(j == '\n'):
        t = t[j].replace('\n', '')
    else:
        t = s[int(j)] 

print(len(t))
        
'''     