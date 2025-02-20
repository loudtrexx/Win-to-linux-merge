import subprocess

def usr_check():
    try:
        user = subprocess.run(["whoami"],capture_output=True,text=True)
        user = user.stdout.strip()
        print(user)
        if user == "root":
            print("User ok!")
            root_check()
            
        
        else:
            print("Not running as root")
            exit()
    except KeyboardInterrupt:
        print("Ended by the user")

def root_check():
    try:
                subprocess.run(["mkdir", "/root/test"], check=True, capture_output=True, text=True)
                subprocess.run(["rm", "-fr", "/root/test"], check=True)
                print("Root check was successful!")
            
    except subprocess.CalledProcessError as e:
        print(e.stderr)
        if "File exists" in e.stderr:
            print("Yes")
            subprocess.run(["mv", "/root/test/", "test1"])
            print("Your old 'test' folder in '/root' was renamed to 'test1'. The script will try again.")
            root_check()
        elif "Permission denied":
            print("Failed to write to '/root'. Are you fakerooted?")
    except KeyboardInterrupt:
        print("Ended by the user")

usr_check()
root_check()