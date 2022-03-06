import os
import re
import csv

## rename downloaded linkedin course files
class FileRenamer():
    def __init__(self):
        self.path = os.getcwd()
        self.path = os.path.normpath(self.path)
        self.pathsep = self.path.count(os.path.sep) + 1        

## function to get prefix
    def getprefix(self, target_file, target_index):
        ## Get the first word
        target_prefix = os.path.basename(target_file).split()[0]
        
        ## Get the second word
        ## Use full filename if no second word
        try:
            target_filename = os.path.basename(target_file).split()[1]
        except:
            target_filename = os.path.basename(target_file)
        
        ## Check if second word is a delimiter or the start of filename
        ## Get the filename without prefix
        if(len(target_filename)==1):
            target_filename = " ".join(os.path.basename(target_file).split()[2:])
        else:
            target_filename = os.path.basename(target_file)
        ## Check for and strip off brackets from the prefix
        if(re.search(r"\[(\w+)\]", target_prefix)):
            target_prefix = target_prefix.strip("[").strip("]")
        else:
            pass

        ## Use prefix if numeric
        ## Else autoindex prefix based on accessed sequence
        if(target_prefix.isnumeric()):
            target_prefix = '{:0>2}'.format(target_prefix)
            target_result = [target_prefix, target_filename]
            return target_result
        else:
            target_prefix = '{:0>2}'.format(target_index + 1)
            target_result = [target_prefix, target_filename]
            return target_result

## linkedIn rename loop  
    def linkedin(self):
        courses = [f.path for f in os.scandir(self.path) if f.is_dir()]
        for course in courses:
            chapters = [f.path for f in os.scandir(course) if f.is_dir()]  
            for chapter in chapters:
                chapter_index = chapters.index(chapter)
                chapter_prefix = "C" + self.getprefix(chapter, chapter_index)[0] + "_"
                episodes = [f.path for f in os.scandir(chapter) if f.is_file()]
                for episode in episodes:
                    if episode.endswith(".srt"):
                        os.remove(os.path.join(chapter,episode))
                    else:
                        episode_index = episodes.index(episode)
                        episode_prefix = self.getprefix(episode, episode_index)[0]
                        episode_filename = self.getprefix(episode, episode_index)[1]
                        newfilename = chapter_prefix + episode_prefix + "_" + episode_filename
                        with open('log.csv','a') as csvfile:
                            headers=['path','before','after']
                            writer = csv.DictWriter(csvfile, fieldnames=headers)
                            if os.stat('log.csv').st_size == 0:
                                writer.writeheader()
                            writer.writerow({'path': chapter, 'before': os.path.basename(episode), 'after': newfilename})
                            os.rename(os.path.join(chapter, episode), os.path.join(chapter, newfilename))


if __name__ == "__main__":
    app = FileRenamer()
    app.linkedin()


##  REFERENCES
##  ====================================================    
##  https://stackoverflow.com/questions/509211/understanding-slice-notation
##  https://stackoverflow.com/questions/8569201/get-the-string-within-brackets-in-python
##  https://stackoverflow.com/questions/30963705/python-regex-attributeerror-nonetype-object-has-no-attribute-group
##  https://stackoverflow.com/questions/5188792/how-to-check-a-string-for-specific-characters/5189069
##  https://www.programiz.com/python-programming/methods/list/index
##  https://docs.python.org/3/library/re.html
##  https://stackoverflow.com/questions/42977363/python-csv-header-ignore-while-keep-appending-data-to-csv-file
##
##  PROBLEM
##  ====================================================    
##  .Course A
##  ...[0] Chapters
##  .....Exercise Files
##  .....[0] Files.ext
##
##  .Course B
##  ... 2 - Chapters
##  ...... Exercise Files
##  ...... 2 Files.ext
##
##
##  SOLUTION
##  ====================================================    
##  C01_01_Files.ext
##  C02_02_Files.ext
##
##
##  WIP
##  ====================================================   
##  - How to prevent renaming when already renamed?
##  - Write results of before and after to text file
##
##
##  OLD VERSION
##  ====================================================  
##  for folders with format as "[01] Chapter A"    
##    def linkedin(self):
##        courses = [f.path for f in os.scandir(self.path) if f.is_dir()]
##        for course in courses:
##            chapters = [f.path for f in os.scandir(course) if f.is_dir()]
##            for chapter in chapters:
##                # Get chapter prefix within brackets
##                chapter_prefix = re.search(r"\[(\w+)\]", os.path.basename(chapter))
##                if chapter_prefix.group(1).isnumeric():
##                    prefix_chapter = "C" + "{:0>2}".format(chapter_prefix.group(1)) + "_"
##                else:
##                    pass
##                episodes = [f.path for f in os.scandir(chapter) if f.is_file()]
##                for episode in episodes:
##                    if episode.endswith(".srt"):
##                        os.remove(os.path.join(chapter,episode))
##                    else:
##                        # Get episode prefix within brackets                        
##                        episode_prefix = re.search(r"\[(\w+)\]", os.path.basename(episode))
##                        if episode_prefix.group(1).isnumeric():
##                            prefix_episode = '{:0>2}'.format(episode_prefix.group(1)) + "_"
##                        else:
##                            prefix_episode = '{:0>2}'.format(episodes.index(episode) + 1) + "_"
##                        new_prefix = prefix_chapter + prefix_episode
##                        newfilename = new_prefix + os.path.basename(episode).split("] ")[1]
##                        os.rename(os.path.join(chapter, episode), os.path.join(chapter, newfilename))
