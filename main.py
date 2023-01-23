__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

import shutil
import os
from zipfile import ZipFile

path= os.getcwd() #This function of the Python OS module returns the string containing the absolute path to the current working directory. Always assign the names of the parameters as they are assigned in the modules.
dir = 'cache'
Cache_dir= os.path.join (path,dir)

# 1 EXERCISE
def clean_cache ():
   
   check_folder = os.path.isdir('cache') #----->   # checking if the directory cache, exist or not. 
   if check_folder:                                
        shutil.rmtree (Cache_dir)                  
        #print("% s has been removed successfully" % dir)     
        os.mkdir(Cache_dir)
        #print("% s has been created successfully" % dir) # print with % is similar to f'string' syntax for linking string and variables.

#print (clean_cache())

# 2 EXERCISE

file_path = os.path.join (path,"data.zip")

def cache_zip (file_path, dir_path):

    with ZipFile(file_path, 'r') as zip:  #r: mode metadata_encoding => https://docs.python.org/3/library/zipfile.html
        zip.extractall(dir_path)
        #print('Done!')
    
#print (cache_zip(file_path,Cache_dir))

# 3 EXERCISE

def cached_files ():

    files_cache= os.listdir (Cache_dir) # cache_dir is already an absolute path
    return files_cache

#print (cached_files())


# 4 EXERCISE

def find_password(file_paths):
     
    open_gate1= os.listdir (file_paths) #got a file list
    
    for file in open_gate1:
        gate2= os.path.join(file_paths,file)
        open_gate2= open (gate2,'r') # got just 1 file
        if 'password' in open_gate2.read():
            #print (file)
            open_gate3= open(gate2,'r') # got the one that has the password
            
            for count_item, value in enumerate (open_gate3):
                if 'password' in value:
                    password = (value[value.find(" "):][1:])

    return password
print (find_password(Cache_dir))






         
    
