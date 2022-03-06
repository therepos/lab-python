import os

## rename downloaded coursera course files
class FileRenamer():
    def __init__(self):
        self.path = os.getcwd()
        self.path = os.path.normpath(self.path)
        self.pathsep = self.path.count(os.path.sep) + 1        
    
    def get_depth(self, targetpath):
        curr_path = os.path.normpath(targetpath)
        next_pathlevel = curr_path.count(os.path.sep) + 1
        curr_pathtree = [root for root, dirs, files in os.walk(targetpath, topdown=True)]
        depth = max(curr_pathtree, key=len).count(os.path.sep) - curr_path.count(os.path.sep)
        return depth

    def get_totaldir(self, targetpath):
        curr_path = os.path.normpath(targetpath)
        next_pathlevel = curr_path.count(os.path.sep) + 1
        curr_pathtree = [root for root, dirs, files in os.walk(targetpath, topdown=True)]
        totaldir = sum(1 for x in curr_pathtree if x.count(os.path.sep) == next_pathlevel)
        return totaldir

    def get_totalsubdir(self, targetpath):
        curr_path = os.path.normpath(targetpath)
        next_pathlevel = curr_path.count(os.path.sep) + 1
        curr_pathtree = [root for root, dirs, files in os.walk(targetpath, topdown=True)]
        totalsubdir = sum(1 for x in curr_pathtree if x.count(os.path.sep) > next_pathlevel)
        return totalsubdir
    
    def get_depthpath(self, targetpath, targetdepth=1):
        curr_path = os.path.normpath(targetpath)
        next_pathlevel = curr_path.count(os.path.sep) + targetdepth
        curr_pathtree = [root for root, dirs, files in os.walk(curr_path, topdown=True)]
        pathtree = [x for x in curr_pathtree if x.count(os.path.sep) == next_pathlevel]
        return pathtree

    def get_prefix(self, targetpath):
        prefix_chap = os.path.basename(targetpath)[:2]
        return prefix_chap

    def coursera_structure(self):
        depth = self.get_depth(self.path)
        courses = [f.path for f in os.scandir(self.path) if f.is_dir()]
        for course in courses:
            print("--", os.path.basename(course))
            modules = [f.path for f in os.scandir(course) if f.is_dir()]
            for module in modules:
                print("-----", os.path.basename(module))
                weeks = [f.path for f in os.scandir(module) if f.is_dir()]
                for week in weeks:
                    print("----------", os.path.basename(week))
                    chapters = [f.path for f in os.scandir(week) if f.is_dir()]
                    for chapter in chapters:
                        print("==============", os.path.basename(chapter))
                        files = [f.path for f in os.scandir(chapter) if f.is_file()]
                        for index, file in enumerate(files):
                            print("................", os.path.basename(file))

    def coursera(self):
        depth = self.get_depth(self.path)
        courses = [f.path for f in os.scandir(self.path) if f.is_dir()]
        for course in courses:
            modules = [f.path for f in os.scandir(course) if f.is_dir()]
            for module in modules:
                if os.path.basename(module)[:2].isnumeric():
                    prefix_module = '{:0>2}'.format(os.path.basename(module)[:2]) + "_"
                else:
                    prefix_module = '{:0>2}'.format(modules.index(module) + 1) + "_"
                prefix = prefix_module + "00_00_"
                self.renamecoursera(module, prefix)
                weeks = [f.path for f in os.scandir(module) if f.is_dir()]
                for week in weeks:
                    if os.path.basename(week)[:2].isnumeric():
                        prefix_week = '{:0>2}'.format(os.path.basename(week)[:2]) + "_"
                    else:
                        prefix_week = '{:0>2}'.format(weeks.index(week) + 1) + "_"
                    prefix = prefix_module + prefix_week + "00_"
                    self.renamecoursera(week, prefix)
                    chapters = [f.path for f in os.scandir(week) if f.is_dir()]
                    for chapter in chapters:
                        if os.path.basename(chapter)[:2].isnumeric():
                            prefix_chapter = '{:0>2}'.format(os.path.basename(chapter)[:2]) + "_"
                        else:
                            prefix_chapter = '{:0>2}'.format(chapters.index(chapter) + 1) + "_"
                        prefix = prefix_module + prefix_week + prefix_chapter
                        self.renamecoursera(chapter, prefix)

    def renamecoursera(self, targetpath, prefix="00_00_00_"):
        files = [f.path for f in os.scandir(targetpath) if f.is_file()]
        for file in files:
            if os.path.basename(file)[:2].isnumeric():
                newfilename = prefix + os.path.basename(file)
            else:
                newfilename = prefix + "00_" + os.path.basename(file)
            os.rename(os.path.join(targetpath, file), os.path.join(targetpath, newfilename))
            

if __name__ == "__main__":
    app = FileRenamer()
    app.coursera()


## Version 2
## ====================================================    
## for root, subdirectories, files in os.walk(directory, topdown=True):
##     print("Root: ", root)
##     print("Subdirectories: ", subdirectories)
##     print("Files: ", files)
##     print("=====")## projects = 0
    
## buildings = 0
## txt_files = 0
## 
## path = os.getcwd()
## 
## for root, directories, files in os.walk(path):
##     if root == path:
##         projects = len(directories)
##         for sub_dir in directories:
##             full_dir = os.path.join(root, sub_dir)
##             for root_, directories_, files_ in os.walk(full_dir):
##                 if root_ == full_dir:
##                     if directories_ == []:
##                         buildings += 1
##                     else:
##                         buildings += (len(directories_))
## 
##     for i in files:
##         if i.endswith('.txt'):
##             txt_files += 1
## 
## print("There are {} projects, {} buildings and {} text files".format(projects, buildings, txt_files))

##     for subdirectory in subdirectories:
##         print(os.path.join(root, subdirectory))
##     for file in files:
##         print(os.path.join(root, file))

## Version 1
## ====================================================    
## class FileRenamer:
##     def __init__(self):
##         self.path = os.getcwd()
##         self.weekfolders = [f.path for f in os.scandir(self.path) if f.is_dir()]
##         self.prefixweek = "00_"
##         self.prefixchapter = "00_"
## 
##     def rename(self, currentfolder):
##         files = [f.path for f in os.scandir(currentfolder) if f.is_file()]
##         for index, file in enumerate(files):
##             prefix = self.prefixweek + self.prefixchapter
##             newfilename = prefix + os.path.basename(file)
##             os.rename(os.path.join(currentfolder, file), os.path.join(currentfolder, newfilename))
##         ## self.__init__()
## 
##     def start(self):
##         for wfolder in self.weekfolders:
##             currentdir = os.path.basename(wfolder)
##             self.prefixweek = currentdir[:2] + "_"
##             ## self.prefixweek = currentdir.split("_",1)[0] + "_"
##             self.cfolders = [f.path for f in os.scandir(wfolder) if f.is_dir()]
##             
##             wfiles = [f.path for f in os.scandir(wfolder) if f.is_file()]
##             for index, file in enumerate(wfiles):
##                 prefix = self.prefixweek + self.prefixchapter + "00_"
##                 ## prefix = self.prefixweek + self.prefixchapter + "00_"                
##                 newfilename = prefix + os.path.basename(file)
##                 os.rename(os.path.join(currentdir, file), os.path.join(currentdir, newfilename))
## 
##             for folder in self.cfolders:
##                 currentdir = os.path.basename(folder)
##                 self.prefixchapter = currentdir[:2] + "_"
##                 ## self.prefixchapter = currentdir.split("_",1)[0] + "_"                
##                 self.rename(folder)
##             
## 
## if __name__ == "__main__":
##     app = FileRenamer()
##     app.start()        

##  REFERENCES
##  ====================================================    
##  https://www.codegrepper.com/code-examples/python/python+loop+through+all+folders+and+subfolders
##  https://stackoverflow.com/questions/10989005/do-i-understand-os-walk-right
##  https://programtalk.com/python-examples/os.walk.next/
##  https://stackoverflow.com/questions/56440759/count-numbers-of-subdirectories-and-files-with-special-conditions-in-python
##  https://www.positronx.io/python-count-the-number-of-files-and-directories/
##  https://stackoverflow.com/questions/7159607/list-directories-with-a-specified-depth-in-python
##  https://queirozf.com/entries/python-number-formatting-examples

##  STRUCTURE
##  ====================================================    
##  .Level 0 - Course
##  ...Level 1 - Modules [01]
##  .....Level 2 - Weeks [01]
##  .......Level 3 - Chapters [01]
##  .........Level 4 - Files [01]
##  newfilename = 01_01_01_01_File.ext
## 
##  ====================================================    
##  01_02_03_04_EpisodeTitle.mp4
##  01 = Topic
##  02 = Week
##  03 = Week Topic
##  04 = Episode
##     
##  WIP
##  ====================================================    
##  original_name = "snackbox_12.dat"
##  truncated_name = original.split("_")[0] + ".dat"
##  
##  for index, file in enumerate(files):
##      os.rename(os.path.join(path, file), os.path.join(path, ''.join([str(index), '.jpg'])))
##
##  Go through all the files to rename a particular format.
##  Go through all the files and remove a particular type.
