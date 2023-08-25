import os
import platform
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


def osCheck():
    whichOs=platform.system()
    if whichOs == 'Linux':
        ytDlpPath='yt-dlp_linux'
        pathModifier='/'
        andModifier=";"
    else:
        ytDlpPath='yt-dlp.exe'
        pathModifier='\\'
        andModifier="&"
    return [ytDlpPath,pathModifier,andModifier]
pathInfo=osCheck()
linkList = ''''''
def getPath():
    while True:
        print(colored("enter the path where videos will be stored", "magenta"))
        print(colored('>> ', "green"), end='', flush=True) 
        path = input()
        path = path.replace("\"", "")
        path = path.replace("\'", "")  
        if os.path.isdir(path):    return path
        else:   print(colored("invalid dir","red"))
def getFormat():
    while True:
        print(colored("Which format Will be the Downloads", "yellow"))
        print("[a] mp4")
        print("[b] m4a")
        print("[c] webm")
        print(colored('>> ', "green"), end='', flush=True)
        format = input()
        if format == "a":
            format = "mp4"
            break
        elif format == "b":
            format = "m4a"
            break
        elif format == "c":
            format = "248"
            break
        else:
            print(colored("choose a valid format","red"))
    return format
def getLinkList():
    while True:
        print(colored("how should we extract the url:", "cyan"))
        print("[a] text file")
        print("[b] command line")
        print(colored('>> ', "green"), end='', flush=True)
        linkingMethod = input()
        if linkingMethod == "a":    linkList=ExctractFromText()
        elif linkingMethod == "b":  linkList=TerminalForLink()    
        else:   print(colored("please choose a valid option", "red"))
        return linkList
def ExctractFromText():
    while True:
        print("enter the path of the file")
        print(colored('>> ', "white"), end='', flush=True)
        filepath = input()
        filepath = filepath.replace("\"", "")
        filepath = filepath.replace("\'", "")
        if os.path.isfile(filepath):    break  
    with open(filepath, "r") as f:
        f = open(filepath, "r")
        ThisLinkList = f.read()
        f.close()
    ThisLinkList=ThisLinkList.replace(" ", "\n") # in case of more link in one line
    return ThisLinkList
def removeFromTerminalList(thisLinkList):
    thisLinkList = thisLinkList.replace(" ","") 
    links = thisLinkList.split("\n") 
    links.pop(-1) 
    thisLinkList = "\n".join(links) 
    thisLinkList = thisLinkList.replace(" ", "")
    return thisLinkList
def addFromTerminalList(thisLinks):
    thisList = ''
    thisLinks=thisLinks.replace(" ", "\n") # in case of more link in one line
    thisLinksList=thisLinks.split('\n')
    for eachLink in thisLinksList:
        if eachLink:        thisList += '\n'+eachLink
    return thisList
def TerminalForLink():
    linkList=''
    print("enter the urls of the video you want,type \"remove\" for remove the last link, for enter them type \"enter\"")
    while True:
        print(colored('\n >> ', "white"), end='', flush=True)
        link = input()
        if link ==      "remove":linkList=removeFromTerminalList(linkList)     
        elif link ==    "enter":break    
        else: linkList+=addFromTerminalList(link)  
        print(linkList)
    return linkList
pwd=os.getcwd()
destination=getPath()
format=getFormat()
linkList = getLinkList()
linkList = linkList.replace(' ','\n')
links = linkList.split("\n")


command = ""
for link in links:
    if link:
        command += (f"{pwd}{pathInfo[1]}{pathInfo[0]} -f {format} -i \"{link}\" -o \"{destination}{pathInfo[1]}%(title)s.%(ext)s\" ") + pathInfo[2]
os.system(command)
while True:
    print('\nDone!!')
    input()
# todo [X] check bug in remove 
# todo [X] check not finding ./yt-dlp_linux: not found
# todo [X] check text file
# todo [] check work in windows