import json
inputf='quistion.json'
inputf=open(inputf, 'r')
res=0
name=input('Enter your name: ')
dic=dict()
d=json.load(inputf)
inputf.close()
for key,value in d.items():
    print (key)
    ans=input()
    if ans==value:
        res=res+1
        dic[key]=value
dic[name]=res
print (dic)
outf='result.json'
outf =open(outf, 'w')
json.dump(dic,outf)
outf.close()
