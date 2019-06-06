list = ["a",11,"b","c","ff",25.5,55,77]
c = 0
a = []
b = []
d = []
while ( c < len(list)):
    if(type(list[c])==str):
        a.append(list[c])
    elif(type(list[c])==int):
        b.append(list[c])
    else :
        d.append(list[c])
        
    c+=1

print (a)
print (b)
print (d)
