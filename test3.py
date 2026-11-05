num = int(input("enter the number"))
array = []
x1=x2=x3=0

for i in range (0,len(str(num))):
    array.append(int(num%10))
    num = num/10

print(array)
for i in range (len(array)):
    x = array[i]
    match x:
        case 1:
            x1+=1
        case 2:
            x2+=1
        case 3:
            x3+=1
        case _:
            print("invalid input")

if(x1 != 0):
    print("number 1 is",x1)

if(x2 != 0):
    print("number 2 is",x1)

if(x3 != 0):
    print("number 3 is",x1)