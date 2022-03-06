# References
# https://www.geeksforgeeks.org/access-metadata-of-various-audio-and-video-file-formats-using-python-tinytag-library/
# https://www.codegrepper.com/code-examples/python/how+to+save+python+output+to+csv+file
# https://www.geeksforgeeks.org/python-os-listdir-method/



import os
import csv
from tinytag import TinyTag
from datetime import timedelta

path = os.getcwd()

with open('metadata.csv', 'w', encoding='UTF8', newline='') as csvfile:
    fieldnames = ['filename', 'duration']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for filename in os.listdir(path):
        if filename.endswith(".mp4"):
            video = TinyTag.get(filename)
            writer.writerow({'filename': filename, 'duration': timedelta(seconds=int(video.duration))})
            continue
        else:
            continue


# WIP
# Cycle through directories from a root directory
# https://stackoverflow.com/questions/19587118/iterating-through-directories-with-python

##import os
##rootdir = 'C:/Users/sid/Desktop/test'
##
##for subdir, dirs, files in os.walk(rootdir):
##    for file in files:
##        print os.path.join(subdir, file)
