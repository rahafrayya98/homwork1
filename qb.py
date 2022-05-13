x=int(input('Enter the number='))
res=[] 
while x>0 :
    res.append(x%2)
    x=x//2
    res.reverse()
for x in res:
    print (x, end="")
