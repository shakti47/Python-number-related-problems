
'''n=int(input())
n=str(n)
n=list(n)
r=' '

for i in range(len(n):
               if(n[i]==0):
                       n[i]='1'

                r=r + n[i]

del n

print(int(r))
'''
n=int(input("Enter any number"))

s=str(n)

l=[]

for i in s:

    if(i=='0'):

        l.append('1')

    else:

        l.append(i)

ns=""

for i in l:

    ns+=i

print(int(ns))

