MinVal=[]
num=int(input("How many values you wants to enter:"))
for i in range(1,num+1):
    element=int(input("Enter the value:"))
    MinVal.append(element)
print(MinVal)
print("Min value is :",min(MinVal))