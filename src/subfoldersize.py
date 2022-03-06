# import module
import os
import pandas as pd

course_metadata = {'title':[], 'foldersize':[]}
size = 0
courses = [f.path for f in os.scandir(os.getcwd()) if f.is_dir()]
for course in courses:
    size = 0
    course_name = os.path.basename(course)
    episodes = [f.path for f in os.scandir(course) if f.is_file()]
    for episode in episodes:
        size += + os.path.getsize(episode)

    course_metadata['title'].append(course_name)
    course_metadata['foldersize'].append(round(size/1024000))

course_data_df = pd.DataFrame(course_metadata)
course_data_df.to_csv('metadata.csv')

##*************************************
##REFERENCE
##*************************************
##https://www.geeksforgeeks.org/how-to-get-size-of-folder-using-python/
##
##*************************************
##Old Version
##*************************************
##
##size = 0
##folderpath = os.getcwd()
##for path, dirs, files in os.walk(folderpath):
##    for f in files:
##        fp = os.path.join(path, f)
##        size += os.path.getsize(fp)
##
##print("Folder size: " + str(size))
##
