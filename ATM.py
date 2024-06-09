import time
import random

lang = "English"
lang = "Hindi"
print("Please insert your CARD")
print("Please wait while transaction is under processing......")
lang = str(input("Select language (English / Hindi) : "))

if lang == "English":
   print("Welcome to the ATM Machine...!")
else:
   print("Namaste! ATM me aapka swagat hai...")   


time.sleep(5)

passward = 12345
balance = 5000

if passward == 12345:
    print("""
        1. Create Pin
        2. Change  Pin 
        3. Next
         
        """)
    try:
       option = int(input("Please enter your choice :"))
        
    except:
        print("Invalid choice! Try again.")    
    if option == 1:
       
       accNo = str(input("Enter account last 4 digits: "))
       print("Your account number is : ", "***********"+accNo)
       mob = int(input("Enter mobile number to get OTP : "))
       otp = random.randrange(1000, 9999)
       print(f"OTP {otp} is generated for create pin.")
       user = int(input("Enter OTP : "))
       if user == otp:
        passward = int(input("Enter passward: "))
        passward = int(input("Confirm passward: "))
        print("Passward generated Successfully!")
       if user != otp:
        print("Incorrect OTP!")
        

    if option == 2:
       accNo = str(input("Enter account last 4 digits : "))
       print("Your account number is : ","***********"+accNo)
       mob = int(input("Enter mobile number to get OTP : "))
       otp = random.randrange(1000, 9999)
       print(f"OTP {otp} is generated for create pin.")
       user = int(input("Enter OTP : "))
       if user == otp:
        passward = int(input("Enter old passward: "))
        passward = int(input("Create new passward: "))
        passward = int(input("Confirm passward: "))
        print("Passward changed Successfully!")
        

if option == 3:
 pin = int(input("Enter Your Passward : "))
 if pin != passward:
    print("Incorrect pin. Try again.")
 else: 
  while True:

    print("""
        4. Balance
        5. Withdraw balance
        6. Deposite balance
        7. Exit  
        """)
      
    try:
       option = int(input("Please enter your choice :"))
        
    except:
        print("Invalid choice! Try again.")  
  
       
    if option == 4:
        print(f"Your available balance is : Rs.{balance}")
        print("\n")
        print("\n")


    elif option == 5:
        withdraw_amount = int(input("Please enter withdraw_amount :"))
        if balance <= withdraw_amount:
           print("Insufficient balance!")
        else:
         balance = balance - withdraw_amount
         print(f"Rs.{withdraw_amount} is debited from your account.")
         print(f"Your available balance is Rs.{balance}")  
         print("\n")
         print("\n")



    elif option == 6:
        deposit_amount = int(input("Please enter deposit amount :"))
        balance = balance + deposit_amount
        print(f"Rs.{deposit_amount} is credeted to your account.")
        print(f"Your availabe balance is Rs.{balance}")
        print("\n")
        print("\n")



    elif option == 7:
        print("Exit!")
        print("Thanks!\n****** Visit again.!******")
        break

  