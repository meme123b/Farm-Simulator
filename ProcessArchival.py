import os
from datetime import datetime
import colorama as ca
from tkinter import *

ca.init()
global PATH, OFFSETS, VERSION
OFFSETS = 825783
VERSION = 100
PATH = "C:\\Users\\Administrator\\AppData\\LocalLow\\FarmGame\\"

def string_shift(text, offset):
    """对字符串中的每个字符进行偏移"""
    return ''.join(chr(ord(char) + offset) for char in text)

def CheckIfTheFolderExists():
    # 检查目录是否存在
    directory = os.path.dirname(PATH)
    if not os.path.exists(directory):
        # 目录不存在，创建目录
        os.makedirs(directory)

def VersionComparison():
    with os.scandir(PATH) as entries:
        for entry in entries:
            print(entry.name, end = ' -> ')
            with open(PATH + entry.name, 'r', encoding='utf-8') as f:
                lines = string_shift(f.readlines()[0], -OFFSETS).split('\n')[0].split('=')[1]
                Version = list(map(int, lines.split('.')))
                print('version:', end = ' ')
                if Version[0] * 100 + Version[1] * 10 + Version[2] == VERSION:
                    print(ca.Fore.GREEN + (lines + ' 存档版本号等于游戏版本号, 可以游玩!') + ca.Fore.RESET)
                elif Version[0] * 100 + Version[1] * 10 + Version[2] < VERSION:
                    print(ca.Fore.YELLOW + (lines + ' 存档版本号低于游戏版本号, 如使用该存档启动游戏将自动覆盖') + ca.Fore.RESET)
                else:
                    print(ca.Fore.RED + (lines + ' 存档版本号高于游戏版本号, 请检查你的游戏版本是否是最新版本') + ca.Fore.RESET)
                

def SaveFile():
    with open(PATH + f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S').replace(' ', '_').replace(':', '')}.sav", 'w', encoding = 'UTF-8') as f:
        f.write(f"{string_shift(f'VERSIONS=1.0.0', OFFSETS)}")
        f.close()

def OpenFile(FileName):
    with open(PATH + FileName, 'r', encoding='utf-8') as file:
        lines = string_shift(file.readlines()[0], -OFFSETS).split("\n")
        print(lines)
    
CheckIfTheFolderExists()

if __name__ == '__main__':
    VersionComparison()
    #SaveFile()
