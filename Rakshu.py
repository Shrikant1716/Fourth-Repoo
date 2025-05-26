overall=[]
odd=[]
even=[]
num=int(input("How many values you wants to add:"))
for i in range(1,num+1):
    y=int(input("Enter the value:"))
    overall.append(y)
print(overall)
for j in overall:
    if j%2==0:
        even.append(j)
    elif j%2!=0:
        odd.append(j)
    else:
        pass
print(even)
print(odd)