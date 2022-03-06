import os
path = os.getcwd()
files = os.listdir(path)

## rename downloaded youtube files
for index, file in enumerate(files):
    nameparts = file.split(" [")[0] + ".mp4"
    newfilename = nameparts.split(" ",1)[0] + "." + nameparts.split(" ",1)[1]
    os.rename(os.path.join(path, file), os.path.join(path, newfilename))

## WIP
## ===============================================
## original_name = "snackbox_12.dat"
## truncated_name = original.split("_")[0] + ".dat"
## 
## for index, file in enumerate(files):
##     os.rename(os.path.join(path, file), os.path.join(path, ''.join([str(index), '.jpg'])))
