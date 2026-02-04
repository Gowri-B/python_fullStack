import random

Username = input("Enter USername : ")
Password = input("Enter Password : ")
generated_otp = random.randint(1111,9999)
print(f"Generated otp : {generated_otp}")

entered_otp = int(input("please enter otp : "))

master_Username = "Admin"
master_Password = "Admin@123"

if(Username == master_Username and Password == master_Password and generated_otp):
    print("login success")
else:
    print("please check username/password/otp")