li=[] 

for i in range(2,101):

    f=0

    for j in range(2,i+1):

        if(i!=j and i%j==0): #if any n

            f=1

            break 

    if(f==0):

        li.append(i)

print('Prime numbers between 1 to 100:')

print(*li,sep=' ')
