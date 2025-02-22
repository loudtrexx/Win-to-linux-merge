import platform

# OS check for the start of the program
def OS_chk():
    # Get the os and its version
    os = platform.system()
    ver = platform.version()

# Output the result
    try:

    
    
        if os == "Linux":
            print(f"Running {os} {ver}")
            pass

        else:
            print(f"You are running {os} {ver}. Program is made for GNU/Linux")
            input("Press Enter to exit ")
            exit()
    except KeyboardInterrupt:
        print("Ended by the user")
        exit()

OS_chk() 
