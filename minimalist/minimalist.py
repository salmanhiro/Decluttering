import shutil as sh
import os
print("Every day you should RUN THIS SCRIPT every new program came!")
days = int(input("How many days since you commit? "))
root_path = "./input" #modify this line if needed
dest_path = "./json" #modify this line if needed
 
try:        
    os.mkdir(dest_path)
    print("Directory " , dest_path ,  " Created ")  
    for dirpath, dnames, fnames in os.walk(root_path):    
        for f in fnames:
            for i in range(days):
                if f.endswith(".json"): #modify this line if needed
                    source_file_path =  os.path.join(dirpath, f)
                    dest_file_path   =  os.path.join(dest_path, f)
                    sh.copyfile(source_file_path, dest_file_path)
except FileExistsError:
    print("Directory " , dest_path ,  " Already Exists, proceed to copy") 
    for dirpath, dnames, fnames in os.walk(root_path):    
        for f in fnames:
            for i in range(days):
                if f.endswith(".json"): #modify this line if needed
                    source_file_path =  os.path.join(dirpath, f)
                    dest_file_path   =  os.path.join(dest_path, f)
                    sh.copyfile(source_file_path, dest_file_path)


