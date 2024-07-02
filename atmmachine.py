import time

print("Welcome To Areebas Bank")
time.sleep(2)

print("=============================================")

print("Please Enter Your Card! ")
time.sleep(5)

password = 0000

pin = int(input("Enter Your 4 Digit Pin: "))

print("=============================================")
print("=============================================")

balance = 12000

if pin == password:
    while True:

        print("""
            1 == balance
            2 == withdraw balance
            3 == deposit balance
            4 == transfer
            5 == exit
            """
            )
        
        print("=============================================")
        print("=============================================")
        
        try:
            option=int(input("Enter Your Choice: "))
        except:
            print("Enter (1-4) only")
        
        print("=============================================")
        
        if option == 1:
            
            print("=============================================")
            print(f"Your current balance is: ${balance}")

        if option == 2:
            
            print("=============================================")
            withdraw = int(input("Enter Withdraw Amount: $"))
            balance = balance - withdraw

            print(f"${withdraw} is debited from your account")
            print(f"Your current balance is: ${balance}")
        
        if option == 3:
                        
            print("=============================================")
            deposit = int(input("Enter Deposit Amount: $"))
            balance = balance + deposit

            print(f"${deposit} is credited from your account")
            print(f"Your current balance is: ${balance}")

        if option == 4:
        
            transfer = int(input("Enter Transfer Amount: $"))
            balance = balance - transfer

            print(f"${transfer} is credited from your account")
            print(f"Your current balance is: ${balance}")
            print("=============================================")

        if option == 5:
            
            print("Thankyou for using Areebas Bank. ")
            print("=============================================")
            break


else:
    print("=============================================")
    print("Wrong Pin. Try Again ")