__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

import shutil
import os
from zipfile import ZipFile

path = os.getcwd()
data_path = os.path.join(path,"data.zip")
cache_path = os.path.join(path,'cache')

# 1 EXERCISE
def clean_cache ():
    check_folder = os.path.isdir('cache') # checking if the directory cache, exists or not. 
    if check_folder:                                
        shutil.rmtree(cache_path)                  
        os.mkdir(cache_path)
    else: 
       os.mkdir (cache_path)

#print(clean_cache())

# 2 EXERCISE

def cache_zip(file_path, dir_path):

    with ZipFile(file_path, 'r') as zip: 
        zip.extractall(dir_path)
        
#print(cache_zip(data_path, cache_path))

# 3 EXERCISE

def cached_files(): 

    path= 'C:/Users/lesty/OneDrive/Desktop/WincAcademy/print/files/cache/' #absolute path
    files_cache = os.listdir(path)
    files_dir = list()
    for file in files_cache:
        file_path = f"{path}{file}"
        files_dir.append(file_path)

    return files_dir #returns a list of all the file paths in the cache

#print(cached_files())

# 4 EXERCISE

paths_list = cached_files()

def find_password(paths_list):

    for file in paths_list:
        if 'password' in open (file,'r').read():
            for count_item, value in enumerate (open(file,'r')):
                if 'password' in value:
                    password = (value[value.find(" "):][1:])
                    return password

print(find_password(paths_list))

