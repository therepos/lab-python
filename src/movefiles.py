import os
import shutil
import zipfile

## =======================================     
## Single Folder - Move all files within subdirectories to root
## =======================================
##
##class FileMover:
##    def __init__(self):
##        self.targetpath = os.getcwd()  
##
##    def movefiles(self, targetpath):
##        for root, dirs, files in os.walk(targetpath, topdown=False):
##            for file in files:
##                try:
##                    source = os.path.join(root, file)
##                    destination = os.path.join(targetpath, file)
##                    if not os.path.exists(destination):
##                        shutil.move(source, targetpath)
##                    else:
##                        if not root == targetpath:
##                            os.remove(source)
##                        else:
##                            pass
##                except OSError:
##                    pass
##            try:
##                os.rmdir(root)
##            except OSError:
##                pass
##
##    def start(self):
##        self.movefiles(self.targetpath)
##
##      
##if __name__ == "__main__":
##    app = FileMover()
##    app.start()

## =======================================     
## Multiple Folder - Move all files within subdirectories to their respective root
## =======================================
##          
class FileMover:
   def __init__(self):
       self.targetpath = os.getcwd()
       self.targetfolders = [f.path for f in os.scandir(self.targetpath) if f.is_dir()]

   def movefiles(self, currentfolder):
       subfolders = [f.path for f in os.scandir(currentfolder) if f.is_dir()]
       for sub in subfolders:
           for f in os.listdir(sub):
               source = os.path.join(sub, f)
               destination = os.path.join(currentfolder, f)
##               if not os.path.exists(destination):
               shutil.move(source, destination)
##               else:
##                  os.remove(source)
           os.rmdir(sub)
           
##   def unzipfiles(self, currentfolder):
##       zipfiles = [f.path for f in os.scandir(currentfolder) if zipfile.is_zipfile(f)]
##       for zf in zipfiles:
##           with zipfile.ZipFile(zf, 'r') as zip_ref:
##               zip_ref.extractall(currentfolder)
##           os.remove(zf)

   def start(self):
       for folder in self.targetfolders:
          self.movefiles(folder)
##          self.unzipfiles(folder)
           
if __name__ == "__main__":
   app = FileMover()
   app.start()
##
##    
## =======================================     
## DOCUMENTATION
## =======================================
## Point of Entry: ./Course/Subfolders
## Point of Entry: ./Course/Weeks
##
##    
## =======================================   
## REFERENCES
## =======================================
## Source: https://stackoverflow.com/questions/58792626/extract-all-files-from-multiple-folders-with-python
## Purpose: Move files in subfolders to main folder
## To-Do:
## - method to extract files from zip to root
## - method to delete file types (e.g. srt)
## self.targetfolder = r"./"
## https://stackoverflow.com/questions/48892772/how-to-remove-a-directory-is-os-removedirs-and-os-rmdir-only-used-to-delete-emp
## https://stackoverflow.com/questions/6996603/how-to-delete-a-file-or-folder-in-python
## https://stackoverflow.com/questions/3451111/unzipping-files-in-python
## https://automatetheboringstuff.com/chapter9/
## https://www.tutorialspoint.com/python/os_chdir.htm
## https://stackoverflow.com/questions/45703685/move-files-in-folders-to-a-top-level-directory
## https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory
## https://programmerah.com/python-how-to-delete-empty-files-or-folders-in-the-directory-21529/
##
## =======================================   
## WIP
## =======================================   
## Not recursive enough to remove layers of subdirectories. Need to execute several times to deliver.
