import os

print(os.getcwd())

# os.unlink()
# deletes file 

# os.rmdir()
# deletes directories IF they are empty

# import shutil
# shutil.rmtree()
# deletes directory and ALL of its content


## should do a dry run using print function to see what youre deleting before running a program
# e.g:
#  for filename in os.listdir():
#       if filename.endswith():
#               os.unlink() ----> during dry run comment delete related line out and just run with print first
#          print(filename)




# All above deletions are permanent. Can import third party module send2trash to instead delete files/folders to the Recycle Bin

# send2trash.send2trash()
