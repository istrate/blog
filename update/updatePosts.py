# importing os module
import os
 
# importing shutil module
import shutil
 
# path
path = '/opt/app-root/src/update'
 
# List files and directories
print("Before moving file:")
print(os.listdir(path))
 
 
# Assign source and destination
source = '/opt/app-root/src/update'
destination = '/opt/app-root/src'
 
sourcePath = path+'/'+source
destinationPath = path+'/'+destination
 
# Check if file already exists
if os.path.isdir(destinationPath+'/'+source):
    print(source, 'exists in the destination path!')
    shutil.rmtree(destinationPath+'/'+source)
     
elif os.path.isfile(destinationPath+'/'+source):
    os.remove(destinationPath+'/'+source)
    print(source, 'deleted in', destination)
 
# Move the content
# source to destination
dest = shutil.move(sourcePath, destinationPath)
 
# List files and directories
print("After moving file:")
print(os.listdir(path))
 
print(source, 'has been moved!')
 
# Print new path of file
print("Destination path:", dest)
