import os

def usr_check():
    try:
        user = os.system("whoami")
        print(user)
        if user == "root":
            print("User ok!")
            os.system("mkdir /root/test")
        
        else:
            print("Not running as root")
    except KeyboardInterrupt:
        print("Ended by the user")

usr_check()