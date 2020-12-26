# Try to use vscode with better comment extention to read code

import pyfiglet # * this module helps to create fansy art 😏
import colorama # * for garbage colors 

import random
import platform
import webbrowser
import os

# ? intializing variables and stuffs

colorama.init(autoreset=True)

# ? Core functions

def prg(word): # * color green
    print(colorama.Fore.GREEN + word)
        
        

def prd(word): # ! color red
    print(colorama.Fore.RED + word)
        

def banner(word): # for banner
    num = random.randint(1, 2)

    if num == 1:
        prg(pyfiglet.figlet_format(word))

    else:
        prd(pyfiglet.figlet_format(word))

def clear(): # clear terminal according to os

    running_os = platform.system() # * getting current os

    if running_os[0] == 'W':
        os.system("cls")

    else:
        os.system("clear")


# main

def main():
    clear()
    banner("~#Root@CKCCTV")
    prd("[*] developed by arjun arz || fadhil")
    print("")
    print("")

    opt = input(colorama.Fore.LIGHTRED_EX + "user@ckcctv #~ ")

    if opt == "help":
        clear()
        print()
        print()
        prg("show - list all cctv")
        prg("dev - show about us")
        prg("bye - quit")
        prg("help - show this message")
        print()
        print()

        abcd = input("Press enter to countinue ...")

        main()

    if "show" in opt:
        print("")
        prg("Jakarta                 - a")
        prg("CCTV JAWA BARAT website - b")
        prg("cctv website            - c")
        print("")
        prg("back - 0")
        print("")

        show_opt = input(colorama.Fore.LIGHTRED_EX + "user@ckcctv/show #~ ")

        if show_opt == "a":
            webbrowser.open("http://jasamargalive.com/webjm3/mjm/index.php?r=site/getarea&a=2&b=568")

        if show_opt == "b":
            webbrowser.open("http://rttmc.dephub.go.id/rttmc/m/page/cctv")

        if show_opt == "c":
            webbrowser.open("https://atcs.banjarmasinkota.go.id")

        if show_opt == "0":
            main()

        else:
            main()

    if "dev" in opt:
        clear()
        print("")
        print("")

        prg("Arjun Arz\n")
        prg("Certified Ethical hacker\npentester")
        print("")
        print(colorama.Fore.LIGHTGREEN_EX + "Instagram : https://instagram.com/arz_beats")
        print(colorama.Fore.LIGHTGREEN_EX + "Github : https://github.com/cyberkallan")
        print(colorama.Fore.LIGHTGREEN_EX + "Website : https://cyberkallan.com/")
        print("")
        print("")
        prg("Fadhil\n")
        prg("Student\nproffesional idiot")
        print("")
        print(colorama.Fore.LIGHTGREEN_EX + "Instagram : https://instagram.com/__fadhil_m_")
        print(colorama.Fore.LIGHTGREEN_EX + "Github : https://github.com/fadhilsaheer")
        print(colorama.Fore.LIGHTGREEN_EX + "Website : https://fadhilsaheer.github.io/")
        print("")
        print("")

        input("Press enter to countinue ...")
        main()

main()