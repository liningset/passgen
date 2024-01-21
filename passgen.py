#!/usr/bin/env python3

from generator import Generator
from termcolor import cprint,colored
import sys
import os

#dismiss extra long or short argument counts right off the bat
argc = len(sys.argv)
if argc == 1 or argc > 5 or "--help" in sys.argv or "-h" in sys.argv:
    print("""usage: 
    passgen.py [-l|--length] <number> 
               [-m|--modifiers] <u>ppercase,<l>owercase,<n>umbers,<s>pecials """)
    sys.exit()


def extract_cli_arguments():
    #creating fresh copy of sys.argv instead of referring to it
    args = sys.argv[1:]
    LENGTH = 8
    MODIFIERS = ""
    INTERACTIVE = False
    for arg in args:
        i = args.index(arg)
        if arg == "-l" or arg == "--length":
            try:
                if int(args[i+1]) > 0:
                    LENGTH = int(args[i+1])
                    args.remove(args[i+1])
                else:
                    cprint(f"[-] at {arg}: length must be a number higher than 0", "red")
                    sys.exit()

            except ValueError:
                cprint(f"[-] at {arg}: length is not a valid number", "red")
                sys.exit()
            except IndexError:
                cprint(f"[-] at {arg}: value for {arg} doesn't exist", "red")
                sys.exit()
        elif arg == "-m" or arg == "--modifiers":
            try:
                modifier_letters = list(set(args[i+1]))
                if all(map(lambda x: x in "luns", modifier_letters)):
                    MODIFIERS = str(args[i+1])
                    args.remove(args[i+1])
                else:
                    cprint(f"[-] at {arg}: wrong modifier, only l,u,n,s are valid", "red")
                    sys.exit()

            except IndexError:
                cprint(f"[-] at {arg}: value for {arg} doesn't exist")
                sys.exit()
        elif arg == "-i" or arg == "--interactive":
            pass

        else:
            cprint(f"[-] at {arg}: couldn't recognize {arg}", "red")
            sys.exit()
    return {"LENGTH": LENGTH, "MODIFIERS": MODIFIERS}

args = extract_cli_arguments()
generator = Generator(args["LENGTH"], args["MODIFIERS"])


os.system("clear")
password = generator.new_password()
cprint("/=-=-=-=-=-=-=-=-=-=-=\\", "light_green")
print("\n" + password + "\n")
cprint("\\=-=-=-=-=-=-=-=-=-=-=/", "light_green")

answer = input("\ndo you wanna copy to clipboard?[y/n] ")
if answer in ["yes", "y"]:
    os.system(f"echo '{password}' | xclip -sel c")
    sys.exit()



