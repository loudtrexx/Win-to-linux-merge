import platform

# OS check for the start of the program
def OS_chk():
    # Get the os and its version
    os = platform.system()
    ver = platform.version()

# Output the result
    try:
        if os == "Windows":
            print(f"You are running Windows {ver}. The script is made for GNU/Linux!")
            input("Press Enter to exit ")
            exit()
    
        elif os == "Darwin":
            print(f"You are running {os} (Likely MacOS). This script is made for GNU/Linux!")
            input("Press Enter to exit ")
            exit()
    
    
        elif os == "Linux":
            print(f"Running {os} {ver}")
            pass

        else:
            print("OS is not recognized. It could be because the current os is non-linux UNIX or ReactOS. Rerun the script if you believe this is a mistake")
            input("Press Enter to exit ")
            exit()
    except KeyboardInterrupt:
        print("Ended by the user")
        exit()

OS_chk() 
