# Try to use vscode with better comment extention to read code

import os
import platform

# ! some of grabages

path = os.path.dirname(os.path.realpath(__file__))

# ! install modules using pip

def install(pip):
    os.system(f"{pip} install pyfiglet")
    os.system(f"{pip} install colorama")

    os.chdir(path) # ? cd into path [current location]
    os.system("python3 main.py")

# ! This function will find current os and clear terminal according to it

def clear():

    running_os = platform.system() # * getting current os

    if running_os[0] == 'W':
        os.system("cls")

    else:
        os.system("clear")


# ! main function will take pip version

# ? The reason iam using many types of pip 
# ? because it should be run in many systems 
# ? with 0 errors 😇

def main(err=None):
    clear()
    if err:
        print("Sorry No Such Option :(")
    print("")
    print("How do you install python requirements ??")
    print("")
    print("pip - 1")
    print("pip3 - 2")
    print("python -m pip - 3")
    print("python3 -m pip - 4")
    print("")
    print("custom - 5")
    print("exit this shi* - 6")
    print("")

    opt = input("Enter Option Number :) ")

    if opt == "1":
        install("pip")

    if opt == "2":
        install("pip3")

    if opt == "3":
        install("python -m pip")

    if opt == "4":
        install("python3 -m pip")

    if opt == "5":
        print("")
        print("")

        custom_pip = input("what you use ?? :) ")
        install(custom_pip)

    if opt == "6":
        quit()

    else:
        main(True)

if __name__ == "__main__":
    main()