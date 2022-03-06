import os

[os.rename(f, 'MSD-' + str(f)) for f in os.listdir('.')
 if not f.startswith('MSD')]


## ======================
## REFERENCE
## ----------------------
##
## https://stackoverflow.com/questions/30751918/renaming-multiple-files-in-a-folder-by-adding-prefix-using-python
