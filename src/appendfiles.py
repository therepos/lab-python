import glob
import os

path = os.getcwd() + "\**\*.bas"
read_files = glob.glob(path, recursive=True)

with open("result.bas", "wb") as outfile:
    for f in read_files:
        with open(f, "rb") as infile:
            outfile.write(infile.read())
            outfile.write(b"\n")

# =============================
# References
# =============================
# https://stackoverflow.com/questions/14798220/how-can-i-search-sub-folders-using-glob-glob-module
# https://www.geeksforgeeks.org/python-program-to-merge-two-files-into-a-third-file/