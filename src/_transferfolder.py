
import shutil
import os
 
# path to source directory
src_dir = 'fol1'
 
# path to destination directory
dest_dir = 'fol2'
 
# getting all the files in the source directory
files = os.listdir(src_dir)
 
shutil.copytree(src_dir, dest_dir)




## REFERENCES
## -----------------------
## https://www.geeksforgeeks.org/copy-all-files-from-one-directory-to-another-using-python/
