num = int(input("enter the number"))
base = int(input("enter the base"))
array = []

def charInt(x):
    match x:
        case 10:
            return 'A'
        case 11:
            return 'B'
        case 12:
            return 'C'
        case 13:
            return 'D'
        case 14:
            return 'E'
        case 15:
            return 'F'

 
while(num > base):
    k=num%base
    if k>9:
        k = charInt(k)
    print(k)
    array.append(k)
    num = num/base

print(int(num))
for i in range (len(array)):
    print(array[i])
