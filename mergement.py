import subprocess

def dirmake():
    try:
        subprocess.run(["mkdir", "/tmp/mergement"])
    except subprocess.CalledProcessError:
        pass

def check():
        judgement = subprocess.run(["/bin/bash", "List_block_devices.sh"], capture_output=True, check=True, text=True)
        print("The following devices were found: ")
        print(judgement.stdout)

def actions():
    print("What would you like to do?")
    print("1. Input the disk with windows")
    print("2. Cancel operations")
    choose = input("")
    if choose == "1":
        print("Type the name of your windows disk (Example 'sda2', 'nvme0n1p4')")
        device = input("")
        dirmake()
        print("Sudo is required.")
        subprocess.run(["sudo", "mount", "/dev/" + device, "/tmp/mergement"], capture_output=True, check=True, text=True)
    elif choose == "2":
        pass

def compilation():
    try:
        check()
        actions()
    except subprocess.CalledProcessError as e:
         print(f"Uh oh something went wrong: {e}")
         actions()

#check()
#actions()