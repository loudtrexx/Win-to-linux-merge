import Start_OS_check
import Menu
try:
    Start_OS_check.OS_chk()
    Menu.choices()
except KeyboardInterrupt:
    print("Ended by the user")