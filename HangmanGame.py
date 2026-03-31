# HANGMAN GAME

import colorama
colorama.init()

import random
from random import randint
import math
import time
import os
import sys

## Never Delete this List because it will ruine the code!
LoadList = []
## Alphabet checking
AlphabetCaps = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
RemoveItems = []
CorrectItems = []

SaveAlphCap = sorted(AlphabetCaps)

GameSelection = ['Sports','Space','Celebrities','Games','Random','Back']

GenreText = "Random"

FileNotFound = []
IOErrorFound = []

j = 0
load = random.randint(1,5)

DictionaryNotFound = False 
SportsNotFound = False 
SpaceNotFound = False 
CelebritiesNotFound = False 
GamesNotFound = False
MainMenuNotFound = False  
GameTitleNotFound = False 

DictionaryIOError = False
SportsIOError = False
SpaceIOError = False
CelebritiesIOError = False
GamesIOError = False
MainMenuIOError = False
GameTitleIOError = False

# Loading BookOfWords

BookOfWords = []

filename = "dictionary.txt"
try:
    fo = open(filename, "r")
except FileNotFoundError:
    FileNotFound.append(filename)
    DictionaryNotFound = True
except IOError:
    IOErrorFound.append(filename)
    DictionaryIOError = True
else:
    LoadList = fo.readlines()
    for item in LoadList:
        item = item.strip()
        BookOfWords.append(item)
    
    fo.close()

Genre = sorted(BookOfWords)

# Loading MainMenu

MainMenu = []

filename2 = "mainmenu.txt"
LoadList.clear()
try:
    fo2 = open(filename2, "r")
except FileNotFoundError:
    FileNotFound.append(filename2)
    MainMenuNotFound = True
except IOError:
    IOErrorFound.append(filename2)
    MainMenuIOError = True
else:
    LoadList = fo2.readlines()
    for item in LoadList:
        item = item.strip()
        MainMenu.append(item)

    fo2.close()

# Loading Title

Title = []

filename3 = "title.txt"
LoadList.clear()
try:
    fo3 = open(filename3, "r")
except FileNotFoundError:
    FileNotFound.append(filename3)
    GameTitleNotFound = True
except IOError:
    IOErrorFound.append(filename3)
    GameTitleIOError = True
else:
    LoadList = fo3.readlines()
    for item in LoadList:
        item = item.strip()
        Title.append(item)

    fo3.close()

# Sports

Sport = []

filename4 = "Sports.txt"
LoadList.clear()
try:
    fo4 = open(filename4, "r")
except FileNotFoundError:
    FileNotFound.append(filename4)
    SportsNotFound = True
except IOError:
    IOErrorFound.append(filename4)
    SportsIOError = True
else:
    LoadList = fo4.readlines()
    for item in LoadList:
        item = item.strip()
        Sport.append(item)

    fo4.close()

# Space

Space = []

filename5 = "Space.txt"
LoadList.clear()
try:
    fo5 = open(filename5, "r")
except FileNotFoundError:
    FileNotFound.append(filename5)
    SpaceNotFound = True
except IOError:
    IOErrorFound.append(filename5)
    SpaceIOError = True
else:
    LoadList = fo5.readlines()
    for item in LoadList:
        item = item.strip()
        Space.append(item)

    fo5.close()

# Celebrities

Celebrities = []

filename6 = "Celebrities.txt"
LoadList.clear()
try:
    fo6 = open(filename6, "r")
except FileNotFoundError:
    FileNotFound.append(filename6)
    CelebritiesNotFound = True
except IOError:
    IOErrorFound.append(filename6)
    CelebritiesIOError = True
else:
    LoadList = fo6.readlines()
    for item in LoadList:
        item = item.strip()
        Celebrities.append(item)

    fo6.close()

# Game

Games = []

filename7 = "Game.txt"
LoadList.clear()
try:
    fo7 = open(filename7, "r")
except FileNotFoundError:
    FileNotFound.append(filename7)
    GamesNotFound = True
except IOError:
    IOErrorFound.append(filename7)
    GamesIOError = True
else:
    LoadList = fo7.readlines()
    for item in LoadList:
        item = item.strip()
        Games.append(item)

    fo7.close()

# --------------------------



def SuperSecretSettings():
    ''' Important Note ! This may give a user a seagure because of bright and flashing colours .
        DO THIS AT YOUR OWN RISK!!! '''
    clear()
    j = 0
    load = randint(10,50)
    time.sleep(5)
    print(colorama.Fore.RED + colorama.Style.BRIGHT + '\n                              ______________________________                                    \n                             /  _____/\\_   _____/\\__    ___/                                    \n                            /   \\  ___ |    __)_   |    |                                       \n                            \\    \\_\\  \\|        \\  |    |                                       \n                             \\______  /_______  /  |____|                                       \n                                    \\/        \\/                                                \n__________.____________  ____  __.__________ ________  .____    .____     ___________________   \n\\______   \\   \\_   ___ \\|    |/ _|\\______   \\_____  \\ |    |   |    |    \\_   _____/\\______ \\  \n |       _/   /    \\  \\/|      <   |       _/ /   |   \\|    |   |    |     |    __)_  |    |  \\ \n |    |   \\   \\     \\___|    |  \\  |    |   \\/    |    \\    |___|    |___  |        \\ |    `    |____|_  /___|\\______  /____|__ \\ |____|_  /\\_______  /_______ \\_______ \\/_______  //_______  /\n        \\/            \\/        \\/        \\/         \\/        \\/       \\/        \\/         \\/\n\n        ')
    time.sleep(0.1)
    clear()
    print(colorama.Fore.BLUE + colorama.Style.BRIGHT + '\n                              ______________________________                                    \n                             /  _____/\\_   _____/\\__    ___/                                    \n                            /   \\  ___ |    __)_   |    |                                       \n                            \\    \\_\\  \\|        \\  |    |                                       \n                             \\______  /_______  /  |____|                                       \n                                    \\/        \\/                                                \n__________.____________  ____  __.__________ ________  .____    .____     ___________________   \n\\______   \\   \\_   ___ \\|    |/ _|\\______   \\_____  \\ |    |   |    |    \\_   _____/\\______ \\  \n |       _/   /    \\  \\/|      <   |       _/ /   |   \\|    |   |    |     |    __)_  |    |  \\ \n |    |   \\   \\     \\___|    |  \\  |    |   \\/    |    \\    |___|    |___  |        \\ |    `    |____|_  /___|\\______  /____|__ \\ |____|_  /\\_______  /_______ \\_______ \\/_______  //_______  /\n        \\/            \\/        \\/        \\/         \\/        \\/       \\/        \\/         \\/\n\n        ')
    time.sleep(0.1)
    clear()
    print(colorama.Fore.YELLOW + colorama.Style.BRIGHT + '\n                              ______________________________                                    \n                             /  _____/\\_   _____/\\__    ___/                                    \n                            /   \\  ___ |    __)_   |    |                                       \n                            \\    \\_\\  \\|        \\  |    |                                       \n                             \\______  /_______  /  |____|                                       \n                                    \\/        \\/                                                \n__________.____________  ____  __.__________ ________  .____    .____     ___________________   \n\\______   \\   \\_   ___ \\|    |/ _|\\______   \\_____  \\ |    |   |    |    \\_   _____/\\______ \\  \n |       _/   /    \\  \\/|      <   |       _/ /   |   \\|    |   |    |     |    __)_  |    |  \\ \n |    |   \\   \\     \\___|    |  \\  |    |   \\/    |    \\    |___|    |___  |        \\ |    `    |____|_  /___|\\______  /____|__ \\ |____|_  /\\_______  /_______ \\_______ \\/_______  //_______  /\n        \\/            \\/        \\/        \\/         \\/        \\/       \\/        \\/         \\/\n\n        ')
    time.sleep(0.1)
    clear()
    print(colorama.Fore.GREEN + colorama.Style.BRIGHT + '\n                              ______________________________                                    \n                             /  _____/\\_   _____/\\__    ___/                                    \n                            /   \\  ___ |    __)_   |    |                                       \n                            \\    \\_\\  \\|        \\  |    |                                       \n                             \\______  /_______  /  |____|                                       \n                                    \\/        \\/                                                \n__________.____________  ____  __.__________ ________  .____    .____     ___________________   \n\\______   \\   \\_   ___ \\|    |/ _|\\______   \\_____  \\ |    |   |    |    \\_   _____/\\______ \\  \n |       _/   /    \\  \\/|      <   |       _/ /   |   \\|    |   |    |     |    __)_  |    |  \\ \n |    |   \\   \\     \\___|    |  \\  |    |   \\/    |    \\    |___|    |___  |        \\ |    `    |____|_  /___|\\______  /____|__ \\ |____|_  /\\_______  /_______ \\_______ \\/_______  //_______  /\n        \\/            \\/        \\/        \\/         \\/        \\/       \\/        \\/         \\/\n\n        ')
    time.sleep(0.1)
    clear()
    print(colorama.Fore.WHITE + colorama.Style.BRIGHT + '\n                              ______________________________                                    \n                             /  _____/\\_   _____/\\__    ___/                                    \n                            /   \\  ___ |    __)_   |    |                                       \n                            \\    \\_\\  \\|        \\  |    |                                       \n                             \\______  /_______  /  |____|                                       \n                                    \\/        \\/                                                \n__________.____________  ____  __.__________ ________  .____    .____     ___________________   \n\\______   \\   \\_   ___ \\|    |/ _|\\______   \\_____  \\ |    |   |    |    \\_   _____/\\______ \\  \n |       _/   /    \\  \\/|      <   |       _/ /   |   \\|    |   |    |     |    __)_  |    |  \\ \n |    |   \\   \\     \\___|    |  \\  |    |   \\/    |    \\    |___|    |___  |        \\ |    `    |____|_  /___|\\______  /____|__ \\ |____|_  /\\_______  /_______ \\_______ \\/_______  //_______  /\n        \\/            \\/        \\/        \\/         \\/        \\/       \\/        \\/         \\/\n\n        ')
    time.sleep(0.1)
    clear()
    while j < load:
        print(colorama.Fore.GREEN + colorama.Style.BRIGHT + "                           ;xxxxxxxxxxxxxxxxxxxxxxxxxxxxxkkkkkkkkkkkkxxxddddddddddxxxxxxxxxxxddddddooooddddxxxxxxxxxdddddoooooooooddxxxdddddddxxxxxxxxxxxxxxxxdddooodddddddd;                           \n                           :xxxxxxxxxxxxxxxxxxxxxxxxxxxxxkkkkkkkkkkkkkxxdddddddddxxkkkkkkkkkxxxxxxxddddddxkkkkkkkkkkxxxxxddooooooooodxxxxxxxxxxxxxxxxxxxxxxddddddooodddddddd;                           \n                           :xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxdddddddddxxkkkkkxxddddddddddddddddxxkkkkkkkkkkkkxxxdoooooooooddxkkkkkkkkkxxxxxxxxxxddxxdddooodddddddd;                           \n                           :xxxxxxxxxxxxxxxxxxxxxkkkkxxkkkkxxxxdddddddddxxxxxxxdxxxxxddddooooooooodddxxxdddddddxxdddxxxxxxxdooooooooodxxkkkkkkkkkxxxxxxxxxxxxxxdddoodddddddd;                           \n                           :xxxxxxxxxxxxxxxxxxkkOOOkxxkOOOOkkkkkxxxxxxxxxxxxxxxxddddddddddddooooodxxxxkkkxxxddddxxddddddddddoooooodooodddxxxxxxxxxxxxxxxxxxxxxxdddoodddddddd;                           \n                           ;xxxxxxxxxxxxxxxxxkOOOkkxxxkOOOOkkOOOkkkkkkkkxxxxxxxxxxxxxdddddddoooollcclllccloddddddxxdddooooooooooooooooodddxxxxxkkOOkkxkkkkxxxxdddooodddddddd;                           \n                           ;xxxxxxxxxxxxkkkOkOOkkxxxxxkkOOkkOOOOOOOOOOOOkxxxxxxxxkkkkkkxddodddl:;,,,,,,,,,,;:loddddddxxxdxddooooooodddxxxkkkkkkOOOOOkkxkOOkxxddooooodddddddd;                           \n                           ;xxxxxxxxxxxkkOOOOOOkxxxxkkOOOOkkOOOOOOOOOOkkxxxxxxxxxxkkkkkkxddddoc;''''..'''''',;:odddxxkxxxxddooooooodxkkkkkkOOOOOOOOOOkxxkkkkxddooooodddddddd;                           \n                           ;xxxxxxkkkxxxxkkkOOkxxxkkOOOOOOkOOOOOOkkxxxxxkxxxxxxkxxxxxxxdddddoc:;,,'''''''''',,,:oddxxxxddddooooooooddxxkkkkkOOOOOOOOkxxxdddxxxxddddddddddddd;                           \n                           ;xxxxkkOOOOkkxxxxxkxxxxkOOOOOOOkkkkkkxxxxxxkkkkxxxxxkkxxddddddddlccc::ccccccccccc:,,;lddddoooooodddoooooooddddxxkkOOOOOOOOkkxddddxxxxxxxddxxxxxxd;                           \n                           ;xxkOOOOOOOOOkxxxxxxxkOOOOOOOOkkxxxxxxxxxxkOOkxxxxxxxxxxxxkkkkkd:;:ccccllloooooool:,;odxxdddoooddxddoooddddododddxkkkOOOOOOkkxddddxkkxxxxxxxxxxxd;                           \n                           :xkOOOOOOOOOOkkxxxxxkOO000OOkkxxxkkxxxxxxkOO0OkxxxxxxxxxkOOOOkkd:::::::cllllooooooc;:oxkkkxxxdoooddoooodxxxddooodddxxxkOOOkkkxdddddxxxxxxkkkkxxxx;                           \n                           :kOOOOOOOOOOOOOkkxxxkOOOOOkkxxxxkOOOOkkxxkO00OkxxxxxxkOOOOOOOkkxlcc::::::ccllcclllc:cdkkkkkkkxdddoooooodxxxxdddoddddddxxkkkkkxxdddddxxxkkOOOOkkkx;                           \n                           :kOOOOOOOOOOOOOOkxxxxkkxxxxxxxxkkOOOOOOkkkkO0OkxxxxxkOOOOOOOkkdooolccc::::cllcccllclxkkkkkkkkxxxxdooooodxkkxdddddxxxdddddxxkkkkxdddxxxkkO00000OOk:                           \n                           :kOOOOOOOO000OOkkxxxxxxxxxxxxxxkkOOOOkkkxkkkkkxxxxxxxkOOOOOOkxolodlcccc::cclolooooloxkkkkkkkkxxxxdoooooddxxddddxxxxxxdddddddxkkkxxxxkOOOO0000000Oc                           \n                           :kOOOOOOOO000OOkxxxxxxxxkkkkkxxxxkkOkxxxkOkkxxxxxxxxkOOOOOOOkkxooolccc::::clloooolloxkkkkkkkkkxxdooooooodddddddxxxkxxxdddddddddxxxxkOOO0000000000c                           \n                           :kOOOOOOOOOOOOOkkxxkkkkxxkkOkxxxxxxxxxxkOOOOkxxxxxxxxkOOOOOOkkkxxdlc::::ccllooooloodxkkkkkkkkkxxxdoooooooodxxdddxkkkxddddddddddxxxxkkO00000000000c                           \n                           :kOOOOOOOOOOOOOkxxxkOOkxxxxxxxxkkxxxxxkOOOOOOkxxxxxxxxxxkOOOkkkkxdlc:::::cclllloooodxxkkkkkkkxxdddooooooddxkkxxdxxxxddddxxkxxxxxxxxxkO00000000000c                           \n                           :kOOOOOOOOkkkkxxxxkkOOOkkxxxxxkOOOOkxxkOOOO0OkxxxxxkxxxxxkkkkkkxdolccccclllollloooooddxkkkkkkxdooooooooodxkkkkkxxdxxxxdddxxddxkOkkxkkO0000000000Oc                           \n                           ;kOOOOOOkkxxxxxxxxxkkkkkkkxxxxkOOOOOkxkOOOOOkxxxxxkkkkxdddxxxxddolc:::::ccclllloddoooddxxkxxddoodddooooodxkkkkkxxxkkkxxdddddxkOOOkxxkOO000000000Oc                           \n                           ;xkkOOkkxxxxxxxxddxddxxxxddddxxkOOOOkxxkOOOOkxxxxxxxxxddddddooooolcc::::cccllllodddddddddddoooooddddoooodxkkkkkxxkOOkkxxdddxkOOOOkkxxxkkOO000000Oc                           \n                           ;dxxkkxxxxxxxxxxddxxxxxxdddxdddxkkkkkxxkkkkkkdddddddddxxkkxxddddlccclcllllllllooc;coxxddddddddoooooooooooxxkkkkxxkOOkkxddddxxkkkkkxxxxxxxkOO000OOc                           \n                           ;xxdxddxxkkkkkxkkkkkkkkxdxxkxdddxkkkkxdxkkkkxdddddddddxxdollloool::cc:cccllllldo:''';:cldxxxxxxdooooooooodxxkkxxkkOOkxddddddddddxxxxxxxxxxkOO000Oc                           \n                           ;xddddxxkkkkkkkkkkkkkkxddxkkkxdddxkkkxdddxxxdddddddoolc:,''';lddoc:c::::clllodxo;......',;clodxxddooooooodxxkxxxkkkkkxdddddddxxxkkxxxxxkkkkkkkOOk:                           \n                           ;dddddxxkkkkkkkkkkkkkxdddxkkxxxdddxxxdxxdddddoollc:;,'......,loddolc::::looddxd:'...........',:coddoooooodddddddxkkxddddxxxdddxkkkkkkkkOOOOkkxxkx;                           \n                           ;dddddxxkkkkkkkkkkkkxxdddxxxdddddddddxkkkkxdol;,''..........'looodoc:;;:lodxdo;'................',:coooooooooooooddddddxkkkxdddxkkkOkkkOOO0OOkxxx;                           \n                           ;ddddxkkkOOOkkkkkkkkxdddddddddddddddxkkkkkkxo:'..............,;::cc::;;:loddl;.....................'cooooodddxddoooooddxxxkxddddxkkkkkkOOOOOOkxxx;                           \n                           ;ddddxkkkOkkkxkkkxxxddddddxxxdddddddxkkkkkkxl,.................,;:::::::cclc;'......................,lddoddxxxxxdoooddddddddddddxkkkkkkkkOOOOkxxx;                           \n                           ;dddxkkkkkkxxxxdddddddddxxkxxddodddddxkkkkkxc'.................,;:::cllc:cc:'.......................'cdddddxxxxxdooooddxxxxdddddxxkkkkkkkOOOOOkxx;                           \n                           ;ddddxxxxxxxdddddodddxxxkkxxxdoddddoddxxkkkd:'.................';;;:cllc:c:,.........................:oddddxxxxdoooodddxkOOkxdddddxxxxxxxkOOOOOkx:                           \n                           ;ddddddddxxxxxxddddxxkkkkkxxdoodxxdddddxkkko;..................';;;;colc:c:'.........................;oddddxxxdoooddxxdxOOOOkkxddddddddddxkOOOOkx;                           \n                           ;odddddxxkkkkkkxdddxxkxxkxxddodxxxddddddxkkl,...................,;;;;cc:::,..........................,ldddxxxxdooodxkxxxkOOOOOOOkxddddddddxxxxkxx;                           \n                           ;odddxxkkkkkkkkxdoodxxxxxxxdoodxxxxddddddxxl'...................,;;;;;;;;,'..........................,lddddxxdooodxkOkxxkOOOOOOOOkxdxxxxxkkxxxxxx;                           \n                           ;oddxkkkkkkkkkkxdoooddxxxxxdodxxxddddddddxxl'...................,;;;;;:;'............................'cddddxdoooodxkOOkxxkOOOOOOOkxxxkkxkkOOkkxxx;                           \n                           ;oddxxkkkkkkkkxddoooodxxxxdoodxxddoddxxxdddc'...................';:;;;;,..............................:odddddoddddxxkOOkxxkOOOOkxxddxkkkkkOOOOkkx:                           \n                           ;oddddxkkkkxxdddodddooddxxdoddxdddddddxxddo:'...................';:;;;;'..............,;,'............;oddddooxxxdddxkOkxxkOOOOkxxxxxkkxxkOOOOOOk:                           \n                           ;ddddddxkkxddddddxxxxdoooooooooodxxxxxdddol;....................';:;;;,.............',;::::;,'........,ldddooddddddddxkkxxxkOOkxxxxxxxxxxkOOOOkkx;                           \n                           ;dxxdddddddddddxxkkkxdooooooooodxkkkkkxddoc,.....................,;;;;,.............';;;:cccc:........'cdddoooddxkxxddddddxxkxxxkkkxdddddkOOOkxxx:                           \n                           ;dxxxxxddddddxxxkkkkkxddoooooddxkkkkkOkxxdc'.....................',;;;'.............';;::cccc:'........;odddoodxkkkkkxddddddxxxkOOOkxddoodxxxxxxk:                           \n                           ;ddxdxxddddddxxxxddxddddooooddxxxkkkkkkkxxl,.....................'',,,'..............';:::ccc:'........,ldddddxkkkkkkkxxdddddxxkkOOkkxddooddxxkkkc                           \n                           ;dxxxxxdddddxxxxxxxxddddoooodxxxxkkkkkkkkxl,......................'',,.................,;:cc:,..........cdddddxxkkkkkkxxdddddxxkkkxxxxxdooddxkkkk:                           \n                           ;dxkkkxddddxxxkkkkxxxxxdoooooddxkkkkOkkkxdl;......................'',,..................,;;;,...........cddddxxxkkkkkkxxddooddxxxxxxxxdddoddxxxkx:                           \n                           ;dxxxxxddddxxkkxxkxxxxxdooooooodkkkkOkxddddo:'....................',,,...............  ................;ldddoddxxxxkkxxddooodxxxxxxxxxxxddddxkkOk:                           \n                           ;dxxxxxddddxxxxxxxxxxxxdooooooodxkkkkxdddddoc'....',,'''''........''',................ ...............'cddddoooddxxxxdooooooodxxxxxxxxxxddddxxkkk:                           \n                           ;dxxxxdddddxxxxxxxxxxxxdooodddooddxddddxxddoc'...,:clllll:,........'''................. ..............;lddddddooddddddooooooodxxxxxxxxxxdddddxkkk:                           \n                           ;dxxxxddoodxxxxxxxxxxxxdooodxdddoddddxxkkxddo:'.';clllcc:;'.........''...............................,lddddddddddddooooddoooodxxxxxxxxxxdddddxkkk:                           \n                           ;dxxxddooodxxxxxxxxxxxxdooodxxxxddddxkkkkxdddoc;,,;::;;;;;,..........'..................   .......',:oddddddddddddddddddddooodxxxxxxxxxxxddddxkkk:                           \n                           ,oddddoooodddxxxxxxxxxdoooodxxxxdddxkkkkkxddddoolc:;;;;;:;,..........'......................';ccclooddddddddddddddddddddddooddxxxxxxxxxxxddddxxkk:                           \n                           ,oddddoooodddddddddddddoooodxddoddddxxkkkxddddoooooc;;;;:;...........'......................,lddddddddddddddddddddddddddddooodddxxxxxxxxddddddxxx:                           \n                           ,oddxdoooddxxxxxxxxxxxddoooddooodddddddkkxddoooooddl;,,,'............'......................':oddddddddddddddddddddddddddddddddddddddddddddoodxxx;                           \n                           ,oddddooodxxxxxxxxxxxxxdoooooooddxxddddddddoooooodo:.................'.......................'coddddddddddddddddddddddddddddddxxxxxxxxxxxddoodxxx:                           \n                           ;oddddooodxxxxxxxxxxxxxdooooooddxxxxxdooooooooooooc'.................'........................:odddddddddddddddddddddddddddddddxxxxxxxxxxxddoddxd;                           \n                           ;odddooooddxxxxxxxxxxxddooooooddxxxxdddooooooooodo;.................''........................;odddddddddddddddddddddddddddddddxxxxxxxxxxdddoodxd;                           \n                           ;odddoooodddxxxxxxxxxxdooooddddddddddddddooooodddl'.................''............',..........;lddddddddddddddddddddddddddddddxxxxxxxxxxxxddoodxd;                           \n                           ;odddooooddddxxxxxxxxddoooodddddddddddddddddddddo:'.................''........................,ldddddddddddddxxxdddxxxxxxdddddxxxxxxxxxxxxddooddd;                           \n                           ,oooooooooooodddddddddooooooooodddddddddooooodddo;..................''........................,cdddxxxxxxxddxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxdddddd;                           \n")
        time.sleep(0.05)
        clear()
        print(colorama.Fore.RED + colorama.Style.BRIGHT + "                           ;xxxxxxkxxxxxxxxxxxxxxxxxkkkkkkkkkkkkkkkkkkxxddddddddddxxxxxxxxxxxxxxxddooooddddxxxxxxxxxxxxdddooooooooddxxxdddddddxxxxxxxxxxxxxxxxxddddodddddddd;                           \n                           ;xxxxxxxxxxxxxxxxxxxxxxxxxxxxxkkkkkkkOOkkOkkxdddddddddxxkkkkkkkkkkxxxxxxddddddxkkkkkkkkkkxxxxxddooooooooddxxxxxxxxxxxxxxxxxxxxxxxxdddddoooddddddd;                           \n                           ;xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxkkxxddddddddxxkkkkkkxxddddddddddddddddxxkkkkkkkkkkkkxxxdooooooooodxxkkkkkkkkxxxxxxxxxxxxxxxxdddoooddddddd;                           \n                           ;xxxxxxxxxxxxxxxxxxxxxkkkkxxkkkkxxxxxxdddddddxxxxxxxxxxxxxxddddddooooooddddddddddddxxdddxxxxxxxxdooooooooodxxkkkkxxkkkxxxxxxxxxxxxxxxdddooddddddd;                           \n                           ;xxxxxxxxxxxxxxxxxxkkOOOkxxkOOOOkkkkkkxxxxxxxxxxxxxxxxdddddddddxddoooddollccccc:::clodxddddddddddoooooodoooddddxdxxxxxxxxxxxxxxxxxxxxdddodddddddd;                           \n                           ;xxxxxxxxxxxxxxxxkkOOOOkxxxkOOOOOOOOOkkkkkkkkkxxxxxxxxxxxxxdddddddddddo:,,,'',,,,,,,;codddddoooooooooooodooodddxxxxxkkOOkkxkkkkkxxxxdddoodddddddd;                           \n                           ;xxxxxxxxxxxkkkOOOOOkkxxxxxkOOOOOOOOOOOOOOOOOkxxxxxxxxkkOkkkxxdddddddoc:,''''..''''',,;codxxxddddooooooodddxxxkkkkkkOOOOOkkxkOOOkxddddooodddddddd;                           \n                           ;xxxxxxxxxxxkkOOOOOOkxxxkkkOOOOOOOOOOOOOOOOkkxxxxxxxxxkkkkkkkxdddxxddl:;;,,,,'',,,,,,,,;lxxxxxxddooooooddxkkkkkkkOOOOOOOOkkxxkkkkxdddddoddddddddd;                           \n                           ;xxxxxxkkkkxxxkkOOOkkxxkOOOOOOOOOOOOOOkkxxxxxkxxxxxkkxxxxxxxxddddddlcccccccclccllllc:;',cdxxddddooooooooddxxkkkkkkOOOOOOOkxxxxxxxxxxxdddddddxxxxd;                           \n                           ;xxxxkkOOOOkkxxxxkkxxxxkOOOOOOOkkkkkkxxxxxxkkkkxxxxkkkxxxddddxxdddo:;:cccccllooooooolc;;cddooooodddoooooooodddxxkkOOOOOOOOOkxxdddxxxkxxxdddxxxxxd;                           \n                           ;xxkOOOOOOOOOkxxxxxxxkOO000OOOkkxxxxxxxxxkkOOOkxxxxxkxxxxkkkkkkkxdoc:cc::::ccllloooooc;;ldddoooodxddoooddddoooddxxkkkOOOOOOOkxddddxkxxxxdxxxxxxxx;                           \n                           :xkOOOOOOOO0OkkxxxxxkO00000OkkxxxkkkxxxxxkO00OkxxxxxxxkkkOOOOOOkkxdollc::::::cllcccllc:cdxxxxdoooddoooodxxxddoooddddxxkOOOkkkxdddddddddxxkkkkkxxx;                           \n                           :kOOOOOOOOOOOOOkkxxxkOOOOOkkxxxxkOOOOkkxxkO00OkxxxxxkkOOOOOOOOOkkdoddoccccc::clllccllcldkkkkkxddooooooodxxxxdddoodddddxxkkkkkkxddddddxxxkOOOOOkkx;                           \n                           :kOOOOOOOOOOOOOOkxxxxkkxxxxxxxxkOOOOOOOkkkkO0OkxxxxxkOO0OOOOOkOkkdlodlcccc:::clooooooloxkkkkkkxxxdooooodxkkxdddddxxxdddddxxkkkkxddddxxxkO00000OOk:                           \n                           :kOOOOOOOO0000OkkxxxxxxxxxxxxxxkOOOOOkkkxkkkkkxxxxxxkkO000OOOOOkkxoddlccc:::cllooooolloxkkkkkkxxxdoooooddxxddddxxxkxxdddddddxxkkxdxxkOOO00000000Oc                           \n                           :kOOOOOOOO0000OkxxxxxxxxkkkkkxxxxkkOkxxxkkOkxxxxxxxxkO00OOOOOkkkkkxxdlc:::::clllloooodxkkkkkkkxxddooooooddddoddxxxkkxxddoddddddddxxxOOO0000000000c                           \n                           :kOOOOOOOOOO0OOkkxxkkkkxxkkOkxxxxxxxxxxkOOOOkkxxxxxxkkOOOOOOOkkkkkxxdlcc::::clllllodxxxkkkkkkkxxxdoooooooodxddddxkkkxdddddxxddddxxxxkO00000000000c                           \n                           :kOOOOOOOOOOOOOkxxxkOOkxxxxxxxxkkkxxxxkOOOO0OkxxxxxxxxxkkOOOOkkkxxddolccccccllollloddxkkkkkkkxxxddooooooddxxkxxddxxxddddxxkxxdxxxxxxkO00000000000c                           \n                           :kOOOOOOOOkkkkxxxxkkOOOkkxxxxxkOOOkkxxkOOOOOOkxxxxxkkxxxkkkOOkkxdddolcc:::::ccllllododxkkkkkxxdooooooooodxkkkkkxdddxxddddxxddxkkkkxxkO0000000000Oc                           \n                           :kOOOOOOkkxxxxxxxxxkkkkkkkxxxxkOOOOOkxkOOOOOkxxxxxkkkkxxddxxxxddoddolcc:::cccllllooloodxxxxxddooddddoooodxkkkkkxxxkkkxxddddddxOOOkxxkOO000000000Oc                           \n                           ;xkkOOkkxxxxxxxxxddddxxxxddddxxkOOOOkxxkOOOOkxxxxxxxxxxddddddoooddolccc::ccclllllol;;:loddooooooddddooooodxxkkkxxkOOkkxxdddxkOOOOkkxxxkkOOO00000Oc                           \n                           ;dxxkkxxdxxxxxxxddxxxxxxdddxdddxkkkkkxxkkkkkxxddddddddxxxxxoolloddollllcccccclloddc'..',;:cllooooddoooooodxxkkxxxkkkkkxddoddxkkkkkxxxxxxxkkO0000Oc                           \n                           ;xxxxddxxkkkkkxkkkkkkkkxdxxkxxddxkkkkxdxkkkkxdddddddddddoc:;,,;ldddlc::cccccclodxo;'.......',,;::cloooooodxxxxxdxkkkkxdooooodddddddxxxxxxxxkO000Oc                           \n                           ;dddddxxkkkkkkkkkkkkkkxddxkkkxxddxkkkxdddxxxxddodoollc:;'.....,ldddl:::cllloddxdo;'...............',;:coddxxxxddxkkkkddddddoddxxxxxxxxxxkxxkkkOOk:                           \n                           ;dddddxxkkkkkkkkkkkkkxdddxkkkxxdddxxxxxxxdddddoooc;,,'........,clllc:;:coddddddl,.....................':oddddoooxxkxdoddxxxdddxkkkkkkkkOOOOkkxxkx:                           \n                           ;dddddxxkkkkkkkkkkkkxxdddxxxdddddddddxkkkkxxdddol;.............'',;:;;;:ccllooc,.......................'codoooooodddoodxkkkxdodxxkkkkkkOOOOOOkxxx:                           \n                           ;ddddxkkkkOkkkkkkkkkxdddddddddddddddxkkkkOOkxddoc,...............';;;;:cc:::::;'........................;oddddddooooooddxxkxdoodxkkkkkkkOOOOOkxxx:                           \n                           ;ddddxkkkOkkkkkkkxxxddddddxxxdddodddxkkkkkkkxddo:'...............';;:::::::::;'.........................'cdxxxxxdooooooddddddoddxkkkkkkkkkOOkkxxx;                           \n                           ;dddxkkkkkkxxxxdddddddddxxkxxxdodddddxkkkkkxdddo:'...............';:cll:::::;,'..........................;oxxxxxdooooodxxxxddddddxkkkkxkkkOOOOkxx;                           \n                           ;ddddxxdxxxxxddddddddxxxkkkxxdodddddddxkkkkxddoo:'...............';:lol:;:;;;'...........................;odxxddoooooodxkkkkxddddddxxxxxxkkOOOOkx;                           \n                           ;ddddddddxxxxxxddddxxkkkkkxxddodxxdddddxkkkxddol;................';clol:;;;;,'...........................,ldxxddoooddddxkOOOkkxdddooddddddkkOOOkx;                           \n                           ;odddddxxkkkkkkxdddxxkkkkkxxdoddxxxddddxxkkxddol,................';:cc:;;;;;'.............................;odxdooooxxxddkOOOOOOkxdddddddoddxxxxxx;                           \n                           ;odddxxkkkkkkkkxdoddxxxkkxxddodxxkxxddddxkkxddol,.................,;;;;,,;;,'.............................':oddooodxkkxdxkOOOOOOOkxdxxxxxxxxxxxxx;                           \n                           ;oddxkkkkkkkkkkxdoooddxkkxxdodxxxxdddxxddxkxddol,.................';;;;,,;;,.........,:;;,,,,'.............';codoodkkkkxdxkOOOOOOkxdxkkxxkkOkxxxx;                           \n                           ;oddxxkkkkkkkkxxdoooddxxxxddodxxdddddxkxdxxxddol,..................,;;;,;;,'........';;::ccccc;'..............,cooddxkkxdxkkOOOkxxddxkkxxkOOOOkkx;                           \n                           ;oddddxkkkkxxxddoddddoddxxdodxxddddddxxxxdxdddoc,..................',;;;;,,..........,;;:cccccc;................;coddxkkddxkOOOkxddxxkkxxkkOOOOOk:                           \n                           ;ddddddxkkxxdddddxxxxdooodooodoodxxkxxxdddddddo:'...................,;;;,,'...........,;::cccclc,.................;lddxxdddkOkkxxxxxxxxxxkkOOOkkx;                           \n                           ;xxxdddddddddddxxkkkxxdoooooooodxkkkOOkxddddddo:....................';;,,,'............,;::ccccc:'................':oddddddxxxxxkkkxxddddxkOkkxxx:                           \n                           ;dxxxxxdddddxxxkkkkkkxddoooooddxkkkkOOOkxxddddo;...................'';;,,'................',;:cc:,.................cddddddddddxkkOOkxddoodxxxxxxx:                           \n                           ;ddxdxxddddddxxxxxxxxxdddoooddxxxkkkkkkkkxxdddo:'''.......',,,,;;;;,,;;,'....................';;,'.................:dxxdddddddxkkkkkkxddooddxxxkk:                           \n                           ;dxxxxxdddddxxxxxxxxxxddoooddxxxxkkkkkkOkkxddddoc,....',,;:c::;;:c:,',,,'..............................'...........,oxxddoooddxxxxxxxxxdooodxxkkk:                           \n                           ;dxkxxxddddxxxkkkkxxkxxddoooodxxkkkOOOOkkxxdddddl,....'..';:;;;;;::,',,'....................   ........''..........;oxxxdooooddxxxxxxxdddodddxxkx:                           \n                           ;dxxxxxddddxxkkxxxxkkxxdooooooodxkkOOkxxxxddddddoc,.......,;;;;;;;,'',,'.....................     ...............,:ldxddooooodxxxxxxxxxxddddxxkkk:                           \n                           ;dxxxxdddddxxxxxxxxxxxxdooooooodxkkkkxxxxxdxdddddol:;'.....,;;;;;,...,,'................'.....      ..,;,,,,,,;:lddxxdooooooodxxxxxxxxxxdddddxkkk:                           \n                           ;dxxxxddoddxxxxxxxxxxxxdooodddooodxxddxxxxxdddddddxdolc:,...''''.....,,.................'.............:oddddddddddxddddoooooddxxxxxxxxxxxddddxkkk:                           \n                           ;dxxxxdooodxxxxxxxxxxxxdooodxxdddddddxkkkxxddddddxkkxdoolc,..........,'...............................:ddddddddddddddddddddoddxxxxxxxxxxxddddxkkk:                           \n                           ;dxxxddooodxxxxxxxxxxxxdooodxxxxdddxkkkOOkxxdddddxkkkkxdoo:,,........,................................:dddddddddddddddddddddddxxxxxxxxxxxddddxxkk:                           \n                           ,oddddooooddddxxxxxxxxddooodxxxxdddxkkOOOkxxxddddxkkkkxdol:;,........,'...............................;odxxdddddddddddxxdddddddxxxxxxxxxxdddddxkk:                           \n                           ,oddddooooddddddddddddddooodxdddddddxxkOkkxddddddxkkkxdool:,........',,...............................,ldddddddddddddddddddddddddxxxxxxxxdddddxxx:                           \n                           ,oddxdoooddxxxxxxxxxxxxdoooddoooddddddxkkkdddddddxkxdoooo:,.........',,...............................'cddddddddddddddddddddddddddddxdddddddddxxx;                           \n                           ,oddddooodxxxxxxxxxxxxxdoooooooddxxxddddxdddddooodddooodo;'.........';,................................;odddddddddddddddddddddxxxxxxxxxxxxddodxxx;                           \n                           ;oddddooodxxxxxxxxxxxxxdooooooodxxxxxddodddoooooooooodddl,..........,;,...............''...............;odddddddddddddddddddddxxxxxxxxxxxxdddddxd;                           \n                           ;odddooooddxxxxxxxxxxxxdooooooddxxxxxdddooooooooooodddddc'.........',;,'...............................,ldddddddddddddddddddddxxxxxxxxxxxxddoodxd;                           \n                           ;odddoooodddxxxxxxxxxxdoooodddddddddddddoooooooooddddxddc'.........,;;:;...............................,lddddddddxxxddddddddddxxxxxxxxxxxxxddoddd;                           \n                           ;odddooooddddxxxxxxxxxdoooodddddddddddddoooooooodddxxddo:'........';::cc,..............................'cddddxxxxxxxxxdddddddddxxxxxxxxxxxxddoddd;                           \n                           ,oooooooooooododddddddooooooooooddddddoooooooooooddddddo:,........,:::cc:,.............................'cddddxxxxxxxxxdddddddddxxxxxxxxxxxxddoddd;                           \n")
        time.sleep(0.05)
        clear()
        print(colorama.Fore.BLUE + colorama.Style.BRIGHT + "                           ;xxxxxxxxxxxxxxxxxxxxxxxxkkkkkkkkkkOkkkkkkkkxddddddddddxxxxxxxxxxxxxxxddooooodddxxxxxxxxxxxxddddoooooooddxxdddooddddxxxxxxxxxxxxxxxxxdddooddddddd;                           \n                           ;xxxxxxxxxxxxxxxxxxxxxxxxxxxxkkkkkkkOOOOOOkkxdddddddddxkkkkkkkkkkkxxxxxxdddoddxkkkkkkkkkkxxxxxddooooooooddxxxxxdddxxxxxxxxxxxxxxxxxdddddooodddddd;                           \n                           ;xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxkkkxxddddddxxxxkkkkkkxxxddxdddddddooodddxxxxkkkkkkkkkxxxdooooooooodxxxkkkkkkkkxxxxxxxxxxxxxxxxdddooodddddd;                           \n                           ;xxxxxxxxxxxxxxxxxxxxxkkkkxxkkkkkxxxxxxxdddddxxxxxxxxxxxxxxdddddddooooooollccc:::ccloddddxxxxxxxdooooooooodxxxxxxxxxkkxxxxxxxxxxxxxxxxddooodddddd;                           \n                           ;xxxxxxxxxxxxxxxxxxkkOOOkxxkOOOOkkkkkkxxxxxxxxxxxxxxxxxddddddddxdddoool:;,,,,,,,'',,:clodddddddddoooooodooooddddddxxxxxxxxxxxxxxxxxxxxddooddddddd;                           \n                           ;xxxxxxxxxxxxxxxxkkOOOOkxxxkOOOOOOOOOOOOkkkkkxxxxxxxxxxkxxxxddddddddooc;''''.''''''',,;coddddooooooooooooooooddxxxxxkkkOOkxxkkkkxxxxdddoooddddddd;                           \n                           ;xxxxxxxxxxxxkkOOOOOOkxxxxxkOOOOOOOOOOOOOOOOOkxxxxxxxxkOOkkkxxdddddddl:;,','''',,,,,,,,,cddxxxdddoooooooddddxxkkkkkkOOOOOkxxkOOOkxxdddooooddddddd;                           \n                           ;dxxxxxxxxxxkkOOOOOOkxxxkkkOOOOOOOOOOOOOOOOkkxxxxxxxxxkkkkkkkxxddxxdlccc::ccccclllllc;,,cdkkxxxddooooooddxxkkkkkkkOOOOOOOkkxxkOOkxdddoooooddddddd;                           \n                           ;xxxxxxkkkkxxxkkkOOkkxxkOOOOOOOOOOOOOOkkxxxxkkkxxxxkkxxxxxxxxxdddddc:clccccllllooooolc;,cdxxxdddooooooooodxxxkkkkkkkOOOOOkxxxxxxxxxxxdddoddddxxxd;                           \n                           ;xxxxkkOOOOkkxxxxkkxxxxkOOOOOOOkkkkkkxxxxxxkkkkxxxxkkkxxxxxxxxxdddoc:clc:::clllllooooc;;coddoooodddooooooooddddxkkkkkOOOOOOkxxdddxxxxxxdddddxxxxd;                           \n                           ;xxkOOOOOOOOOkxxxxxxxkOO000OOOkkxxxxxxxxxkkOOOkxxxxkkxxxxkkkkkkkxddollc:;;;::clccccllc::oddooooodxdoooodddoooooddxkkkkOOOOOOkxddddxxxxddddxxxxxxd;                           \n                           ;xkOOOOOOOOOOkkxxxxxkO00000OkkxxxxkkxxxxxkOO0OkxxxxxxxkkkOOOOOOOkxdodoc::::::cllccclllclxkxxxdoooddooooodxdddooooddddxkOOOkkkxddddddddddxxkkkkxxx;                           \n                           ;xOOOOOOOOOOOOOkkxxxkOOOOOkkxxxxkOOOOkkxxkO00OkkkxxxkkOOOOOOOOOOkxoldoccccc::cloooooollodkkkkxddooooooodxxxxdoooodddddxxkkkkkkxdddddddxxkOOOOkkkx;                           \n                           :kOOOOOOOOOOOOOOkkxxxkkxxxxxxxxkOOOOOOOkkkkO0OkkkxxxkO0000OOOOOOkkdooocccc:::cllooooolldxkkxkxxxddooooodxxkxdooddxxddddddxxkkkkxdddddxxkOOO000OOk:                           \n                           :kOOOOOOOOOOO0OOkxxxxxxxxxxxxxxkOOOOOkkkxkkkkkkxxxxxkkO000OOOOOOkkxxxdlc::::cllooooooodxxkxkkxxxddoooooodxxdodddxxxxddooooddxxkxdddxxkOOOO000000Oc                           \n                           :kOOOOOOOOOO00OkxxxxxxxxkkOkkxxxxkkOkxxxkOOkxxxxxxxxkO0000OOOOkkkkkkkdlc:::::clllllodxxxxxkkxxxxdoooooooodooooddxxxxxdddoooooddddddxkOOO00000000Oc                           \n                           :kOOOOOOOOOOOOOOkxxkkOkxxkkOkxxxxxxxxxxkOOOOkkxxxxxxkOOOOOOOOOOkkkxxxdolcccccllllllldxxxxkkxxxxxxdooooooooddddoddxkxxdddddddddddddxxkO00000000000c                           \n                           :kOOOOOOOOOOOOOkxxxkOOOxxxxxxxxkkxxxxxkOOOO0OkxxxxxxxxxkOOOOOOkkxxddoolccc:::ccllllloloxxxxxxxxdddooooooodxxxxdddxxxdddddxxxdddxxxxxkOO000000000Oc                           \n                           :kOOOOOOOOkkkkxxxxkOOOOkkxxxxxkOOOkkxxkOOOO0OkxxxxkkkxxxkkOOOOkxddddddoc:::::ccllllol;,;coxxxxddoddooooodxxxxxxxddddxddddxddddxkkxxxkOO000000000Oc                           \n                           :kOOOOOOkkxxxxxxxxkkkkkkkkxxxxkOOOOOkxkOOOOOOkxxxxkOOkxxxxxxxxxddddddolc:::cccllllodc,...,;ccllloooooooodxxxxkkxdxkkkxxdoooodxkOOkxxkkOO00000000Oc                           \n                           ;xkkOOkkxxxxxxxxxxxdxxxxxxdddxkkOOOOkxxkOOOOkxxxxxxkxxxxxxxddooddddxxoc:cc:cccccloddc'......'',,,,;;::clloxxxxxddxkkkkxddoddxkOOOkxxxxkkkOO0000OOc                           \n                           ;dxxkkxxxxxxxxxxxxxxxxxxddxxxddxkkOOkxxkOOOkkxdddxxxxxxkkkkkxdoollodxdlcccclc:clddxo;'.................'',cdxxxddxkkkkxdooodxxxxxxxxxxxxxxkO000OOc                           \n                           ;xxdxddxxkkkkkkkkkkkkkkxdxxkkxddxkkkkkxxkkkkxdddddddxxkOOkxxol:;,;cdddocccccclodxdl;'.....................'cdxddxkkkkxdooooooddddddddxxxxxxkOO00Oc                           \n                           ;dddddxxkkkkkkkkkkOkkkxddxkkkxxddxkkkxddxxxxxddddddxkkkkxoc:,''..,cddol:::::lodddl,........................;oxddxkxkxdooddoooddxxxxdxxxxxxxxkkOOk:                           \n                           ;dddddxxkkkkkkkkkkkkkxdddxkkkxxdddxxxxxxxxddddddddxkkxoc:,'.......;::cc:::::cccc:,.........................':odddxxxdooddxddodxxkkkkkkkOOOkkkxxxx;                           \n                           ;dddddxxkkkkkkkkkkkkkxdddxxxxddddddddxkkkkkxdddddddxxc,'............'::;;;;:c::;,...........................':odddddoodxxxxdooddxkkkkkkOOOOOkkxxx;                           \n                           ;ddddxxkkkOOkkkOkkkkxxddddddddddddddxkkkOOOkxdddddddo:'.............':::;:::::;,'............................;oddddooooddxxxdoodxxkkkkkkOkOOOkxxx;                           \n                           ;ddddxkkkkkkkkkkkkxxdddddxxxxxddodddxkkOOOOkxdddddddo:..............';::cc:::;;'..............................;lddddooooooddooodxxkkkxxkkkkOkxxxx;                           \n                           ;dddxkkkkkkxxxxxddddddddxkkxxxdddddddxkkkkkkxdddddddo:..............';:cllc:;;,'...............................,ldddoooddddddooddxxxkxxkkkkkOkkxx;                           \n                           ;ddddxdddxxxxxddddddxxxxkkkxxdddddddddxkkkOkxddddddddc'.............';:lool:;;'.................................';:looodxxkxdddoodddddddxxkkOOkkx;                           \n                           ;ddddddddxxxxxxxdddxxkkkkkkxxdodxxdddddxkkkkdddddddxxl'.............',:lool;,,......''''...........................':lodxkkkkxxddoooooooddxkkOOkx;                           \n                           ;odddddxxkkkkkkxdddxkkkkkkxxdddxxxxddddxkkkkxddddddxxl'.............',;:cc:,,'..';ccccc:::,..........................',:oxkkOOOkxdooooooooddxxxxd;                           \n                           ;odddxxkkkkkkkkxddddxxkkkxxxdddxxxxxddddxkkkxddddddxxl'..............,,;;;;,'...';ccccccccc:,...........................'cxkOOOkkxdddxxxxxxxxxxxd;                           \n                           ;oddxkkkkkkkkkkxdddddxxkkkxdddxxxxdddxxxdxkkxddddddddl,..............',;;;,,'....';::cccccllc;'..........................;dkkkkOkxddxxkxxxkkkxxxd;                           \n                           ;oddxxkkkkkkkkkxdoodddxkkxxddxxxdddddxkxdxkxxddddxxxdl;..............',;;;,'......';::cccclllc;..........................;oxkkkxxdddxkkkxxkOOOkkx;                           \n                           ;oddddxkkkkkxxdddddddddxxxdodxxddddddxxkxxxxxddddxkkxo:'.............',;;,,'........',,;::cllc;'.........................,lxkkkxddddxkkkxxkkOOOOx;                           \n                           ;ddddddxkkxxdddddxxxxdoodddoddoodxxkkxxxxdxddddddxxxdoc,............'',;;,,'..............,;:;,..........................'lxkkxxdddddxxxxkkkOOkkx;                           \n                           ;xxxdddddddddddxkkkkkxdoooooooodxkkkOOkxxxddxxddddddddd:......,'....'',;;,,........................'''...................'cdxddxxkxxdddddxxkkkxxd;                           \n                           ;dxxxxxdddddxxxkkkkkkxxdoooodddxkkkkOOOkxxxxxxddddddxxxc,....,;,....',,;;;,........................',,'.................':oooddxkkkkxdddoddxxxxxx:                           \n                           ;ddxddddddddxxxxxxxxxxxddooddxxxxkkkkkkOkkxxxxddddxxkxo:,'...,,.....',;;;,'.........................................',;cloooodxkkkkkkxddoooddxxkk:                           \n                           ;dxxxxxdddddxxxxxxxxxxddoooddxxxxkkkkkkOkkxxxdddddxkxxol:;'..''.....',,;,,'......................  ...,::::;:::clllooddddoooddxxxxxxxxxddoodxxkkk:                           \n                           ;dxkxxxddddxxkkkkkkkkkxxdoooddxxkkkkOOOkkxxxxdddddxxxdl:;,............',,'............................;oddddddxxxxxxxxxxdoooodddxxxxxxdddooddxxxx:                           \n                           ;dxxxxxddddxxkkkkkxkkxxdooooooodxkkOOkxxxxxxxdddddollc::;,............',,.............................;oddddddddxxxxxxxdooooodxxxxxxxxxxdooddxkkk:                           \n                           ;dxxxxdddddxxxxxxxxxxxxdoooooooddxkkkxxxxxxxxddddolccllc:;'...........','.............................,ldddddddddxxxxdooooooodxxxxxxxxxxddoddxkkk:                           \n                           ;dxxxxdddddxxxxxxxxxxxxdooodddooodxxddxxxxxxddddddocccllc;'...........','.............................'cddddddddddxddddoooooodxxxxxxxxxxdddddxkkk:                           \n                           ;dxxxxddoodxxxxxxxxxxxxdooodxxddoodddxkkkxxxdddddxxl::cc:;,,;;.....'',,,'..............................:oddxdddddddddddddddoddxxxxxxxxxxxddddxxkk:                           \n                           ;dxxxddooodxxxxxxxxxxxxdooodxxxxdddxxkkOOkxxxddddxxl:;:::codd:.....,;;;;'..............................,ldddddddddddddddddddddxxxxxxxxxxxdddddxkk:                           \n                           ,oddddoooodddxxxxxxxxxddooddxxxxdddxkkOOOkxxxddddxkxdoooooddo;.....,;;;,'...............................;oddddddddddddxddddddddxxxxxxxxxxdddddxkx:                           \n                           ,oddddoooodddxddxddddddoooddxdddodddxxkOOkxxdddddxkkkxddooodl'....';:;;,'...............................,ldddxddddddddddddddddddddxxxxxxxdddddxxx;                           \n                           ,oddxdoooddxxxxxxxxxxxxdoodddoooodddddxkkkxddddddxkxddoooooo:'....';:;;,'...............................'cdddddddddddddddddddddddddxxddddddddddxx;                           \n                           ,oddddooodxxxxxxxxxxxxxdoooooooddxxxdddxxxddddddddddoodddddl,.....'::;;,'................................:odddddddddddddddddddxxxxxxxxxxxdddddxxx;                           \n                           ;oddddooodxxxxxxxxxxxxxdooooooddxxxxxdddddddoooooooooddxdddc,.....':::;;'................................,ldddddddddddddddddddxxxxxxxxxxxddddddxd;                           \n                           ;odddooooddxxxxxxxxxxxxdoooooddxxxxxxdddooooooooooodddxxddoc,.....,::::;,'...............................'cddddddxxdddddddddddxxxxxxxxxxxxdddddxd;                           \n                           ;odddoooodddxxxxxxxxxxdoooodddddddddddddooooooooodddddddxdl:'.....,:c::;,,'...............................:ddxxxxxxdddddddddddxxxxxxxxxxxxxddddxd;                           \n                           ;odddoooodddxxxxxxxxxxdoooodddddddddddddoooooooooddxdxxddoc,......,:cc:;;;'...............................;odddxxxxdddddddddddxxxxxxxxxxxxxxddddd;                           \n                           ,oooooooooooododddddddooooooooooddddddoooooooooooddddddddo:'......,:cc:;;;,...............................,ldddxxxxxxddddddddddxxxxxxxxxxxxxddddo;                           \n")
        time.sleep(0.05)
        clear()
        print(colorama.Fore.MAGENTA + colorama.Style.BRIGHT + "                           :xkxxxxkkkxxxxxxxxxxxxxxkkkkkkkkkkkOOkkkkkkkxddddddddddxxxxxxxxxxxxxxxdddoodddddxxxxxxxxxxxxddoooooooooddxxxddoodddxxxxxxxxxxxxxxxxxdddoooddddddd;                           \n                           :xkxxxxxxxxxxxxxxxxxxxxxxxxxxkkkkkkOOOOOOOkkxdddddddddxkkkkkkkkkkkkxxxxxxddddxxkkkkkkkkkkkxxxxddooooooooddxxxxxdxxxxxxxxxxxxxxxxxxxddddoooddddddd;                           \n                           :xkkkxxxxxxxxxxxxxxxxxxxxxxxxxkkxxxxxxxkkkxxddddddxxxxkkkkkkxxxdxxxdddddddddddxxkkkkkkkkkkkkkxxdooooooooodxxxkkkkkkkkxxxxxxxxxxxxxxxddddooddddddd;                           \n                           :xkxxxxxxxxxxxxxxxxxxxkkkkxxkkkkkxxxxxxxdddddxxxxxxxxxxxxxxdddddddddoodddxxxxxddxxxxxxxxxxkkkxxxdooooooooodxxxkkxxkkkkkxxxxxxxxxxxxxxxddooddddddd;                           \n                           :xxxxxxxxxxxxxxxxxxkkOOOkxxkOOOOkkkkkkxxxxxxxxxxxxxxxxxddddddddxddddddxkkkOOOkkkxxxxxxxxxdddddddddoooooddooddddxdxxxxxxxxxxxxxxxxxxxxdddooddddddd;                           \n                           :xxxxxxxxxxxxxxxxkkOOOOkxxxkOOOOOOOOOOOOkkkkkxxxxxxxxxxxxxxxdddddddddxkOOOOOOOOOkxxxxxxxxddddddoodooooddddoodddxxxxxkkOOOkxkkkkkxxxxdddoodddddddd;                           \n                           ;xxxxxxxxxxxkkkOOOOOOkxxxxxkOOOOkOOOOOOOOOOOOkxxxxxxxxkkOkkkxxdddxxxkkkOOOOOOOOOOkxxxxxxxxxxxxxxddddddddddxxxxkkkOkkOO00OOkkkOOOkxxddddoodddddddd;                           \n                           ;xxxxxxxxxxxkkOOOOOOkxxxkkkOOOOOkOOOOOOOOOOkkxxxxxxxxxkkkkkkkxxddxkkOOOOOOOOOOOOOOOkkxxxxkkkkkxxddddddddxxkkkkkkkOOOOO00OOkxxkkOkxdddddoddddxxddd;                           \n                           ;xxxxxxkkkkxxxkkOOOkkxxkOOOOOOOOOOOOOOkkxxxxxkkxxxxkkkxxxxxxxxddddxkkkkOOOOOOOOOOOOOkxxxxkkxxxxdddddddddddxkkkkkkkOOOOOOOkkxxxxxxxxxxdddddddxxxxd;                           \n                           ;xxxkkkOOOOkkxxxxkkxxxkkOOOOOOOkkkkkkxxxxxxkkkkxxxxkkkxxxxxxxxxdddddxxkkOOOOOOOOOkkxxxxxxddddddddxddddddddddddxxkkOOOOOOOOOkxxdddxxkkxxxdddxxxxxd;                           \n                           ;xxkOOOOOOOOOkxxxxxxxkOO000OOOkkxxxxxxxxxkkOOOkxxxxkkxxxxkkkkkkkxddddxkkOOOOOOOOkxxxxxkkxxxddddddxddddddddddddddxxkkkOOOOOOOkxddddxxkxxxddxxxxxxx;                           \n                           :xkOOOOOO0O0OkkxxxxxkO00000OkkxxxkkkxxxxxkOO0OkxxxxxxxxkkOOOkkxxdollclodxxkkOOkxxxxxxkkOkkkkxddoddddddddxxxdddddddddxkkOOOOOkxdddddddddxxkkkkkxxx;                           \n                           :kOOOOOOOOOOOOOkkxxxkOOOOOkkxxxxkOOOOkkkxkO00OkkkkkxkkOOOOkxdolc:;,,,,;:ccclodxxxxkkkkkkkkkkkxddddddddddxkkxdddddddddxxkkkOkkkxdddddddxxkOOOOOkkx:                           \n                           :kOOOOOOOOO0OOOOkkxxxkkxxxxxxxxkOOOOOOOkkkkO0OkkkkxkkO00Okdl:;;,,,,''',,,,,,;cdkkOkkkkkkkkkkkkkxxdddddddxkkxdddddxxxdddddxkkkkkxddddxxxkO00000OOk:                           \n                           :kOOOOOOOO0000OOkxxxxxxxxkxxxxxkOOOOOkkkxkkkkkkkkkxkkOO0Okoc;''''',,,,;;;,,'';lkOkkkkkkkkkkkkkkkxdddddddxxxddddxxxkxxdddddddxxkkxdxxkkOOO0000000Oc                           \n                           :kOOOOOOOO0000OkxxxxxxxxkkOkkxxxxkOOkxxxkOOkkkkxxxxkkO00Oxoc;;;;;;:clllollc;,,cxkkkkkkkkkkkkkkkxxddddooddddddddxxkkkxxxdddddddddddxkOOO000000000Oc                           \n                           :kOOOOOOO00000OOkxxkkOkxxkkOOkxxxxxxxxkkOO0OOkkkkxxkkOOOOxoccccclllllooooooc;,:oxxxxkkkkkkkkkkkkxddooooooddxxdddxkkkxdddddxxddddxxxxkO00000000000c                           \n                           :kOOOOOOOO0OOOOkxxxkOOOkxxxkxxkkkkxxxxOOOO00Okxxxxkkxxxkkdc:ccccclllloooooolc;:lddddxxkkkkkkkkxxdddooooodxxkkxxdxxxxddddxxkxxdxxxxxxkO00000000000c                           \n                           :kOOOOOOOOOkkkxxxxkOOOOkkxxxxxkOOOOkxxkOOO00Okxxxxkkkxxxkxlccc:::cclcccllllll:codddoddxkkOOkkxddooddoooddxkkkkkxxdxxxxdddxxddxkOkxxkkO0000000000Oc                           \n                           :kOOOOOOOkxxxxxxxxkkkkOOkkxxxxkOOOOOkxkOOOOOOkxxxxkOOkxxxxdllc::::clllcclloolclodddddddxkkkkxddddddddddddxkkkOkkxxkkkkxddddddxOOOkxxkOO000000000Oc                           \n                           ;xkOOOOkxxxxxxxxxxxxxxxxxxxxxxkOOOOOkxxkOOOOkxxxxxkkkxxxxxddoc::::clolllooooollodxxxxxdxxxdddddddxxddododxkkkOkxxkOOOkkxdddxkOOOOOkxxkkkOO000000Oc                           \n                           ;dxxkkxxxxxxxxxxxxxxxxxxxxxxxdxxkkOOkxxkkOOOkxxxxxxxxxkkkkxdolc::::cloooooooolodxkkxkkxxxxxxxddoooddoododxkkkkkxkkOOOkkxdddxxkkkkkkxxxxxxkOO0000Oc                           \n                           ;xxxxxxxxkkkkkkkkkkkkkkxxxxkkxddxkkkkkxxkkOkxxddddxxxkOOOOkddocc:::cllccllloloxkkkkkkxxdxkkkkkxddoooooooddxkkkxxkOOOOkxdddddddddxxxxxxxxxxkkO000Oc                           \n                           ;xxdddxxkkkkkkkkkkOkkkxxdxkkkxxddxkkkxddxxxxxdddddxkkOOOOkkxdol:::::cc:::cloloxkxdddddddxxxkkkkxxdooooooodxkkxxxkOOOkxddddddddxxkkxxxxkkkkxkkkOOk:                           \n                           ;dddddxxkkkkkkkkkkkkkxddxxkkkxxdddxxxxxxxxddddddddxkOOOOOkddddol:::ccc:::cloloxxddooddddddddxxxxxxxdooooodddddddxkkkxdddxxxdddxkkkkkkkkOOOOkkkkkx:                           \n                           ;dddddxxkkkkkkkkkkkkkxdddxxxdddddddddxkkkkkxxddddddxkOOkxddddxxdl::cc::::cloooddoooddxxxxdoodxxxxxxdooooooooddddddxddddxkkkxdddxkkkkkkOOOOOOOkxxx:                           \n                           ;xxddxkkkOOOkkkOkkkkxxddddddddddddddxkkkOOOkxxddddddxxkxddddxxxxoc::c:::ccllllool::lodxxxddooddxxxdoooooooddxxxdoooooddxxkkxddddxkkkkkkOOOOOOkxxx:                           \n                           ;dddxxkkkOkkkkkkkkxxddddddxxxxddddddxkkOOOOkxxdddxxdddddddddxxxxdc::::ccccllllloc,.'',;:ccllloodddddooooodxxxxxxdoooodddddddddddxkkkkkkkkOOOOkxxx:                           \n                           ;dddxkkkkkkxxxxxddddddddxkkxxxdddddddxkkkkkkxddddddddddddxxxxxxxoc:::clllcllccodl,.........'',,;:clloooooddxxxxxdooooddxxxxdddddxxkkkkkkkkkOOOkxx:                           \n                           ;ddddxxxxxxxxxdddddddxxxkkkxxdddddddddxkkkOkxddddddxxxdddxxdollddc:::coolcc:cldxl,.................',:lodddxxxxdoooooddxkkkkxddddddxxxxxxkkOOOOkx;                           \n                           ;dddddddxxxxxxxxdddxxkkkkkkxxdodxxdddddxkkkkddddddxxkkxdool:;,:oddl::lool::codddc'....................,ldddxxxxdooodxddxkOOOOkkxddddddddddxkOOOkx;                           \n                           ;ddddddxxkkkkkkxdddxkkkkkkxxdodxxxxddddxkkkkxddddddxxxoc:,'...,ldddollollclddddl,......................;odxxxxdooodxkxdxkOOOOOOOkxdddddddddxxxkxx;                           \n                           ;oddxxxkkkkkkkkxddddxxkkkkxddddxxkxxddddxkkkxdddddool:,'......'cooooolccloodddo:'......................'cdxxxdoooodxkkxxxkOOOOOOOkxdxxxxxxxxxxxxx;                           \n                           ;odxxkkkkkkkkkkxddoodxxkkkxdddxxxxdddxxddxkkxdddlc:,'..........,;;;::::::::cll:,........................:ddxddooodxkkOkxxkOOOOOOOkxxxkkkkkkkkkxxx;                           \n                           ;oddxxkkkkkkkkkxdoooddxkkxxdddxxdddddxkxdxxxdddo:'................';::::::::::;,........................;odddooddddxkOOkxxkOOOOkxxdxxkkkkkkOOOOkx;                           \n                           ;dddddxkkkkkxxdddddddddxxxdodxxddddddxxxxdxxdddl,..................,::::::::::;,........................'ldddodxddddxkOkxxxkOOOkxdxxxkkkkkkOO0OOk:                           \n                           ;ddddddxkkxxdddddxxxxdooddooddoodxxkkxxxddddddoc,..................,;:::::::::;'.........................;oddddddddddxkkxxxkOkkxxxxxxxxxkkkOOOkkx:                           \n                           ;xxxdddddddddddxkkkkkxdoooooooodxkkkOOkxddddddoc,...................;::::;;;;;;'.........................'cddoodxxxxddddddxxxxxxkkkxxddddxkOOkxxx:                           \n                           ;dxxxxxdddddxxxkkkkkkxxdoooooddxkkkkOOOkxxddddoc'...................,;;;;;;;;;,'..........................,ldodxkkkkkxddddddddxkOOOkkxdddddxxxxxk:                           \n                           ;dxxdxxdddddxxxxxxxxxxxddooodxxxxkkkkkkkkxxdddo:'....................,;;;;;;;,,'...........................;odxxkkkkkkxxdddddxxkkOOkkkxdooodxxxkkc                           \n                           ;dxxxxxdddddxxxxxxxxxxddoooddxxxxkkkkkkOkkxdddo;.....................,;;;,,,,,,'...........................':ddxxxxxxxxxdddddxxxxxxxxxxddoodxxkkk:                           \n                           ;xxkkkxddddxxkkkkkxkkkxddoooddxxkkkOOOkkkxxdddo;.....................',;,,,,,,''............................'ldxxxxkkxxxdoooddxxxxxxxxxddooddxxkx:                           \n                           ;dxxxxxddddxkkkkxxxxkxxdooooooodxkkOOkxxxdddddo:'.....................,;,,,,,,''.............................,oxxxxxkxxddoooodxxxxxxxxxxdooddkkOk:                           \n                           ;dxxxxdddddxxkxxxxxxxxxdoooooooddkkkkxxxxxddddoc'.....................,;,,,,,,''..............................:ddxxxxdooooooodxxxxxxxxxxddoddxkkk:                           \n                           ;dxxxxdddddxxxxxxxxxxxxdooodddooodxxddxxxxdddddc,.........,::,........,;,,,,,,,'..............................,oddxdddooooooodxxxxxxxxxxddoddxkkk:                           \n                           ;dxxxxdddddxxxxxxxxxxxxdooodxxddoddddxkkkxxddddl,....';:cclll:'.......,;,,,;;,,'.................. ...........,lddddddddddooodxxxxxxxxxxxddddxkkk:                           \n                           ;dxxxxdddddxxxxxxxxxxxxdooddxxxxddddxkkkOkxddddc,....;cc:::ccc;.......,;,,,,,,,'..................  ..........,oddddddddddoooddxxxxxxxxxxddddxkkk:                           \n                           ,oddddoooodddxxxxxxxxxddooddxxxxdddxkkkOOkxddddc,..,;cc:;;::cl:'......,,,,,,,,,''.............................:ddxdddddxdddddddxxxxxxxxxxdddddxkk:                           \n                           ,odddddooddddxddxdddddddooddxddoodddxxkOkkxdddoc;',,,,;;;;;:cc;'......,,,,,,,,,''............''..............,lddddddddddddddddddxxxxxxxddddddxxx:                           \n                           ,oddxdoooddxxxxxxxxxxxxdoodddoooodddddxkkxxdddoc,.''..',;;;::;........''',,,,,,,''.........';::::::;'.......,ldxddddddddddddddddddddddddddddddxxx;                           \n                           ,oddddooodxxxxxxxxxxxxxdoooooooddxxxddddxddddool;'......',,'..........''',,,;,,'''.........';;::cccc;'.....'cddxxdddddddddddddxxxxxxxxxxxdddddxxx:                           \n                           ;oddddooodxxxxxxxxxxxxxdooooooddxxxxxddooddoooooc,............  ......''.'',,,''............,;;:cclc:,.....,ldxddxddddddddddddxxxxxxxxxxxddddddxd;                           \n                           ;odddoooodxxxxxxxxxxxxxdoooooddxxxxxxdddoooooooooc,'........... ......'....'''............ ..,;;:clc:,....'cdxxxxxxxxdddddddddxxxxxxxxxxxddddddxd;                           \n                           ;odddoooodddxxxxxxxxxxdoooodddddddddddddoooooooodoolllcc;,............'....'........'.....  ..';:ccc,...',cddxxxxxxxxdddddddddxxxxxxxxxxxxxddddxd;                           \n                           ;odddoooodddxxxxxxxxxxdoooodddddddddddddoooooododdxxxxdddo:...........'..'',,;::;;;;;,'.........'','...,codxxxxxxxxxxxddddddddxxxxxxxxxxxxxdddddd;                           \n                           ;oooooooooooddoddddddddoooooodddddddddoooooooooddddddddddd:...........'.',;::cllcc:::;,................;odxxxxxxxxxxxxddddddddxxxxxxxxxxxxxxddddd;                           \n")
        time.sleep(0.05)
        clear()
        print(colorama.Fore.WHITE + colorama.Style.BRIGHT + "                           ;xxxxxxxxxxxxxxxxxxxxxxxxkkkkkkkkkkOkkkkkkkkxddddddddddxxxxxxxxxxxxxxxddooooodddxxxxxxxxxxxxddddoooooooddxxdddooddddxxxxxxxxxxxxxxxxxdddooddddddd;                           \n                           ;xxxxxxxxxxxxxxxxxxxxxxxxxxxxkkkkkkkOOOOOOkkxdddddddddxkkkkkkkkkkkxxxxxxdddoddxkkkkkkkkkkxxxxxddooooooooddxxxxxdddxxxxxxxxxxxxxxxxxdddddooodddddd;                           \n                           ;xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxkkkxxddddddxxxxkkkkkkxxxddxdddddddooodddxxxxkkkkkkkkkxxxdooooooooodxxxkkkkkkkkxxxxxxxxxxxxxxxxdddooodddddd;                           \n                           ;xxxxxxxxxxxxxxxxxxxxxkkkkxxkkkkkxxxxxxxdddddxxxxxxxxxxxxxxdddddddooooooollccc:::ccloddddxxxxxxxdooooooooodxxxxxxxxxkkxxxxxxxxxxxxxxxxddooodddddd;                           \n                           ;xxxxxxxxxxxxxxxxxxkkOOOkxxkOOOOkkkkkkxxxxxxxxxxxxxxxxxddddddddxdddoool:;,,,,,,,'',,:clodddddddddoooooodooooddddddxxxxxxxxxxxxxxxxxxxxddooddddddd;                           \n                           ;xxxxxxxxxxxxxxxxkkOOOOkxxxkOOOOOOOOOOOOkkkkkxxxxxxxxxxkxxxxddddddddooc;''''.''''''',,;coddddooooooooooooooooddxxxxxkkkOOkxxkkkkxxxxdddoooddddddd;                           \n                           ;xxxxxxxxxxxxkkOOOOOOkxxxxxkOOOOOOOOOOOOOOOOOkxxxxxxxxkOOkkkxxdddddddl:;,','''',,,,,,,,,cddxxxdddoooooooddddxxkkkkkkOOOOOkxxkOOOkxxdddooooddddddd;                           \n                           ;dxxxxxxxxxxkkOOOOOOkxxxkkkOOOOOOOOOOOOOOOOkkxxxxxxxxxkkkkkkkxxddxxdlccc::ccccclllllc;,,cdkkxxxddooooooddxxkkkkkkkOOOOOOOkkxxkOOkxdddoooooddddddd;                           \n                           ;xxxxxxkkkkxxxkkkOOkkxxkOOOOOOOOOOOOOOkkxxxxkkkxxxxkkxxxxxxxxxdddddc:clccccllllooooolc;,cdxxxdddooooooooodxxxkkkkkkkOOOOOkxxxxxxxxxxxdddoddddxxxd;                           \n                           ;xxxxkkOOOOkkxxxxkkxxxxkOOOOOOOkkkkkkxxxxxxkkkkxxxxkkkxxxxxxxxxdddoc:clc:::clllllooooc;;coddoooodddooooooooddddxkkkkkOOOOOOkxxdddxxxxxxdddddxxxxd;                           \n                           ;xxkOOOOOOOOOkxxxxxxxkOO000OOOkkxxxxxxxxxkkOOOkxxxxkkxxxxkkkkkkkxddollc:;;;::clccccllc::oddooooodxdoooodddoooooddxkkkkOOOOOOkxddddxxxxddddxxxxxxd;                           \n                           ;xkOOOOOOOOOOkkxxxxxkO00000OkkxxxxkkxxxxxkOO0OkxxxxxxxkkkOOOOOOOkxdodoc::::::cllccclllclxkxxxdoooddooooodxdddooooddddxkOOOkkkxddddddddddxxkkkkxxx;                           \n                           ;xOOOOOOOOOOOOOkkxxxkOOOOOkkxxxxkOOOOkkxxkO00OkkkxxxkkOOOOOOOOOOkxoldoccccc::cloooooollodkkkkxddooooooodxxxxdoooodddddxxkkkkkkxdddddddxxkOOOOkkkx;                           \n                           :kOOOOOOOOOOOOOOkkxxxkkxxxxxxxxkOOOOOOOkkkkO0OkkkxxxkO0000OOOOOOkkdooocccc:::cllooooolldxkkxkxxxddooooodxxkxdooddxxddddddxxkkkkxdddddxxkOOO000OOk:                           \n                           :kOOOOOOOOOOO0OOkxxxxxxxxxxxxxxkOOOOOkkkxkkkkkkxxxxxkkO000OOOOOOkkxxxdlc::::cllooooooodxxkxkkxxxddoooooodxxdodddxxxxddooooddxxkxdddxxkOOOO000000Oc                           \n                           :kOOOOOOOOOO00OkxxxxxxxxkkOkkxxxxkkOkxxxkOOkxxxxxxxxkO0000OOOOkkkkkkkdlc:::::clllllodxxxxxkkxxxxdoooooooodooooddxxxxxdddoooooddddddxkOOO00000000Oc                           \n                           :kOOOOOOOOOOOOOOkxxkkOkxxkkOkxxxxxxxxxxkOOOOkkxxxxxxkOOOOOOOOOOkkkxxxdolcccccllllllldxxxxkkxxxxxxdooooooooddddoddxkxxdddddddddddddxxkO00000000000c                           \n                           :kOOOOOOOOOOOOOkxxxkOOOxxxxxxxxkkxxxxxkOOOO0OkxxxxxxxxxkOOOOOOkkxxddoolccc:::ccllllloloxxxxxxxxdddooooooodxxxxdddxxxdddddxxxdddxxxxxkOO000000000Oc                           \n                           :kOOOOOOOOkkkkxxxxkOOOOkkxxxxxkOOOkkxxkOOOO0OkxxxxkkkxxxkkOOOOkxddddddoc:::::ccllllol;,;coxxxxddoddooooodxxxxxxxddddxddddxddddxkkxxxkOO000000000Oc                           \n                           :kOOOOOOkkxxxxxxxxkkkkkkkkxxxxkOOOOOkxkOOOOOOkxxxxkOOkxxxxxxxxxddddddolc:::cccllllodc,...,;ccllloooooooodxxxxkkxdxkkkxxdoooodxkOOkxxkkOO00000000Oc                           \n                           ;xkkOOkkxxxxxxxxxxxdxxxxxxdddxkkOOOOkxxkOOOOkxxxxxxkxxxxxxxddooddddxxoc:cc:cccccloddc'......'',,,,;;::clloxxxxxddxkkkkxddoddxkOOOkxxxxkkkOO0000OOc                           \n                           ;dxxkkxxxxxxxxxxxxxxxxxxddxxxddxkkOOkxxkOOOkkxdddxxxxxxkkkkkxdoollodxdlcccclc:clddxo;'.................'',cdxxxddxkkkkxdooodxxxxxxxxxxxxxxkO000OOc                           \n                           ;xxdxddxxkkkkkkkkkkkkkkxdxxkkxddxkkkkkxxkkkkxdddddddxxkOOkxxol:;,;cdddocccccclodxdl;'.....................'cdxddxkkkkxdooooooddddddddxxxxxxkOO00Oc                           \n                           ;dddddxxkkkkkkkkkkOkkkxddxkkkxxddxkkkxddxxxxxddddddxkkkkxoc:,''..,cddol:::::lodddl,........................;oxddxkxkxdooddoooddxxxxdxxxxxxxxkkOOk:                           \n                           ;dddddxxkkkkkkkkkkkkkxdddxkkkxxdddxxxxxxxxddddddddxkkxoc:,'.......;::cc:::::cccc:,.........................':odddxxxdooddxddodxxkkkkkkkOOOkkkxxxx;                           \n                           ;dddddxxkkkkkkkkkkkkkxdddxxxxddddddddxkkkkkxdddddddxxc,'............'::;;;;:c::;,...........................':odddddoodxxxxdooddxkkkkkkOOOOOkkxxx;                           \n                           ;ddddxxkkkOOkkkOkkkkxxddddddddddddddxkkkOOOkxdddddddo:'.............':::;:::::;,'............................;oddddooooddxxxdoodxxkkkkkkOkOOOkxxx;                           \n                           ;ddddxkkkkkkkkkkkkxxdddddxxxxxddodddxkkOOOOkxdddddddo:..............';::cc:::;;'..............................;lddddooooooddooodxxkkkxxkkkkOkxxxx;                           \n                           ;dddxkkkkkkxxxxxddddddddxkkxxxdddddddxkkkkkkxdddddddo:..............';:cllc:;;,'...............................,ldddoooddddddooddxxxkxxkkkkkOkkxx;                           \n                           ;ddddxdddxxxxxddddddxxxxkkkxxdddddddddxkkkOkxddddddddc'.............';:lool:;;'.................................';:looodxxkxdddoodddddddxxkkOOkkx;                           \n                           ;ddddddddxxxxxxxdddxxkkkkkkxxdodxxdddddxkkkkdddddddxxl'.............',:lool;,,......''''...........................':lodxkkkkxxddoooooooddxkkOOkx;                           \n                           ;odddddxxkkkkkkxdddxkkkkkkxxdddxxxxddddxkkkkxddddddxxl'.............',;:cc:,,'..';ccccc:::,..........................',:oxkkOOOkxdooooooooddxxxxd;                           \n                           ;odddxxkkkkkkkkxddddxxkkkxxxdddxxxxxddddxkkkxddddddxxl'..............,,;;;;,'...';ccccccccc:,...........................'cxkOOOkkxdddxxxxxxxxxxxd;                           \n                           ;oddxkkkkkkkkkkxdddddxxkkkxdddxxxxdddxxxdxkkxddddddddl,..............',;;;,,'....';::cccccllc;'..........................;dkkkkOkxddxxkxxxkkkxxxd;                           \n                           ;oddxxkkkkkkkkkxdoodddxkkxxddxxxdddddxkxdxkxxddddxxxdl;..............',;;;,'......';::cccclllc;..........................;oxkkkxxdddxkkkxxkOOOkkx;                           \n                           ;oddddxkkkkkxxdddddddddxxxdodxxddddddxxkxxxxxddddxkkxo:'.............',;;,,'........',,;::cllc;'.........................,lxkkkxddddxkkkxxkkOOOOx;                           \n                           ;ddddddxkkxxdddddxxxxdoodddoddoodxxkkxxxxdxddddddxxxdoc,............'',;;,,'..............,;:;,..........................'lxkkxxdddddxxxxkkkOOkkx;                           \n                           ;xxxdddddddddddxkkkkkxdoooooooodxkkkOOkxxxddxxddddddddd:......,'....'',;;,,........................'''...................'cdxddxxkxxdddddxxkkkxxd;                           \n                           ;dxxxxxdddddxxxkkkkkkxxdoooodddxkkkkOOOkxxxxxxddddddxxxc,....,;,....',,;;;,........................',,'.................':oooddxkkkkxdddoddxxxxxx:                           \n                           ;ddxddddddddxxxxxxxxxxxddooddxxxxkkkkkkOkkxxxxddddxxkxo:,'...,,.....',;;;,'.........................................',;cloooodxkkkkkkxddoooddxxkk:                           \n                           ;dxxxxxdddddxxxxxxxxxxddoooddxxxxkkkkkkOkkxxxdddddxkxxol:;'..''.....',,;,,'......................  ...,::::;:::clllooddddoooddxxxxxxxxxddoodxxkkk:                           \n                           ;dxkxxxddddxxkkkkkkkkkxxdoooddxxkkkkOOOkkxxxxdddddxxxdl:;,............',,'............................;oddddddxxxxxxxxxxdoooodddxxxxxxdddooddxxxx:                           \n                           ;dxxxxxddddxxkkkkkxkkxxdooooooodxkkOOkxxxxxxxdddddollc::;,............',,.............................;oddddddddxxxxxxxdooooodxxxxxxxxxxdooddxkkk:                           \n                           ;dxxxxdddddxxxxxxxxxxxxdoooooooddxkkkxxxxxxxxddddolccllc:;'...........','.............................,ldddddddddxxxxdooooooodxxxxxxxxxxddoddxkkk:                           \n                           ;dxxxxdddddxxxxxxxxxxxxdooodddooodxxddxxxxxxddddddocccllc;'...........','.............................'cddddddddddxddddoooooodxxxxxxxxxxdddddxkkk:                           \n                           ;dxxxxddoodxxxxxxxxxxxxdooodxxddoodddxkkkxxxdddddxxl::cc:;,,;;.....'',,,'..............................:oddxdddddddddddddddoddxxxxxxxxxxxddddxxkk:                           \n                           ;dxxxddooodxxxxxxxxxxxxdooodxxxxdddxxkkOOkxxxddddxxl:;:::codd:.....,;;;;'..............................,ldddddddddddddddddddddxxxxxxxxxxxdddddxkk:                           \n                           ,oddddoooodddxxxxxxxxxddooddxxxxdddxkkOOOkxxxddddxkxdoooooddo;.....,;;;,'...............................;oddddddddddddxddddddddxxxxxxxxxxdddddxkx:                           \n                           ,oddddoooodddxddxddddddoooddxdddodddxxkOOkxxdddddxkkkxddooodl'....';:;;,'...............................,ldddxddddddddddddddddddddxxxxxxxdddddxxx;                           \n                           ,oddxdoooddxxxxxxxxxxxxdoodddoooodddddxkkkxddddddxkxddoooooo:'....';:;;,'...............................'cdddddddddddddddddddddddddxxddddddddddxx;                           \n                           ,oddddooodxxxxxxxxxxxxxdoooooooddxxxdddxxxddddddddddoodddddl,.....'::;;,'................................:odddddddddddddddddddxxxxxxxxxxxdddddxxx;                           \n                           ;oddddooodxxxxxxxxxxxxxdooooooddxxxxxdddddddoooooooooddxdddc,.....':::;;'................................,ldddddddddddddddddddxxxxxxxxxxxddddddxd;                           \n                           ;odddooooddxxxxxxxxxxxxdoooooddxxxxxxdddooooooooooodddxxddoc,.....,::::;,'...............................'cddddddxxdddddddddddxxxxxxxxxxxxdddddxd;                           \n                           ;odddoooodddxxxxxxxxxxdoooodddddddddddddooooooooodddddddxdl:'.....,:c::;,,'...............................:ddxxxxxxdddddddddddxxxxxxxxxxxxxddddxd;                           \n                           ;odddoooodddxxxxxxxxxxdoooodddddddddddddoooooooooddxdxxddoc,......,:cc:;;;'...............................;odddxxxxdddddddddddxxxxxxxxxxxxxxddddd;                           \n                           ,oooooooooooododddddddooooooooooddddddoooooooooooddddddddo:'......,:cc:;;;,...............................,ldddxxxxxxddddddddddxxxxxxxxxxxxxddddo;                           \n")
        time.sleep(0.05)
        clear()
        print(colorama.Fore.YELLOW + colorama.Style.BRIGHT + "                           ;xxxxxxkxxxxxxxxxxxxxxxxxkkkkkkkkkkkkkkkkkkxxddddddddddxxxxxxxxxxxxxxxddooooddddxxxxxxxxxxxxdddooooooooddxxxdddddddxxxxxxxxxxxxxxxxxddddodddddddd;                           \n                           ;xxxxxxxxxxxxxxxxxxxxxxxxxxxxxkkkkkkkOOkkOkkxdddddddddxxkkkkkkkkkkxxxxxxddddddxkkkkkkkkkkxxxxxddooooooooddxxxxxxxxxxxxxxxxxxxxxxxxdddddoooddddddd;                           \n                           ;xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxkkxxddddddddxxkkkkkkxxddddddddddddddddxxkkkkkkkkkkkkxxxdooooooooodxxkkkkkkkkxxxxxxxxxxxxxxxxdddoooddddddd;                           \n                           ;xxxxxxxxxxxxxxxxxxxxxkkkkxxkkkkxxxxxxdddddddxxxxxxxxxxxxxxddddddooooooddddddddddddxxdddxxxxxxxxdooooooooodxxkkkkxxkkkxxxxxxxxxxxxxxxdddooddddddd;                           \n                           ;xxxxxxxxxxxxxxxxxxkkOOOkxxkOOOOkkkkkkxxxxxxxxxxxxxxxxdddddddddxddoooddollccccc:::clodxddddddddddoooooodoooddddxdxxxxxxxxxxxxxxxxxxxxdddodddddddd;                           \n                           ;xxxxxxxxxxxxxxxxkkOOOOkxxxkOOOOOOOOOkkkkkkkkkxxxxxxxxxxxxxdddddddddddo:,,,'',,,,,,,;codddddoooooooooooodooodddxxxxxkkOOkkxkkkkkxxxxdddoodddddddd;                           \n                           ;xxxxxxxxxxxkkkOOOOOkkxxxxxkOOOOOOOOOOOOOOOOOkxxxxxxxxkkOkkkxxdddddddoc:,''''..''''',,;codxxxddddooooooodddxxxkkkkkkOOOOOkkxkOOOkxddddooodddddddd;                           \n                           ;xxxxxxxxxxxkkOOOOOOkxxxkkkOOOOOOOOOOOOOOOOkkxxxxxxxxxkkkkkkkxdddxxddl:;;,,,,'',,,,,,,,;lxxxxxxddooooooddxkkkkkkkOOOOOOOOkkxxkkkkxdddddoddddddddd;                           \n                           ;xxxxxxkkkkxxxkkOOOkkxxkOOOOOOOOOOOOOOkkxxxxxkxxxxxkkxxxxxxxxddddddlcccccccclccllllc:;',cdxxddddooooooooddxxkkkkkkOOOOOOOkxxxxxxxxxxxdddddddxxxxd;                           \n                           ;xxxxkkOOOOkkxxxxkkxxxxkOOOOOOOkkkkkkxxxxxxkkkkxxxxkkkxxxddddxxdddo:;:cccccllooooooolc;;cddooooodddoooooooodddxxkkOOOOOOOOOkxxdddxxxkxxxdddxxxxxd;                           \n                           ;xxkOOOOOOOOOkxxxxxxxkOO000OOOkkxxxxxxxxxkkOOOkxxxxxkxxxxkkkkkkkxdoc:cc::::ccllloooooc;;ldddoooodxddoooddddoooddxxkkkOOOOOOOkxddddxkxxxxdxxxxxxxx;                           \n                           :xkOOOOOOOO0OkkxxxxxkO00000OkkxxxkkkxxxxxkO00OkxxxxxxxkkkOOOOOOkkxdollc::::::cllcccllc:cdxxxxdoooddoooodxxxddoooddddxxkOOOkkkxdddddddddxxkkkkkxxx;                           \n                           :kOOOOOOOOOOOOOkkxxxkOOOOOkkxxxxkOOOOkkxxkO00OkxxxxxkkOOOOOOOOOkkdoddoccccc::clllccllcldkkkkkxddooooooodxxxxdddoodddddxxkkkkkkxddddddxxxkOOOOOkkx;                           \n                           :kOOOOOOOOOOOOOOkxxxxkkxxxxxxxxkOOOOOOOkkkkO0OkxxxxxkOO0OOOOOkOkkdlodlcccc:::clooooooloxkkkkkkxxxdooooodxkkxdddddxxxdddddxxkkkkxddddxxxkO00000OOk:                           \n                           :kOOOOOOOO0000OkkxxxxxxxxxxxxxxkOOOOOkkkxkkkkkxxxxxxkkO000OOOOOkkxoddlccc:::cllooooolloxkkkkkkxxxdoooooddxxddddxxxkxxdddddddxxkkxdxxkOOO00000000Oc                           \n                           :kOOOOOOOO0000OkxxxxxxxxkkkkkxxxxkkOkxxxkkOkxxxxxxxxkO00OOOOOkkkkkxxdlc:::::clllloooodxkkkkkkkxxddooooooddddoddxxxkkxxddoddddddddxxxOOO0000000000c                           \n                           :kOOOOOOOOOO0OOkkxxkkkkxxkkOkxxxxxxxxxxkOOOOkkxxxxxxkkOOOOOOOkkkkkxxdlcc::::clllllodxxxkkkkkkkxxxdoooooooodxddddxkkkxdddddxxddddxxxxkO00000000000c                           \n                           :kOOOOOOOOOOOOOkxxxkOOkxxxxxxxxkkkxxxxkOOOO0OkxxxxxxxxxkkOOOOkkkxxddolccccccllollloddxkkkkkkkxxxddooooooddxxkxxddxxxddddxxkxxdxxxxxxkO00000000000c                           \n                           :kOOOOOOOOkkkkxxxxkkOOOkkxxxxxkOOOkkxxkOOOOOOkxxxxxkkxxxkkkOOkkxdddolcc:::::ccllllododxkkkkkxxdooooooooodxkkkkkxdddxxddddxxddxkkkkxxkO0000000000Oc                           \n                           :kOOOOOOkkxxxxxxxxxkkkkkkkxxxxkOOOOOkxkOOOOOkxxxxxkkkkxxddxxxxddoddolcc:::cccllllooloodxxxxxddooddddoooodxkkkkkxxxkkkxxddddddxOOOkxxkOO000000000Oc                           \n                           ;xkkOOkkxxxxxxxxxddddxxxxddddxxkOOOOkxxkOOOOkxxxxxxxxxxddddddoooddolccc::ccclllllol;;:loddooooooddddooooodxxkkkxxkOOkkxxdddxkOOOOkkxxxkkOOO00000Oc                           \n                           ;dxxkkxxdxxxxxxxddxxxxxxdddxdddxkkkkkxxkkkkkxxddddddddxxxxxoolloddollllcccccclloddc'..',;:cllooooddoooooodxxkkxxxkkkkkxddoddxkkkkkxxxxxxxkkO0000Oc                           \n                           ;xxxxddxxkkkkkxkkkkkkkkxdxxkxxddxkkkkxdxkkkkxdddddddddddoc:;,,;ldddlc::cccccclodxo;'.......',,;::cloooooodxxxxxdxkkkkxdooooodddddddxxxxxxxxkO000Oc                           \n                           ;dddddxxkkkkkkkkkkkkkkxddxkkkxxddxkkkxdddxxxxddodoollc:;'.....,ldddl:::cllloddxdo;'...............',;:coddxxxxddxkkkkddddddoddxxxxxxxxxxkxxkkkOOk:                           \n                           ;dddddxxkkkkkkkkkkkkkxdddxkkkxxdddxxxxxxxdddddoooc;,,'........,clllc:;:coddddddl,.....................':oddddoooxxkxdoddxxxdddxkkkkkkkkOOOOkkxxkx:                           \n                           ;dddddxxkkkkkkkkkkkkxxdddxxxdddddddddxkkkkxxdddol;.............'',;:;;;:ccllooc,.......................'codoooooodddoodxkkkxdodxxkkkkkkOOOOOOkxxx:                           \n                           ;ddddxkkkkOkkkkkkkkkxdddddddddddddddxkkkkOOkxddoc,...............';;;;:cc:::::;'........................;oddddddooooooddxxkxdoodxkkkkkkkOOOOOkxxx:                           \n                           ;ddddxkkkOkkkkkkkxxxddddddxxxdddodddxkkkkkkkxddo:'...............';;:::::::::;'.........................'cdxxxxxdooooooddddddoddxkkkkkkkkkOOkkxxx;                           \n                           ;dddxkkkkkkxxxxdddddddddxxkxxxdodddddxkkkkkxdddo:'...............';:cll:::::;,'..........................;oxxxxxdooooodxxxxddddddxkkkkxkkkOOOOkxx;                           \n                           ;ddddxxdxxxxxddddddddxxxkkkxxdodddddddxkkkkxddoo:'...............';:lol:;:;;;'...........................;odxxddoooooodxkkkkxddddddxxxxxxkkOOOOkx;                           \n                           ;ddddddddxxxxxxddddxxkkkkkxxddodxxdddddxkkkxddol;................';clol:;;;;,'...........................,ldxxddoooddddxkOOOkkxdddooddddddkkOOOkx;                           \n                           ;odddddxxkkkkkkxdddxxkkkkkxxdoddxxxddddxxkkxddol,................';:cc:;;;;;'.............................;odxdooooxxxddkOOOOOOkxdddddddoddxxxxxx;                           \n                           ;odddxxkkkkkkkkxdoddxxxkkxxddodxxkxxddddxkkxddol,.................,;;;;,,;;,'.............................':oddooodxkkxdxkOOOOOOOkxdxxxxxxxxxxxxx;                           \n                           ;oddxkkkkkkkkkkxdoooddxkkxxdodxxxxdddxxddxkxddol,.................';;;;,,;;,.........,:;;,,,,'.............';codoodkkkkxdxkOOOOOOkxdxkkxxkkOkxxxx;                           \n                           ;oddxxkkkkkkkkxxdoooddxxxxddodxxdddddxkxdxxxddol,..................,;;;,;;,'........';;::ccccc;'..............,cooddxkkxdxkkOOOkxxddxkkxxkOOOOkkx;                           \n                           ;oddddxkkkkxxxddoddddoddxxdodxxddddddxxxxdxdddoc,..................',;;;;,,..........,;;:cccccc;................;coddxkkddxkOOOkxddxxkkxxkkOOOOOk:                           \n                           ;ddddddxkkxxdddddxxxxdooodooodoodxxkxxxdddddddo:'...................,;;;,,'...........,;::cccclc,.................;lddxxdddkOkkxxxxxxxxxxkkOOOkkx;                           \n                           ;xxxdddddddddddxxkkkxxdoooooooodxkkkOOkxddddddo:....................';;,,,'............,;::ccccc:'................':oddddddxxxxxkkkxxddddxkOkkxxx:                           \n                           ;dxxxxxdddddxxxkkkkkkxddoooooddxkkkkOOOkxxddddo;...................'';;,,'................',;:cc:,.................cddddddddddxkkOOkxddoodxxxxxxx:                           \n                           ;ddxdxxddddddxxxxxxxxxdddoooddxxxkkkkkkkkxxdddo:'''.......',,,,;;;;,,;;,'....................';;,'.................:dxxdddddddxkkkkkkxddooddxxxkk:                           \n                           ;dxxxxxdddddxxxxxxxxxxddoooddxxxxkkkkkkOkkxddddoc,....',,;:c::;;:c:,',,,'..............................'...........,oxxddoooddxxxxxxxxxdooodxxkkk:                           \n                           ;dxkxxxddddxxxkkkkxxkxxddoooodxxkkkOOOOkkxxdddddl,....'..';:;;;;;::,',,'....................   ........''..........;oxxxdooooddxxxxxxxdddodddxxkx:                           \n                           ;dxxxxxddddxxkkxxxxkkxxdooooooodxkkOOkxxxxddddddoc,.......,;;;;;;;,'',,'.....................     ...............,:ldxddooooodxxxxxxxxxxddddxxkkk:                           \n                           ;dxxxxdddddxxxxxxxxxxxxdooooooodxkkkkxxxxxdxdddddol:;'.....,;;;;;,...,,'................'.....      ..,;,,,,,,;:lddxxdooooooodxxxxxxxxxxdddddxkkk:                           \n                           ;dxxxxddoddxxxxxxxxxxxxdooodddooodxxddxxxxxdddddddxdolc:,...''''.....,,.................'.............:oddddddddddxddddoooooddxxxxxxxxxxxddddxkkk:                           \n                           ;dxxxxdooodxxxxxxxxxxxxdooodxxdddddddxkkkxxddddddxkkxdoolc,..........,'...............................:ddddddddddddddddddddoddxxxxxxxxxxxddddxkkk:                           \n                           ;dxxxddooodxxxxxxxxxxxxdooodxxxxdddxkkkOOkxxdddddxkkkkxdoo:,,........,................................:dddddddddddddddddddddddxxxxxxxxxxxddddxxkk:                           \n                           ,oddddooooddddxxxxxxxxddooodxxxxdddxkkOOOkxxxddddxkkkkxdol:;,........,'...............................;odxxdddddddddddxxdddddddxxxxxxxxxxdddddxkk:                           \n                           ,oddddooooddddddddddddddooodxdddddddxxkOkkxddddddxkkkxdool:,........',,...............................,ldddddddddddddddddddddddddxxxxxxxxdddddxxx:                           \n                           ,oddxdoooddxxxxxxxxxxxxdoooddoooddddddxkkkdddddddxkxdoooo:,.........',,...............................'cddddddddddddddddddddddddddddxdddddddddxxx;                           \n                           ,oddddooodxxxxxxxxxxxxxdoooooooddxxxddddxdddddooodddooodo;'.........';,................................;odddddddddddddddddddddxxxxxxxxxxxxddodxxx;                           \n                           ;oddddooodxxxxxxxxxxxxxdooooooodxxxxxddodddoooooooooodddl,..........,;,...............''...............;odddddddddddddddddddddxxxxxxxxxxxxdddddxd;                           \n                           ;odddooooddxxxxxxxxxxxxdooooooddxxxxxdddooooooooooodddddc'.........',;,'...............................,ldddddddddddddddddddddxxxxxxxxxxxxddoodxd;                           \n                           ;odddoooodddxxxxxxxxxxdoooodddddddddddddoooooooooddddxddc'.........,;;:;...............................,lddddddddxxxddddddddddxxxxxxxxxxxxxddoddd;                           \n                           ;odddooooddddxxxxxxxxxdoooodddddddddddddoooooooodddxxddo:'........';::cc,..............................'cddddxxxxxxxxxdddddddddxxxxxxxxxxxxddoddd;                           \n                           ,oooooooooooododddddddooooooooooddddddoooooooooooddddddo:,........,:::cc:,.............................'cddddxxxxxxxxxdddddddddxxxxxxxxxxxxddoddd;                           \n")
        time.sleep(0.05)
        clear()
        print(colorama.Fore.RED + colorama.Style.BRIGHT + "                           ;xxxxxxxxxxxxxxxxxxxxxxxxxxxxxkkkkkkkkkkkkxxxddddddddddxxxxxxxxxxxddddddooooddddxxxxxxxxxdddddoooooooooddxxxdddddddxxxxxxxxxxxxxxxxdddooodddddddd;                           \n                           :xxxxxxxxxxxxxxxxxxxxxxxxxxxxxkkkkkkkkkkkkkxxdddddddddxxkkkkkkkkkxxxxxxxddddddxkkkkkkkkkkxxxxxddooooooooodxxxxxxxxxxxxxxxxxxxxxxddddddooodddddddd;                           \n                           :xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxdddddddddxxkkkkkxxddddddddddddddddxxkkkkkkkkkkkkxxxdoooooooooddxkkkkkkkkkxxxxxxxxxxddxxdddooodddddddd;                           \n                           :xxxxxxxxxxxxxxxxxxxxxkkkkxxkkkkxxxxdddddddddxxxxxxxdxxxxxddddooooooooodddxxxdddddddxxdddxxxxxxxdooooooooodxxkkkkkkkkkxxxxxxxxxxxxxxdddoodddddddd;                           \n                           :xxxxxxxxxxxxxxxxxxkkOOOkxxkOOOOkkkkkxxxxxxxxxxxxxxxxddddddddddddooooodxxxxkkkxxxddddxxddddddddddoooooodooodddxxxxxxxxxxxxxxxxxxxxxxdddoodddddddd;                           \n                           ;xxxxxxxxxxxxxxxxxkOOOkkxxxkOOOOkkOOOkkkkkkkkxxxxxxxxxxxxxdddddddoooollcclllccloddddddxxdddooooooooooooooooodddxxxxxkkOOkkxkkkkxxxxdddooodddddddd;                           \n                           ;xxxxxxxxxxxxkkkOkOOkkxxxxxkkOOkkOOOOOOOOOOOOkxxxxxxxxkkkkkkxddodddl:;,,,,,,,,,,;:loddddddxxxdxddooooooodddxxxkkkkkkOOOOOkkxkOOkxxddooooodddddddd;                           \n                           ;xxxxxxxxxxxkkOOOOOOkxxxxkkOOOOkkOOOOOOOOOOkkxxxxxxxxxxkkkkkkxddddoc;''''..'''''',;:odddxxkxxxxddooooooodxkkkkkkOOOOOOOOOOkxxkkkkxddooooodddddddd;                           \n                           ;xxxxxxkkkxxxxkkkOOkxxxkkOOOOOOkOOOOOOkkxxxxxkxxxxxxkxxxxxxxdddddoc:;,,'''''''''',,,:oddxxxxddddooooooooddxxkkkkkOOOOOOOOkxxxdddxxxxddddddddddddd;                           \n                           ;xxxxkkOOOOkkxxxxxkxxxxkOOOOOOOkkkkkkxxxxxxkkkkxxxxxkkxxddddddddlccc::ccccccccccc:,,;lddddoooooodddoooooooddddxxkkOOOOOOOOkkxddddxxxxxxxddxxxxxxd;                           \n                           ;xxkOOOOOOOOOkxxxxxxxkOOOOOOOOkkxxxxxxxxxxkOOkxxxxxxxxxxxxkkkkkd:;:ccccllloooooool:,;odxxdddoooddxddoooddddododddxkkkOOOOOOkkxddddxkkxxxxxxxxxxxd;                           \n                           :xkOOOOOOOOOOkkxxxxxkOO000OOkkxxxkkxxxxxxkOO0OkxxxxxxxxxkOOOOkkd:::::::cllllooooooc;:oxkkkxxxdoooddoooodxxxddooodddxxxkOOOkkkxdddddxxxxxxkkkkxxxx;                           \n                           :kOOOOOOOOOOOOOkkxxxkOOOOOkkxxxxkOOOOkkxxkO00OkxxxxxxkOOOOOOOkkxlcc::::::ccllcclllc:cdkkkkkkkxdddoooooodxxxxdddoddddddxxkkkkkxxdddddxxxkkOOOOkkkx;                           \n                           :kOOOOOOOOOOOOOOkxxxxkkxxxxxxxxkkOOOOOOkkkkO0OkxxxxxkOOOOOOOkkdooolccc::::cllcccllclxkkkkkkkkxxxxdooooodxkkxdddddxxxdddddxxkkkkxdddxxxkkO00000OOk:                           \n                           :kOOOOOOOO000OOkkxxxxxxxxxxxxxxkkOOOOkkkxkkkkkxxxxxxxkOOOOOOkxolodlcccc::cclolooooloxkkkkkkkkxxxxdoooooddxxddddxxxxxxdddddddxkkkxxxxkOOOO0000000Oc                           \n                           :kOOOOOOOO000OOkxxxxxxxxkkkkkxxxxkkOkxxxkOkkxxxxxxxxkOOOOOOOkkxooolccc::::clloooolloxkkkkkkkkkxxdooooooodddddddxxxkxxxdddddddddxxxxkOOO0000000000c                           \n                           :kOOOOOOOOOOOOOkkxxkkkkxxkkOkxxxxxxxxxxkOOOOkxxxxxxxxkOOOOOOkkkxxdlc::::ccllooooloodxkkkkkkkkkxxxdoooooooodxxdddxkkkxddddddddddxxxxkkO00000000000c                           \n                           :kOOOOOOOOOOOOOkxxxkOOkxxxxxxxxkkxxxxxkOOOOOOkxxxxxxxxxxkOOOkkkkxdlc:::::cclllloooodxxkkkkkkkxxdddooooooddxkkxxdxxxxddddxxkxxxxxxxxxkO00000000000c                           \n                           :kOOOOOOOOkkkkxxxxkkOOOkkxxxxxkOOOOkxxkOOOO0OkxxxxxkxxxxxkkkkkkxdolccccclllollloooooddxkkkkkkxdooooooooodxkkkkkxxdxxxxdddxxddxkOkkxkkO0000000000Oc                           \n                           ;kOOOOOOkkxxxxxxxxxkkkkkkkxxxxkOOOOOkxkOOOOOkxxxxxkkkkxdddxxxxddolc:::::ccclllloddoooddxxkxxddoodddooooodxkkkkkxxxkkkxxdddddxkOOOkxxkOO000000000Oc                           \n                           ;xkkOOkkxxxxxxxxddxddxxxxddddxxkOOOOkxxkOOOOkxxxxxxxxxddddddooooolcc::::cccllllodddddddddddoooooddddoooodxkkkkkxxkOOkkxxdddxkOOOOkkxxxkkOO000000Oc                           \n                           ;dxxkkxxxxxxxxxxddxxxxxxdddxdddxkkkkkxxkkkkkkdddddddddxxkkxxddddlccclcllllllllooc;coxxddddddddoooooooooooxxkkkkxxkOOkkxddddxxkkkkkxxxxxxxkOO000OOc                           \n                           ;xxdxddxxkkkkkxkkkkkkkkxdxxkxdddxkkkkxdxkkkkxdddddddddxxdollloool::cc:cccllllldo:''';:cldxxxxxxdooooooooodxxkkxxkkOOkxddddddddddxxxxxxxxxxkOO000Oc                           \n                           ;xddddxxkkkkkkkkkkkkkkxddxkkkxdddxkkkxdddxxxdddddddoolc:,''';lddoc:c::::clllodxo;......',;clodxxddooooooodxxkxxxkkkkkxdddddddxxxkkxxxxxkkkkkkkOOk:                           \n                           ;dddddxxkkkkkkkkkkkkkxdddxkkxxxdddxxxdxxdddddoollc:;,'......,loddolc::::looddxd:'...........',:coddoooooodddddddxkkxddddxxxdddxkkkkkkkkOOOOkkxxkx;                           \n                           ;dddddxxkkkkkkkkkkkkxxdddxxxdddddddddxkkkkxdol;,''..........'looodoc:;;:lodxdo;'................',:coooooooooooooddddddxkkkxdddxkkkOkkkOOO0OOkxxx;                           \n                           ;ddddxkkkOOOkkkkkkkkxdddddddddddddddxkkkkkkxo:'..............,;::cc::;;:loddl;.....................'cooooodddxddoooooddxxxkxddddxkkkkkkOOOOOOkxxx;                           \n                           ;ddddxkkkOkkkxkkkxxxddddddxxxdddddddxkkkkkkxl,.................,;:::::::cclc;'......................,lddoddxxxxxdoooddddddddddddxkkkkkkkkOOOOkxxx;                           \n                           ;dddxkkkkkkxxxxdddddddddxxkxxddodddddxkkkkkxc'.................,;:::cllc:cc:'.......................'cdddddxxxxxdooooddxxxxdddddxxkkkkkkkOOOOOkxx;                           \n                           ;ddddxxxxxxxdddddodddxxxkkxxxdoddddoddxxkkkd:'.................';;;:cllc:c:,.........................:oddddxxxxdoooodddxkOOkxdddddxxxxxxxkOOOOOkx:                           \n                           ;ddddddddxxxxxxddddxxkkkkkxxdoodxxdddddxkkko;..................';;;;colc:c:'.........................;oddddxxxdoooddxxdxOOOOkkxddddddddddxkOOOOkx;                           \n                           ;odddddxxkkkkkkxdddxxkxxkxxddodxxxddddddxkkl,...................,;;;;cc:::,..........................,ldddxxxxdooodxkxxxkOOOOOOOkxddddddddxxxxkxx;                           \n                           ;odddxxkkkkkkkkxdoodxxxxxxxdoodxxxxddddddxxl'...................,;;;;;;;;,'..........................,lddddxxdooodxkOkxxkOOOOOOOOkxdxxxxxkkxxxxxx;                           \n                           ;oddxkkkkkkkkkkxdoooddxxxxxdodxxxddddddddxxl'...................,;;;;;:;'............................'cddddxdoooodxkOOkxxkOOOOOOOkxxxkkxkkOOkkxxx;                           \n                           ;oddxxkkkkkkkkxddoooodxxxxdoodxxddoddxxxdddc'...................';:;;;;,..............................:odddddoddddxxkOOkxxkOOOOkxxddxkkkkkOOOOkkx:                           \n                           ;oddddxkkkkxxdddodddooddxxdoddxdddddddxxddo:'...................';:;;;;'..............,;,'............;oddddooxxxdddxkOkxxkOOOOkxxxxxkkxxkOOOOOOk:                           \n                           ;ddddddxkkxddddddxxxxdoooooooooodxxxxxdddol;....................';:;;;,.............',;::::;,'........,ldddooddddddddxkkxxxkOOkxxxxxxxxxxkOOOOkkx;                           \n                           ;dxxdddddddddddxxkkkxdooooooooodxkkkkkxddoc,.....................,;;;;,.............';;;:cccc:........'cdddoooddxkxxddddddxxkxxxkkkxdddddkOOOkxxx:                           \n                           ;dxxxxxddddddxxxkkkkkxddoooooddxkkkkkOkxxdc'.....................',;;;'.............';;::cccc:'........;odddoodxkkkkkxddddddxxxkOOOkxddoodxxxxxxk:                           \n                           ;ddxdxxddddddxxxxddxddddooooddxxxkkkkkkkxxl,.....................'',,,'..............';:::ccc:'........,ldddddxkkkkkkkxxdddddxxkkOOkkxddooddxxkkkc                           \n                           ;dxxxxxdddddxxxxxxxxddddoooodxxxxkkkkkkkkxl,......................'',,.................,;:cc:,..........cdddddxxkkkkkkxxdddddxxkkkxxxxxdooddxkkkk:                           \n                           ;dxkkkxddddxxxkkkkxxxxxdoooooddxkkkkOkkkxdl;......................'',,..................,;;;,...........cddddxxxkkkkkkxxddooddxxxxxxxxdddoddxxxkx:                           \n                           ;dxxxxxddddxxkkxxkxxxxxdooooooodkkkkOkxddddo:'....................',,,...............  ................;ldddoddxxxxkkxxddooodxxxxxxxxxxxddddxkkOk:                           \n                           ;dxxxxxddddxxxxxxxxxxxxdooooooodxkkkkxdddddoc'....',,'''''........''',................ ...............'cddddoooddxxxxdooooooodxxxxxxxxxxddddxxkkk:                           \n                           ;dxxxxdddddxxxxxxxxxxxxdooodddooddxddddxxddoc'...,:clllll:,........'''................. ..............;lddddddooddddddooooooodxxxxxxxxxxdddddxkkk:                           \n                           ;dxxxxddoodxxxxxxxxxxxxdooodxdddoddddxxkkxddo:'.';clllcc:;'.........''...............................,lddddddddddddooooddoooodxxxxxxxxxxdddddxkkk:                           \n                           ;dxxxddooodxxxxxxxxxxxxdooodxxxxddddxkkkkxdddoc;,,;::;;;;;,..........'..................   .......',:oddddddddddddddddddddooodxxxxxxxxxxxddddxkkk:                           \n                           ,oddddoooodddxxxxxxxxxdoooodxxxxdddxkkkkkxddddoolc:;;;;;:;,..........'......................';ccclooddddddddddddddddddddddooddxxxxxxxxxxxddddxxkk:                           \n                           ,oddddoooodddddddddddddoooodxddoddddxxkkkxddddoooooc;;;;:;...........'......................,lddddddddddddddddddddddddddddooodddxxxxxxxxddddddxxx:                           \n                           ,oddxdoooddxxxxxxxxxxxddoooddooodddddddkkxddoooooddl;,,,'............'......................':oddddddddddddddddddddddddddddddddddddddddddddoodxxx;                           \n                           ,oddddooodxxxxxxxxxxxxxdoooooooddxxddddddddoooooodo:.................'.......................'coddddddddddddddddddddddddddddddxxxxxxxxxxxddoodxxx:                           \n                           ;oddddooodxxxxxxxxxxxxxdooooooddxxxxxdooooooooooooc'.................'........................:odddddddddddddddddddddddddddddddxxxxxxxxxxxddoddxd;                           \n                           ;odddooooddxxxxxxxxxxxddooooooddxxxxdddooooooooodo;.................''........................;odddddddddddddddddddddddddddddddxxxxxxxxxxdddoodxd;                           \n                           ;odddoooodddxxxxxxxxxxdooooddddddddddddddooooodddl'.................''............',..........;lddddddddddddddddddddddddddddddxxxxxxxxxxxxddoodxd;                           \n                           ;odddooooddddxxxxxxxxddoooodddddddddddddddddddddo:'.................''........................,ldddddddddddddxxxdddxxxxxxdddddxxxxxxxxxxxxddooddd;                           \n                           ,oooooooooooodddddddddooooooooodddddddddooooodddo;..................''........................,cdddxxxxxxxddxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxdddddd;                           \n")
        time.sleep(0.05)
        clear()
        j+=1
    x = 0
    clear()
    while x < 10:
        print(colorama.Fore.RED + colorama.Style.DIM + '   ▓█████  ██▀███   ██▀███   ▒█████   ██▀███     ▓█████  ██▀███   ██▀███   ▒█████   ██▀███     ▓█████  ██▀███   ██▀███   ▒█████   ██▀███     ▓█████  ██▀███   ██▀███   ▒█████   ██▀███  \n   ▓█   ▀ ▓██ ▒ ██▒▓██ ▒ ██▒▒██▒  ██▒▓██ ▒ ██▒   ▓█   ▀ ▓██ ▒ ██▒▓██ ▒ ██▒▒██▒  ██▒▓██ ▒ ██▒   ▓█   ▀ ▓██ ▒ ██▒▓██ ▒ ██▒▒██▒  ██▒▓██ ▒ ██▒   ▓█   ▀ ▓██ ▒ ██▒▓██ ▒ ██▒▒██▒  ██▒▓██ ▒ ██▒\n   ▒███   ▓██ ░▄█ ▒▓██ ░▄█ ▒▒██░  ██▒▓██ ░▄█ ▒   ▒███   ▓██ ░▄█ ▒▓██ ░▄█ ▒▒██░  ██▒▓██ ░▄█ ▒   ▒███   ▓██ ░▄█ ▒▓██ ░▄█ ▒▒██░  ██▒▓██ ░▄█ ▒   ▒███   ▓██ ░▄█ ▒▓██ ░▄█ ▒▒██░  ██▒▓██ ░▄█ ▒\n   ▒▓█  ▄ ▒██▀▀█▄  ▒██▀▀█▄  ▒██   ██░▒██▀▀█▄     ▒▓█  ▄ ▒██▀▀█▄  ▒██▀▀█▄  ▒██   ██░▒██▀▀█▄     ▒▓█  ▄ ▒██▀▀█▄  ▒██▀▀█▄  ▒██   ██░▒██▀▀█▄     ▒▓█  ▄ ▒██▀▀█▄  ▒██▀▀█▄  ▒██   ██░▒██▀▀█▄  \n   ░▒████▒░██▓ ▒██▒░██▓ ▒██▒░ ████▓▒░░██▓ ▒██▒   ░▒████▒░██▓ ▒██▒░██▓ ▒██▒░ ████▓▒░░██▓ ▒██▒   ░▒████▒░██▓ ▒██▒░██▓ ▒██▒░ ████▓▒░░██▓ ▒██▒   ░▒████▒░██▓ ▒██▒░██▓ ▒██▒░ ████▓▒░░██▓ ▒██▒\n   ░░ ▒░ ░░ ▒▓ ░▒▓░░ ▒▓ ░▒▓░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░   ░░ ▒░ ░░ ▒▓ ░▒▓░░ ▒▓ ░▒▓░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░   ░░ ▒░ ░░ ▒▓ ░▒▓░░ ▒▓ ░▒▓░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░   ░░ ▒░ ░░ ▒▓ ░▒▓░░ ▒▓ ░▒▓░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░\n    ░ ░  ░  ░▒ ░ ▒░  ░▒ ░ ▒░  ░ ▒ ▒░   ░▒ ░ ▒░    ░ ░  ░  ░▒ ░ ▒░  ░▒ ░ ▒░  ░ ▒ ▒░   ░▒ ░ ▒░    ░ ░  ░  ░▒ ░ ▒░  ░▒ ░ ▒░  ░ ▒ ▒░   ░▒ ░ ▒░    ░ ░  ░  ░▒ ░ ▒░  ░▒ ░ ▒░  ░ ▒ ▒░   ░▒ ░ ▒░\n      ░     ░░   ░   ░░   ░ ░ ░ ░ ▒    ░░   ░       ░     ░░   ░   ░░   ░ ░ ░ ░ ▒    ░░   ░       ░     ░░   ░   ░░   ░ ░ ░ ░ ▒    ░░   ░       ░     ░░   ░   ░░   ░ ░ ░ ░ ▒    ░░   ░ \n      ░  ░   ░        ░         ░ ░     ░           ░  ░   ░        ░         ░ ░     ░           ░  ░   ░        ░         ░ ░     ░           ░  ░   ░        ░         ░ ░     ░     \n                                                                                                                                                                                        ')
        time.sleep(0.05)
        x+=1
    exit()
    
    

def displayTitle(titleFilePath):
    ''' Printing Title '''
    for i,item in enumerate(titleFilePath):
        print(item)

def clear():
    ''' Clearing the whole screen '''
    os.system('cls')

def delay_print(s,t):
    ''' Animate text by moving slower '''
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(t)

    
def Hangman(value):
    ''' Hangman '''
    if value == 0:
        print('\n   +---+\n       |\n       |\n       |\n       |\n      ---')
    elif value == 1:
        print('\n   +---+\n   O   |\n       |\n       |\n       |\n      ---')
    elif value == 2:
        print('\n   +---+\n   O   |\n   |   |\n       |\n       |\n      ---')
    elif value == 3:
        print('\n   +---+\n   O   |\n  /|   |\n       |\n       |\n      ---')
    elif value == 4:
        print('\n   +---+\n   O   |\n  /|\\  |\n       |\n       |\n      ---')
    elif value == 5:
        print('\n   +---+\n   O   |\n  /|\\  |\n  /    |\n       |\n      ---')
    elif value == 6:
        print('\n   +---+\n   O   |\n  /|\\  |\n  / \\  |\n       |\n      ---')


def printWord(guessedLetters):
    ''' Checking where the correct letter can be placed '''
    counter=0
    rightLetters=0
    for char in randomWord:
        if(char in guessedLetters):
            print(randomWord[counter], end=" ")
            rightLetters+=1
        else:
            print(" ", end=" ")
        counter+=1
    return rightLetters

def Game():
    ''' This is the whole hangman game '''
    clear()
    AlphabetCaps = sorted(SaveAlphCap)
    CorrectItems.clear()
    RemoveItems.clear()
    wrong = 0
    right = 0
    displayTitle(Title)
    print()
    print("Genre :", GenreText)
    print()
    Hangman(wrong)
    while (wrong != 6 and right != length):
        print("")
        right = printWord(CorrectItems)
        print("")
        for x in randomWord:
            print("_", end=" ")
        print("\n-----------------------")
        print("Can't use: ", end="")
        for letter in RemoveItems:
            print(letter.lower(), end=", ")
        print("\n-----------------------")
        print("Enter 1 to stop the game.")
        letterGuessed = input("")
        if letterGuessed.upper() in AlphabetCaps:
            if letterGuessed.lower() in randomWord:
                AlphabetCaps.remove(letterGuessed.upper())
                CorrectItems.append(letterGuessed.lower())
                clear()
                displayTitle(Title)
                print()
                print("Genre :", GenreText)
                print()
                Hangman(wrong)
            else:
                wrong+=1
                AlphabetCaps.remove(letterGuessed.upper())
                RemoveItems.append(letterGuessed.lower())
                clear()
                displayTitle(Title)
                print()
                print("Genre :", GenreText)
                print()
                Hangman(wrong)
        elif letterGuessed.lower() == randomWord:
            break
        elif letterGuessed == "1":
            print("Game Stopped")
            break
        else:
            clear()
            displayTitle(Title)
            print()
            print("Genre :", GenreText)
            print()
            Hangman(wrong)
                    
    print("The Answer was", randomWord)
    print("Want to play again?\n1:NO\nANY NUMBER:YES ")

def GameChoice():
    ''' Genre Menu '''
    displayTitle(Title)
    print()
    for i,item in enumerate(GameSelection):
        print(i+1,"-",item)
    print()
    print("Genre Selected :",GenreText)
    print()
    
    

def getChoice1():
    ''' Choice for the main menu '''
    try:
        x = int(input("- "))
    except ValueError:
        print("Oops, You typed a letter instead a digit, please try again.")
    else:
        if x >= 1 and x <=4:
            return x
        else:
            print("The number is out of range!")

def getChoice2():
    ''' Choice for Hangman '''
    try:
        x = int(input("- "))
    except ValueError:
        print("Oops, You typed a letter instead a digit, please try again.")
    else:
        if x >= 1 and x <=2:
            return x
        else:
            print()

def getChoice3():
    ''' Choice for Genre '''
    try:
        x = int(input("- "))
    except ValueError:
        print("Oops, You typed a letter instead a digit, please try again.")
    else:
        if x >= 1 and x <=6:
            return x
        else:
            print()

def displayMenu():
    ''' Displays the Main Menu '''
    for i,item in enumerate(MainMenu):
        print(i+1,"-",item)


def Tutorial():
    ''' Displays the Tutorial For users '''
    clear()
    time.sleep(1)
    delay_print("Hello, User!",0.02)
    time.sleep(2)
    clear()
    delay_print("This tutorial will show you how to play",0.02)
    delay_print("...",0.1)
    time.sleep(1)
    print()
    displayTitle(Title)
    time.sleep(2)
    clear()
    delay_print("Lets get started!",0.02)
    time.sleep(2)
    clear()
    time.sleep(1)
    print('\n------------------+\n     +----+       |\n     O\t  |       |\n    /|\\   |       |\n    / \\   |       |\n\t  |       |\n\t=====     |\n_ _ _ _           |\n------------------+\n')
    print("\n\n")
    delay_print("When you start the game, the stand is for the dummy and the gaps are the text will be displayed.",0.02)
    time.sleep(3)
    clear()
    print("\n------------------+\n     +----+       |\n     \t  |       |\n          |       |\n          |       |\n\t  |       |\n\t=====     |\n\t          |\n_ _ _ _           |\n--------------    |\nCan't use:        |      \n--------------    |\n-_  \t\t  |\n------------------+\n")
    print("\n\n")
    delay_print("You would see this when starting the game.",0.02)
    time.sleep(2)
    clear()
    print("\n------------------+\n     +----+       |\n     \t  |       |\n          |       |\n          |       |\n\t  |       |\n\t=====     |\n\t          |\n_ _ _ _           |\n--------------    |\nCan't use:        |      \n--------------    |\n-_  \t\t  |\n------------------+\n")
    print("\n\n")
    delay_print("The section 'Can't use: ' is when you type a letter that dooesn't exist on the letter so it display there.",0.02)
    time.sleep(0.5)
    print()
    delay_print("If you type the correct letter it would display on those lines!",0.02)
    time.sleep(4)
    clear()
    print("\n------------------+\n     +----+       |\n     \t  |       |\n          |       |\n          |       |\n\t  |       |\n\t=====     |\n\t          |\n_ _ _ _           |\n--------------    |\nCan't use:        |      \n--------------    |\n-_  \t\t  |\n------------------+\n")
    print("\n\n")
    delay_print("Lets guess the first letter.",0.02)
    time.sleep(1)
    clear()
    print("\n------------------+\n     +----+       |\n     \t  |       |\n          |       |\n          |       |\n\t  |       |\n\t=====     |\n\t          |\n_ _ _ _           |\n--------------    |\nCan't use:        |      \n--------------    |\n-_  \t\t  |\n------------------+\n")
    print("\n\n")
    delay_print("Lets try the letter 'U'",0.02)
    time.sleep(2)
    clear()
    print("\n------------------+\n     +----+       |\n     \t  |       |\n          |       |\n          |       |\n\t  |       |\n\t=====     |\n\t          |\n_ _ _ _           |\n--------------    |\nCan't use:        |      \n--------------    |\n-u  \t\t  |\n------------------+\n")
    print("\n\n\nLets try the letter 'U'")
    time.sleep(0.5)
    clear()
    print("\n------------------+\n     +----+       |\n     \t  |       |\n          |       |\n          |       |\n\t  |       |\n\t=====     |\n  u\t          |\n_ _ _ _           |\n--------------    |\nCan't use:        |      \n--------------    |\n-_  \t\t  |\n------------------+\n")
    print("\n\n\nLets try the letter 'U'")
    time.sleep(1)
    clear()
    print("\n------------------+\n     +----+       |\n     \t  |       |\n          |       |\n          |       |\n\t  |       |\n\t=====     |\n  u\t          |\n_ _ _ _           |\n--------------    |\nCan't use:        |      \n--------------    |\n-_  \t\t  |\n------------------+\n")
    print("\n\n")
    delay_print("Hey, It worked!",0.02)
    time.sleep(1)
    clear()
    print("\n------------------+\n     +----+       |\n     \t  |       |\n          |       |\n          |       |\n\t  |       |\n\t=====     |\n  u\t          |\n_ _ _ _           |\n--------------    |\nCan't use:        |      \n--------------    |\n-_  \t\t  |\n------------------+\n")
    print("\n\n")
    delay_print("Lets try the letter F now.",0.02)
    time.sleep(1)
    clear()
    print("\n------------------+\n     +----+       |\n     \t  |       |\n          |       |\n          |       |\n\t  |       |\n\t=====     |\n  u\t          |\n_ _ _ _           |\n--------------    |\nCan't use:        |      \n--------------    |\n-f  \t\t  |\n------------------+\n")
    print("\n\n\nLets try the letter F now.")
    time.sleep(0.5)
    clear()
    print("\n------------------+\n     +----+       |\n     O\t  |       |\n          |       |\n          |       |\n\t  |       |\n\t=====     |\n  u\t          |\n_ _ _ _           |\n--------------    |\nCan't use: f,     |      \n--------------    |\n-_  \t\t  |\n------------------+\n")         
    print("\n\n\nLets try the letter F now.")
    time.sleep(0.5)
    clear()
    print("\n------------------+\n     +----+       |\n     O\t  |       |\n          |       |\n          |       |\n\t  |       |\n\t=====     |\n  u\t          |\n_ _ _ _           |\n--------------    |\nCan't use: f,     |      \n--------------    |\n-_  \t\t  |\n------------------+\n")         
    print("\n\n")
    delay_print("Darn it! ",0.02)
    time.sleep(0.5)
    delay_print("Wait, so it must be 'Duck'!",0.02)
    time.sleep(1)
    clear()
    print("\n------------------+\n     +----+       |\n     O\t  |       |\n          |       |\n          |       |\n\t  |       |\n\t=====     |\n  u\t          |\n_ _ _ _           |\n--------------    |\nCan't use: f,     |      \n--------------    |\n-Duck  \t\t  |\n------------------+\n")
    print("\n\n\nDarn it! Wait, so it must be 'Duck'!")
    time.sleep(0.5)
    clear()
    print("\n---------------------+\n     +----+          |\n     O\t  |          |\n          |          |\n          |          |\n\t  |          |\n\t=====        |\nd u c k\t             |\n_ _ _ _              |\n--------------       |\nCan't use: f,        |      \n--------------       |\n-_                   |\n\t\t     |\nThe answer was, duck |\n---------------------+\n")
    print("\n\n\nDarn it! Wait, so it must be 'Duck'!")
    time.sleep(0.5)
    clear()
    print("\n---------------------+\n     +----+          |\n     O\t  |          |\n          |          |\n          |          |\n\t  |          |\n\t=====        |\nd u c k\t             |\n_ _ _ _              |\n--------------       |\nCan't use: f,        |      \n--------------       |\n-_                   |\n\t\t     |\nThe answer was, duck |\n---------------------+\n")
    print("\n\n")
    delay_print("Yes, it worked!",0.02)
    time.sleep(1)
    clear()
    print("\n---------------------+\n     +----+          |\n     O\t  |          |\n          |          |\n          |          |\n\t  |          |\n\t=====        |\nd u c k\t             |\n_ _ _ _              |\n--------------       |\nCan't use: f,        |      \n--------------       |\n-_                   |\n\t\t     |\nThe answer was, duck |\n---------------------+\n")
    print("\n\n")
    delay_print("And that is how you play hangman!!",0.02)
    time.sleep(1)
    clear()
    print("\n---------------------+\n     +----+          |\n     O\t  |          |\n          |          |\n          |          |\n\t  |          |\n\t=====        |\nd u c k\t             |\n_ _ _ _              |\n--------------       |\nCan't use: f,        |      \n--------------       |\n-_                   |\n\t\t     |\nThe answer was, duck |\n---------------------+\n")
    print("\n\n")
    delay_print("Hope you learned how to play hangman! ",0.02)
    time.sleep(0.5)
    delay_print("Bye!",0.02)
    time.sleep(2)
    


#------- -Main code- --------

if CelebritiesNotFound == True or GamesNotFound == True or DictionaryNotFound == True or SpaceNotFound == True or SportsNotFound == True or GameTitleNotFound == True or MainMenuNotFound == True:
    while 1:
        clear()
        print("There are some Files are missing that are:")
        for i , item in enumerate(FileNotFound):
            print(i + 1, "-", item)
        leave = input("Press '1' to reset everything: ")
        if leave == "1":
            exit()
elif CelebritiesIOError == True or GamesIOError == True or DictionaryIOError == True or SpaceIOError == True or SportsIOError == True or GameTitleIOError == True or MainMenuIOError == True:
    while 1:
        clear()
        print("These are some Files that have an IOError:")
        for i , item in enumerate(IOErrorFound):
            print(i + 1, "-", item)
        leave = input("Press '1' to reset everything: ")
        if leave == "1":
            exit()


while 1:
    clear()
    displayTitle(Title)
    print()
    print(" Hello user!\n\n Welcome to Hangman! to start, you need to create you're username so we can identify\n you! Follow these instructions\n\n Create an Username : 1\n Exit : 2")
    Login = input(" - ")
    if Login == "1":
        clear()
        displayTitle(Title)
        print()
        Username = input("Username - ")
        break
    elif Login == "2":
        exit()


if Username == "Administrator42021":
    clear()
    while 1:
        time.sleep(.5)
        clear()
        print(colorama.Fore.GREEN + "  _                     _ _             \n | |                   | (_)            \n | |     ___   __ _  __| |_ _ __   __ _ \n | |    / _ \\ / _` |/ _` | | '_ \\ / _` |\n | |___| (_) | (_| | (_| | | | | | (_| |\n |______\\___/ \\__,_|\\__,_|_|_| |_|\\__, |\n                                   __/ |\n                                  |___/ ")
        time.sleep(.5)
        clear()
        print("  _                     _ _                 \n | |                   | (_)                \n | |     ___   __ _  __| |_ _ __   __ _     \n | |    / _ \\ / _` |/ _` | | '_ \\ / _` |    \n | |___| (_) | (_| | (_| | | | | | (_| |  _ \n |______\\___/ \\__,_|\\__,_|_|_| |_|\\__, | (_)\n                                   __/ |    \n                                  |___/     ")
        time.sleep(.5)
        clear()
        print(                                    
"  _                     _ _                     \n | |                   | (_)                    \n | |     ___   __ _  __| |_ _ __   __ _         \n | |    / _ \\ / _` |/ _` | | '_ \\ / _` |        \n | |___| (_) | (_| | (_| | | | | | (_| |  _   _ \n |______\\___/ \\__,_|\\__,_|_|_| |_|\\__, | (_) (_)\n                                   __/ |        \n                                  |___/         ")
        time.sleep(.5)
        clear()
        print("  _                     _ _                         \n | |                   | (_)                        \n | |     ___   __ _  __| |_ _ __   __ _             \n | |    / _ \\ / _` |/ _` | | '_ \\ / _` |            \n | |___| (_) | (_| | (_| | | | | | (_| |  _   _   _ \n |______\\___/ \\__,_|\\__,_|_|_| |_|\\__, | (_) (_) (_)\n                                   __/ |            \n                                  |___/             ")
        if j == load:
            clear()
            displayTitle(Title)
            print()
            delay_print("Hello Admin, Welcome to the game controlls.",0.02)
            time.sleep(3)
            clear()
            displayTitle(Title)
            print()
            delay_print("Lets get started Admin!",0.02)
            time.sleep(3)
            clear()
            time.sleep(1)
            delay_print("Controll.Open<AdminControlls>:",0.02)
            print("")
            delay_print("{",0.02)
            print("")
            delay_print("   Controll.DisplayMenu.AdminControll,",0.02)
            print("")
            delay_print("   Update.AdminControll{NULL}:",0.02)
            print("")
            delay_print("       Display.AdminControlls[UPDATEV2]:",0.02)
            print("")
            delay_print("       {",0.02)
            print("")
            delay_print("        .",0.02)
            print("")
            time.sleep(1)
            print("        .10%")
            time.sleep(0.1)
            print("        .12%")
            time.sleep(0.1)
            print("        .25%")
            time.sleep(0.6)
            print("        .50%")
            time.sleep(0.4)
            print("        .52%")
            time.sleep(0.5)
            print("        .66%")
            time.sleep(0.7)
            print("        .78%")
            time.sleep(0.3)
            print("        .79%")
            time.sleep(0.1)
            print("        .87%")
            time.sleep(0.2)
            print("        .94%")
            time.sleep(0.7)
            print("        .100%")
            time.sleep(1)
            print("        .CompleteUpdate.UPDATEV2[100%]};")
            time.sleep(1)
            delay_print("   DisplayControllMenu.To<Administrator42021>",0.02)
            print("")
            delay_print("   User<Administrator42021>.Access[TESTING]};",0.02)
            print("")
            delay_print("End.ControllUpdate<UPDATEV2>};",0.02)
            time.sleep(1)
            clear()
            time.sleep(.5)
            clear()
            print(colorama.Fore.GREEN + "  _                     _ _             \n | |                   | (_)            \n | |     ___   __ _  __| |_ _ __   __ _ \n | |    / _ \\ / _` |/ _` | | '_ \\ / _` |\n | |___| (_) | (_| | (_| | | | | | (_| |\n |______\\___/ \\__,_|\\__,_|_|_| |_|\\__, |\n                                   __/ |\n                                  |___/ ")
            time.sleep(.5)
            clear()
            print("  _                     _ _                 \n | |                   | (_)                \n | |     ___   __ _  __| |_ _ __   __ _     \n | |    / _ \\ / _` |/ _` | | '_ \\ / _` |    \n | |___| (_) | (_| | (_| | | | | | (_| |  _ \n |______\\___/ \\__,_|\\__,_|_|_| |_|\\__, | (_)\n                                   __/ |    \n                                  |___/     ")
            time.sleep(.5)
            clear()
            print(                                    
    "  _                     _ _                     \n | |                   | (_)                    \n | |     ___   __ _  __| |_ _ __   __ _         \n | |    / _ \\ / _` |/ _` | | '_ \\ / _` |        \n | |___| (_) | (_| | (_| | | | | | (_| |  _   _ \n |______\\___/ \\__,_|\\__,_|_|_| |_|\\__, | (_) (_)\n                                   __/ |        \n                                  |___/         ")
            time.sleep(.5)
            clear()
            print("  _                     _ _                         \n | |                   | (_)                        \n | |     ___   __ _  __| |_ _ __   __ _             \n | |    / _ \\ / _` |/ _` | | '_ \\ / _` |            \n | |___| (_) | (_| | (_| | | | | | (_| |  _   _   _ \n |______\\___/ \\__,_|\\__,_|_|_| |_|\\__, | (_) (_) (_)\n                                   __/ |            \n                                  |___/             ")
            time.sleep(.5)
            while 1:
                clear()
                displayTitle(Title)
                print()
                print("Hello " + str(Username) + ",")
                print()
                print("1 - GameCode")
                print("2 - Can't Use Testing")
                print("3 - Code for 'Can't Use'")
                print("4 - Exit")
                choice = input("- ")
                if choice == "1":
                    while 1:
                        clear()
                        print('\nwhile 1:\n    clear()\n    displayTitle(Title)\n    print("Hello " + str(Username) + ",")\n    print()\n    displayMenu()\n    choice = getChoice1()\n    if choice == 1:\n        while 1:\n            randomWord = random.choice(Genre)\n            length = len(randomWord)\n            Game()\n            choice = getChoice2()\n            if choice == 1:\n                break\n            elif choice == 2:\n                print()\n    elif choice == 2:\n        while 1:\n            clear()\n            GameChoice()\n            choice = getChoice3()\n            if choice == 1:\n                Genre.clear()\n                Genre = sorted(Sport)\n                GenreText = "Sports"\n                break\n            elif choice == 2:\n                Genre.clear()\n                Genre = sorted(Space)\n                GenreText = "Space"\n                break\n            elif choice == 3:\n                Genre.clear()\n                Genre = sorted(Celebrities)\n                GenreText = "Celebrities"\n                break\n            elif choice == 4:\n                Genre.clear()\n                Genre = sorted(Games)\n                GenreText = "Games"\n                break\n            elif choice == 5:\n                Genre.clear()\n                Genre = sorted(BookOfWords)\n                GenreText = "Random"\n                break\n            elif choice == 6:\n                break\n    elif choice == 3:\n        Tutorial()        \n    elif choice == 4:\n        exit()\n')
                        print("-------------------------------------END OF CODE-------------------------------------")
                        print()
                        choice = input("Enter '1' to exit: ")
                        if choice == '1':
                            break
                elif choice == "2":
                    while 1:
                        clear()
                        print("\n-----------------------")
                        print("Can't use: ", end="")
                        for letter in RemoveItems:
                            print(letter.lower(), end=", ")
                        print("\n-----------------------")
                        letter = input("Reset: Reset Everything\nBack: Back to concole\n- ")
                        if letter.upper() in AlphabetCaps:
                            AlphabetCaps.remove(letter.upper())
                            RemoveItems.append(letter.lower())
                        elif letter == "Reset":
                            AlphabetCaps = sorted(SaveAlphCap)
                            RemoveItems.clear()
                        elif letter == "Back":
                            AlphabetCaps = sorted(SaveAlphCap)
                            RemoveItems.clear()
                            break
                elif choice == "3":
                    while 1:
                        clear()
                        print('\nAlphabetCaps = [\'A\',\'B\',\'C\',\'D\',\'E\',\'F\',\'G\',\'H\',\'I\',\'J\',\'K\',\'L\',\'M\',\'N\',\'O\',\'P\',\'Q\',\'R\',\'S\',\'T\',\'U\',\'V\',\'W\',\'X\',\'Y\',\'Z\']\nRemoveItems = []\n\nSaveAlphCap = sorted(AlphabetCaps)\n\nwhile 1:\n    clear()\n    print("\n-----------------------")\n    print("Can\'t use: ", end="")\n    for letter in RemoveItems:\n        print(letter.lower(), end=", ")\n    print("\n-----------------------")\n    letter = input("Reset: Reset Everything\nBack: Back to concole\n- ")\n    if letter.upper() in AlphabetCaps:\n        AlphabetCaps.remove(letter.upper())\n        RemoveItems.append(letter.lower())\n    elif letter == "Reset":\n        AlphabetCaps = sorted(SaveAlphCap)\n        RemoveItems.clear()\n    elif letter == "Back":\n        AlphabetCaps = sorted(SaveAlphCap)\n        RemoveItems.clear()\n        break\n')
                        print("-------------------------------------END OF CODE-------------------------------------")
                        print()
                        choice = input("Enter '1' to exit: ")
                        if choice == '1':
                            break
                elif choice == "4":
                    SuperSecretSettings()
        j+=1
else:
    while 1:
        clear()
        displayTitle(Title)
        print("Hello " + str(Username) + ",")
        print()
        displayMenu()
        choice = getChoice1()
        if choice == 1:
            while 1:
                randomWord = random.choice(Genre)
                length = len(randomWord)
                Game()
                choice = getChoice2()
                if choice == 1:
                    break
                elif choice == 2:
                    print()
        elif choice == 2:
            while 1:
                clear()
                GameChoice()
                choice = getChoice3()
                if choice == 1:
                    Genre.clear()
                    Genre = sorted(Sport)
                    GenreText = "Sports"
                    break
                elif choice == 2:
                    Genre.clear()
                    Genre = sorted(Space)
                    GenreText = "Space"
                    break
                elif choice == 3:
                    Genre.clear()
                    Genre = sorted(Celebrities)
                    GenreText = "Celebrities"
                    break
                elif choice == 4:
                    Genre.clear()
                    Genre = sorted(Games)
                    GenreText = "Games"
                    break
                elif choice == 5:
                    Genre.clear()
                    Genre = sorted(BookOfWords)
                    GenreText = "Random"
                    break
                elif choice == 6:
                    break
        elif choice == 3:
            Tutorial()        
        elif choice == 4:
            exit()
