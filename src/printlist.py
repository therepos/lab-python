##   Export mp4 files in the current folder to a text file
import os

##os.system("dir /b > list.txt")
targetpath = os.getcwd()
os.system("dir /s "+targetpath+" | findstr /b /c:\" \" > stats.txt")

## ---------------------------
## REFERENCES
## ===========================
## https://forums.tomshardware.com/threads/how-do-i-get-a-list-of-all-folders-and-their-sizes.994079/
##
## ---------------------------
## WIP
## ===========================
## To clean up the output file showing only the required results
