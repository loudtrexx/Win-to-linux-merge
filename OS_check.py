import os

def is_windows():
    return os.name == 'nt'

if is_windows():
    print("Windows installation detected.")
else:
    print("No Windows installation detected.")
