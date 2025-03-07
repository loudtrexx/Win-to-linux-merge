import platform

# OS check for the start of the program
def OS_chk():
    checked = False
    while checked == False: 
        # Get the os and its version
        os = platform.system()
        ver = platform.version()
        if os == "Linux":
            print(f"Running {os} {ver}")
            checked = True
            continue

        else:
            print(f"You are running {os} {ver}. Program is made for GNU/Linux")
            input("Press Enter to exit ")
            break

#OS_chk() 
