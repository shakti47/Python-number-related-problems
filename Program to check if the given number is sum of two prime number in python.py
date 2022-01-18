Number = int(input("Enter the Number : "))
arr=[]

for i in range(2,Number):
    flag=0
    for j in range(2,i):
        if i%j==0:
            flag  =1

    if flag==0:
        arr.append(i)
flag = 0
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if(arr[i] + arr[j]==Number ):
            flag = 1
            print(str(arr[i]) + "and" + str(arr[j]) + 'are prime number when added gives ' + str(Number))
            break
if(flag == 0):
     print("No prime number can given sum of " + str(Number))
    
