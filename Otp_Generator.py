import random
def otp_gen():
    while True:
        otp=random.randint(111111,999999)
        print("\nHere this is your otp:\n",otp)
        user_input=input("Do you want to generate again ? (yes/no)\n")
        if user_input.lower()=="yes":
            continue
        elif user_input.lower()=="no":
            print("Thank you for using!")
            break
        else:
            print("Sorry,I can't understand")
            break
            
print("This program is to generate otp(one time password)\n")
user_input=input("Do you want to generate an otp ?(yes/no)\n")
if user_input.lower()=="yes":
    otp_gen()
elif user_input.lower()=="no":
    print("Thank you")
    exit()
else:
    print("Soryy,I can't understand")
    exit()

    