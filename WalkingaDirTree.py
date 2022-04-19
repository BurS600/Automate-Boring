import os, pprint

i = 0
j = 0

for folderName, subfolders, filenames in os.walk('C:\\Users\\burha\\MyPythonScripts'):
    pprint.pprint(' The folder is: ' + folderName)
    pprint.pprint(' The subfolders in: ' + folderName + ' are: ' + str(subfolders))
    # remember subfolders and filenames are returned as lists
    pprint.pprint(' The filenames in: ' + folderName + ' are: ' + str(filenames))
    print()

    for subfolder in subfolders:
        i += 1
    pprint.pprint( 'The subfolders in above iteration of the walk equal to: ' + str(i))
    i = 0

    for files in filenames:
        j += 1
    pprint.pprint( 'The files in above iteration of the walk equal to: ' + str(j))
    print()
    j = 0



            
# for subfolder in subfolders:
# if 'fish' in subfolder:
   # os.rmdir(subfolder)


# for file in filenames:
# if file.endswith('.py'):
# shutil.copy(os.path.join(folderName, file), os.join(folderName, file + '.backup')

# remember need to to use absolute paths for above .copy function
# the shutil functions you have come across all need absolute paths to know which file to move/copy to where etc.









    
        

            
