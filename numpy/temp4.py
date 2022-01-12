# d1 = {1:2, 3:4, 'a':'b'}
# d2 = {3:1, 4:4, 10:'a', 'a':[1,2,3]}

# d1 = {1:2, 3:4, 10:5}
# d2 = {3:1, 4:4, 10:'a'}

d1 = {1:2, 3:4, 'a':'b'}
d2 = {0:1, 4:4, 10:'a'}

op = d2

for k,v in d1.items():
    if k in d2:
        temp1=[]
        temp1.append(d1[k])
        temp1.append(d2[k])
        op[k] = temp1
    else:
        op[k]=d1[k]

print(op)