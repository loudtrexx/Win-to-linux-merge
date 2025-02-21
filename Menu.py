# os for running terminal commands during the script, webbrowser to open github
import webbrowser, os

def choices():
    try:
        print("Select one of the options:")
        print("1. Check for windows installations")
        print("2. project github")
        print("3. Read the project wiki or edit it!")
        print("4. Exit")
        choose = input()
        if choose == "1": # Begin the real deal when it is done
            print("Function coming soon!")
    
        elif choose == "2": # Open github page (Duh)
            webbrowser.open("github.com/loudtrexx/Win-to-linux-merge")
            print("Github opened!")
            choices()
    
        elif choose == "3":
            webbrowser.open("https://github.com/loudtrexx/Win-to-linux-merge/wiki/")
            print("Opening wiki...")
            choices()
        
        elif choose == "4":
            print("Closing...")
            exit()
    
        else: # Notify user that input is invalid
            input(f"{choose} is not a valid choice! Continue with enter")
            os.system("clear")
            choices()
    # Handle Keyboard interrupts and TypeErrors
    except KeyboardInterrupt:
        print("Ended by the user")
    except TypeError:
        input("Something went wrong... Continue with Enter:")
        choices()

choices()