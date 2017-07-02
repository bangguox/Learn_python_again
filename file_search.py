#file_search python script
import os,sys
from pathlib import Path


def input_handle():
    MODE = ""
    INPUT1 = ""
    INPUT2 = ""
    if sys.version_info[0] >= 3:
        MODE = input("\n Enter Mode name: ")
        INPUT1 = input("\n Enter file name: ")
        INPUT2 = input("\n Enter source dir name: ")
    elif sys.version_info[0] < 3:
        MODE = raw_input("\n Enter Mode name: ")
        INPUT1 = raw_input("\n Enter file name: ")
        INPUT2 = raw_input("\n Enter source dir name: ")
    File = Path(INPUT1)
    Dir = Path(INPUT2)
    if MODE.lower().strip() not in ["n","x"]:
        print("Not vaild mode")
        exit()
    if not File.is_file() and MODE != 'x':
        print(INPUT1 + " Not Exist")
        exit()
    if not Dir.is_dir():
        print(INPUT2 + " Not Exist")
        exit()
    return MODE,INPUT1, INPUT2

def do_search():
    source = input_handle()
    if source[0] == "x":
        for root,dirs,files in os.walk(source[2]):
            for file in files:
                if file.endswith(source[1]):
                    print(os.path.join(root,file))
    elif source[0] == 'n':
        for root,dirs,files in os.walk(source[2]):
            for file in files:
                if file == (source[1]):
                    print(os.path.join(root,file))



def instruction():
    print("Welcome to use my file search script\n"
          "Mode x: search file with specific extension\n"
          "Mode n: search file with normal mode")
if __name__=='__main__':
    instruction()
    do_search()