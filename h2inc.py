# (c)2018 Jan Lerking
# Convert a C-header file to an asm include file

import os
import sys
from h2inc_parser import parseline, parseparsed

cnt = 0

def sourcedir_filecnt(sourcedir):
    ### Return the number of files, ending with '.h', in sourcedir - including subdirectories ###
    cnt = 0
    for folderName, subfolders, files in os.walk(sourcedir):
        for file in files:
            if file.lower().endswith('.h'):
                cnt = cnt+1
    return cnt
                
def sourcedir_foldercnt(sourcedir):
    ### Return the number of folders, if it contains '*.h' files, in sourcedir - including subdirectories ###
    global cnt
    for folderName, subfolders, files in os.walk(sourcedir):
        if subfolders:
            for subfolder in subfolders:
                sourcedir_foldercnt(subfolder)
        tempf = [file for file in files if file.lower().endswith('.h')]
        if tempf:
            cnt = cnt+1
            print(folderName)
    return cnt