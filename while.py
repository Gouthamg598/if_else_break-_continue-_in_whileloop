a=1
while a<=5:
    print(a)
    a=a+2

a=1
while a<=5:
    print(a)
    if a==3:
        break
    a=a+2


a=0
while a<=5:
    a+=1
    if a>=3:
        continue
    print('goutham',a)

a=0
while a<=5:
    print(a)
    a+=1
else:
    print('goutham')
a=20
while a>15:
    print(a,end=' ')#20 19 18 17 16 
    a-=1


a=20
while a>12:
    print(a,end=' ')#20 19 18 17 16 15 14 13 
    a-=1

a=20
while a>12:
    print(a,end=' ')#20 19 18 17 
    a-=1
    if a==16:
        break
   

a=20
while a>12:
    a-=1
    if a>=16:
        continue
    print(a,end=' ')#15 14 13 12 

a=20
while a>12:
    a-=1
    if a<=15:
        print(a,end=' ')
    else:
        print('nothing',end=' ')#nothing nothing nothing nothing 15 14 13 12 

   
