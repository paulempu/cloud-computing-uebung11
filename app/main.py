import os

def check_syntax():
    # Einfache Funktion
    print("Syntax Check erfolgreich!")

def unsafe_execution(command):
    # SCHLECHT: Bandit wird das hier als Security-Lücke markieren!
    # Das ist gut für deinen Bericht.
    os.system(command)

if __name__ == "__main__":
    check_syntax()
    unsafe_execution("echo 'Hello World'")
