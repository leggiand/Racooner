import os
import subprocess

from Lib.termcolor import colored

print(r''' 
 ██▀███   ▄▄▄       ▄████▄   ▒█████   ▒█████   ███▄    █ ▓█████  ██▀███  
▓██ ▒ ██▒▒████▄    ▒██▀ ▀█  ▒██▒  ██▒▒██▒  ██▒ ██ ▀█   █ ▓█   ▀ ▓██ ▒ ██▒
▓██ ░▄█ ▒▒██  ▀█▄  ▒▓█    ▄ ▒██░  ██▒▒██░  ██▒▓██  ▀█ ██▒▒███   ▓██ ░▄█ ▒
▒██▀▀█▄  ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▒██   ██░▒██   ██░▓██▒  ▐▌██▒▒▓█  ▄ ▒██▀▀█▄  
░██▓ ▒██▒ ▓█   ▓██▒▒ ▓███▀ ░░ ████▓▒░░ ████▓▒░▒██░   ▓██░░▒████▒░██▓ ▒██▒
░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░ ░▒ ▒  ░░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░   ▒ ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
  ░▒ ░ ▒░  ▒   ▒▒ ░  ░  ▒     ░ ▒ ▒░   ░ ▒ ▒░ ░ ░░   ░ ▒░ ░ ░  ░  ░▒ ░ ▒░
  ░░   ░   ░   ▒   ░        ░ ░ ░ ▒  ░ ░ ░ ▒     ░   ░ ░    ░     ░░   ░ 
   ░           ░  ░░ ░          ░ ░      ░ ░           ░    ░  ░   ░     
                   ░                                                     ''')
# list that will be used for store urls
list = ''''''
# choose where store file
while True:
    print(colored("enter the path where videos will be stored", "magenta"))
    print(colored('>> ', "green"), end='', flush=True)  # custom terminal pointer
    path = input()
    pwd = os.getcwd()
    # remove the ' and " symbol for don't call exceptions
    path = path.replace("\"", "")
    path = path.replace("\'", "")
    # check if path exist , if true break and set the path as the storage
    try:
        os.chdir(path)  # try to change location, to check if the path exist
    except Exception as e:
        print(colored(e, 'red'))
    else:
        os.chdir(pwd)  # if the script change location it changes back and break the loop
        break
# ask to prompt what method use for extract link, manually on terminal or extract from a file
while True:
    print(colored("how should we extract the url:", "cyan"))
    print("[a] text file")
    print("[b] command line")
    print(colored('>> ', "green"), end='', flush=True)
    methodolinking = input()
    # extract link from file
    if methodolinking == "a":
        while True:
            print("enter the path of the file")
            print(colored('>> ', "white"), end='', flush=True)
            filepath = input()

            filepath = filepath.replace("\"", "")
            filepath = filepath.replace("\'", "")
            # check if file exist, if so it break and open it
            try:

                f = open(filepath, "r")
            except Exception as e:
                print(colored(e, 'red'))
            else:
                f.close()
                break
        f = open(filepath, "r")
        # add the url to the list
        list += f.read()
        f.close()
        break
    # type the link manually, one or more per line
    elif methodolinking == "b":
        print(
            "enter the urls of the video you want,type \"remove\" for remove the last link, for enter them type \"enter\"")
        while True:
            print(colored('\n >> ', "white"), end='', flush=True)

            link = input()
            # check before all remove so if its true it don't go to the process of adding to the list
            if link != "remove":
                # if enter break
                if link == "enter":
                    break
                # when there are more than one link on the line:
                link = link.replace(" ", "\n") # replace white space with new line

                a = link.split("\n")# divide the link based on the previously added new line
                for b in a:
                    if b:

                        list += "\n"+  b # add links and new line
            # when remove is selected
            else:
                list = list.replace(" ","") # clear the list of eventually white space
                c = list.split("\n") # transform the string in list
                c.pop(-1) # eliminate the last link
                list = "\n".join(c) # transform back the string with new line every link
                list = list.replace(" ", "") # clear the list



            print(list)

        break
    # when the user enter a invalid option
    else:
        print(colored("please choose a valid option", "red"))
        pass
# replace eventually space with new line, useful when read from text file
list = list.replace(" ", "\n")
# the command that will be executed in terminal
command = ""
# add the downlaod command for every link in the list
a = list.split("\n")
for b in a:
    if b:
        command += (f" yt-dlp.exe -i \"{b}\" -o \"{path}\%%(title)s.mp3\" ") + "&"
command += "pause & del \"%~f0\"" # pause the terminal for check log, after enter it delet the temp batch file
f = open("exec.bat", "w") # create a temp batch file
f.write(command) # write on the batch file the command to execute
f.close()
os.system("cmd /k exec.bat") # launch the batch file
