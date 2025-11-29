import os
from datetime import datetime
from colorama import Fore, Style
from tkinter import *

global PATH, OFFSETS, VERSION
OFFSETS = 825783
VERSION = '1.0.0'
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
    root = Tk()
    
    VERSION_LIST = list(map(int, VERSION.split('.')))
    with os.scandir(PATH) as entries:
        for entry in entries:
            Button(root, text = "ARCHIVAL", command = lambda : OpenFile(entry.name)).pack()
            print(entry.name, end = ' -> ')
            with open(PATH + entry.name, 'r', encoding='utf-8') as f:
                lines = string_shift(f.readlines()[0], -OFFSETS).split('\n')[0].split('=')[1]
                print('version:', lines)
    root.mainloop()

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
