i=2
while (i > 1 ):
    print("Banking System \nenter the No for Further procedure \n1.Account Creation\t2.Login into Existing account\t 3. exite")
    x=int(input("enter: "))
    name=""


    if(x==1):
        print("-------------create a an account---------------")
        name=input("enter the name: ")
        accntNo=input("enter the account number: ")
        pinNo=int(input("enter the Pim number to create: "))
        Amount = 1000
        print("Account created successfully")
        print("name: ",name,"\nAccount No: ",accntNo,"\nAmount :",Amount)
    elif(x==2):
        inputAccntNo=input("entert the Account no: ")
        inputpinNo=int(input("enter the pin number"))
        k=2
        if(inputpinNo==pinNo):
            print("succesfullt login into account")
            while (k > 1):
                    print("------------operations----------------")
                    print("1 = cash deposite \t2 = cash withdrawal \t3 = balance checking")
                    xInput=int(input("enter the No: "))
                    if(xInput==1):
                        print("---------cash deposite--------")
                        deposite=int(input("enter the amount to deposite: "))
                        Amount=Amount+deposite
                        print("Deposited succesfully")
                        print("balance Amount: ",Amount)
                    elif(xInput==2):
                        print("---------cash withdrawal---")
                        withdraw=int(input("enter the amount to withdraw: "))
                        if(withdraw > Amount):
                            print("insuffient Amount")
                            print("balance Amount: ",Amount)
                        else:
                            Amount=Amount-withdraw
                            print("Succesfully withdraw the amount")
                            print("balance Amount: ",Amount)
                    elif(xInput==3):
                        print("--------Balance checking-----")
                        print("balance Amount : ",Amount)
                    else:
                        print("invalid input \t exiting for login paage")
                        k=0
    else:
        print("--------------Successfully exited--------------- ")
        i=0

