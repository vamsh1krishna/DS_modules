# get a list of odd numbers b/w 1-20 using map and lambda ?


lis= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

res = list(map(lambda x:x%2!=0, lis))

print(res)