# os for running terminal commands during the script, webbrowser to open github
import webbrowser, os

def choices():
    try:
        print("Select one of the options:")
        print("1. Check for windows installations")
        print("2. project github")
        print("3. Manual (Coming soon!)")
        print("4. Exit")
        choose = input()
        if choose == "1":
            print("Function coming soon!")
    
        elif choose == "2":
            webbrowser.open("github.com/loudtrexx/Win-to-linux-merge")
            print("Github opened!")
            choices()
    
        elif choose == "3":
            print("Function coming soon!")
        
        elif choose == "4":
            print("Closing...")
            exit()
    
        else:
            input(f"{choose} is not a valid choice! Continue with enter")
            os.system("cls")
            choices()
    # Handle Keyboard interrupts and TypeErrors
    except KeyboardInterrupt:
        print("Ended by the user")
    except TypeError:
        input("Something went wrong... Continue with Enter:")
        choices()

choices()