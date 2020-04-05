import shutil as sh
import os

root_path = "./input"
dest_path = "./notebook"
 
try:
    os.mkdir(dest_path)
    print("Directory " , dest_path ,  " Created ") 
except FileExistsError:
    print("Directory " , dest_path ,  " Already Exists")


for dirpath, dnames, fnames in os.walk(root_path):    
    for f in fnames:
        if f.endswith(".ipynb"):
            source_file_path =  os.path.join(dirpath, f)
            dest_file_path   =  os.path.join(dest_path, f)
            sh.copyfile(source_file_path, dest_file_path)