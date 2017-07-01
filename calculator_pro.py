from math import *
import os, sys, logging,math



def command_handle(INPUT):
    if INPUT.lower() == 'q' or INPUT =="":
        exit()
    elif INPUT.lower() == 'help':
        instruction()

def calc():
    def handle():
        INPUT = ""
        if sys.version_info[0] >= 3:
            INPUT = input("\n >>>")
        elif sys.version_info[0] < 3:
            INPUT = raw_input("\n >>>")
        INPUT.replace(" ", "")
        INPUT.replace("%", "/100")
        INPUT.replace("^", "**")
        return INPUT
    function = [i for i in dir(math)]
    INPUT = handle()
    command_handle(INPUT)
    for i in function:
        if i in INPUT.lower():
            INPUT.replace(i, "math."+i)
    try:
        INPUT = eval(INPUT)
    except Exception as e:
        logging.error(str(e))

    return print(INPUT)

def instruction():
    print("Alan's Calculator\n"
          "'q' -> quit\n"
          "'help' -> see help instruction\n"
          "empty input will cause quit\n")



if __name__ == '__main__':
    instruction()
    while(True):

        calc()
