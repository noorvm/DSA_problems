def operations(x,y):
    temp =1
    temp = x % y
    while temp != 0:
        x = y
        y = temp
        temp = x % y

    print(y)




num1 = int(input("enter the 1st nuumber"))
num2 = int(input("enter the 2nd number"))

if num1 > num2 :
    operations(num1,num2)
else:
    operations(num2,num1)