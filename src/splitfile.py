# Reference: https://thispointer.com/python-search-strings-in-a-file-and-get-line-numbers-of-lines-containing-the-string/
# Reference: https://stackoverflow.com/questions/14596884/remove-text-between-and

import re

line_copy = False
logs = ""

with open("test.txt",'r') as file:
    lines = file.readlines()

    for line in lines:
        if line_copy is True:
            logs += line
        if "Private Sub " in line:
            result = line.split(" ")[2].strip()    
            filename = re.sub("[\(].*", "", result) + ".bas"
            line_copy = True
            logs += line
        elif "Public Sub " in line:
            result = line.split(" ")[2].strip()    
            filename = re.sub("[\(].*", "", result) + ".bas"
            line_copy = True
            logs += line
        elif "Sub " in line:
            result = line.split(" ")[1].strip()    
            filename = re.sub("[\(].*", "", result) + ".bas"
            line_copy = True
            logs += line            
        if "Private Function " in line:
            result = line.split(" ")[2].strip()    
            filename = re.sub("[\(].*", "", result) + ".bas"
            line_copy = True
            logs += line                                                 
        elif "Function " in line:
            result = line.split(" ")[1].strip()    
            filename = re.sub("[\(].*", "", result) + ".bas"
            line_copy = True
            logs += line           
        if "End Sub" in line:
            with open(filename,'w') as file:
                    file.write(logs + "\n")
            line_copy = False
            logs = ""
        if "End Function" in line:
            with open(filename,'w') as file:
                    file.write(logs + "\n")
            line_copy = False
            logs = ""        