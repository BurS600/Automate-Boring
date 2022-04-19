import os

print(os.path.join('folder1','folder2','folder3','file.png'))
# makes a file path using the os appropriate separator which is stored in os.sep

print(os.getcwd())
# returns string of cwd

os.chdir('C:\\')
print(os.getcwd()) 
# changes current working directory

# . this folder ; .. means parent folder


os.chdir(r'C:\Users\burha\MyPythonScripts')
print(os.getcwd())
print(os.path.abspath('AbsandRelativeFilePaths.py'))

# passing a file from cwd into os.path.abspath() returns the absolute path N.B: to put filename in quotes


print(os.path.isabs('burha\MyPythonScripts'))

# boolean check to see if filepath is absolute

print(os.path.relpath('C:\\Users\\burha\\MyPythonScripts','C:\\Users'))

#provides relative path between two provided path (with the second path being cwd or frame of reference)


print(os.path.dirname(r'C:\Users\burha\MyPythonScripts\AbsandRelativeFilePaths.py'))
# returns directory path

print(os.path.basename(r'C:\Users\burha\MyPythonScripts\AbsandRelativeFilePaths.py'))

# returns basename file or folder i.e the last most file or folder name in path location


print(os.path.exists('C:\\Users\\RandomNonExistentFolder'))

print(os.path.exists('C:\\Users\\burha\\MyPythonScripts'))

# above checks if folder or file actually exists


print(os.path.isdir('C:\\Users\\burha\\MyPythonScripts'))
print(os.path.isfile('C:\\Users\\burha\\MyPythonScripts'))

#above two check if path provided is folder or a file respectively

print(os.path.getsize('C:\\Users\\burha\\MyPythonScripts'))
print(os.path.getsize('C:\\windows\\system32\\calc.exe')) # calculator tool size

# retrieves size of provided folder or file in bytes

print(os.listdir('C:\\Users\\burha\\MyPythonScripts'))

## OS.LISTDIR (notice its not within path module but rather os module itself) returns all the directories within given path




### Small program to retrieve total size of all files within a folder

TotalDirSize = 0
print('TotalDirSize:' + str(TotalDirSize))
for dir in os.listdir('C:\\Users\\burha\\MyPythonScripts'):
    if not os.path.isfile(os.path.join('C:\\Users\\burha\\MyPythonScripts\\',dir)):
        continue
    TotalDirSize = TotalDirSize + os.path.getsize(os.path.join('C:\\Users\\burha\\MyPythonScripts\\',dir))

print('TotalDirSize after loop:    ' + str(TotalDirSize))
print('Size of MyPythonScripts :   '+ str(os.path.getsize('C:\\Users\\burha\\MyPythonScripts')))







### finally can use os.makedirs('C:\\ etc etc') and python will create all those folders for you in the specified path


















