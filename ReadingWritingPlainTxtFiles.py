# reading / writing plaintext files

# all other files that are binary files (e.g: photo,word doc etc )

import os

print(os.getcwd())


helloFile = open('C:\\Users\\burha\\MyPythonScripts\\TxtFiles\\HelloWorldx3.txt')

# returns a file object which is stored in helloFile. The file datatype has various useful methods
# open() on its own by default opens file in READ MODE. can use open(,'w') to open and write or open(,'a') to open and only append

print(helloFile.read())
print(helloFile.readlines())
helloFile.close()

### above readlines doesn't work!!! This is because you have to re-open file and re-read it as you can only
### perform read once, once the file has been opened using open()



helloFile = open('C:\\Users\\burha\\MyPythonScripts\\TxtFiles\\HelloWorldx3.txt')
content = helloFile.read()
print(content)
helloFile.close()

helloFile = open('C:\\Users\\burha\\MyPythonScripts\\TxtFiles\\HelloWorldx3.txt')
content2 = helloFile.readlines()
print(content2)
helloFile.close()


#### this time it works because of separate open,read,close chunks

helloFile2 = open('C:\\Users\\burha\\MyPythonScripts\\TxtFiles\\HelloWorldx32.txt', 'w')
helloFile2.write("Hello write mode file")
helloFile2.close()
helloFile2 = open('C:\\Users\\burha\\MyPythonScripts\\TxtFiles\\HelloWorldx32.txt')
print(helloFile2.read())
helloFile2.close()


### in above, a whole new file was created and we wrote something within it using WRITE mode
### we then had to close and open the file in read mode to print its contents
### alternatively, the file can be opened from windows explorer to look at its contents

helloFile3 = open('C:\\Users\\burha\\MyPythonScripts\\TxtFiles\\HelloWorldx33.txt', 'w')
helloFile3.write("Hello write mode file")
helloFile3.close()

helloFile3 = open('C:\\Users\\burha\\MyPythonScripts\\TxtFiles\\HelloWorldx33.txt', 'a')
helloFile3.write("\n This sentence has been appended post newline")
helloFile3.close()

helloFile3 = open('C:\\Users\\burha\\MyPythonScripts\\TxtFiles\\HelloWorldx33.txt')
print(helloFile3.read())
helloFile3.close()


### for above, first a new file was created with some initial content
### then, using APPEND mode, additional content was added to end of the file
### finally the contents were opened in read mode and printed to screen


import shelve

shelfFile = shelve.open('mydata')

# above shelve module lets you create shelf files which can hold more complex structures such as dictionaries and lists
# you can set these shelfFiles aside and use as necessary when you need employ structures like dicts etc
# in above we've created mydata shelfFile in cwd


shelfFile['cats'] = ['Betty', "Louie", "NalaTesco", "Broderick"]
shelfFile.close()

## can create dict structure as above using dict syntax
## then similar to txt files, you can close after its been opened/read or edited etc
## assume that similar to read() you can only do whatever you want to do to the file once


shelfFile = shelve.open('mydata')
print(shelfFile['cats'])
shelfFile.close()

# above you are just opening a shelf file using shelve module and storing that object into ShelfFile
# and you are specifying the key to the dictionary to print out the returning value pair
## When you create a shelfFile you will notice three extensions being created : .BAK , .DAT , .DIR

shelfFile = shelve.open('mydata')
valuesList = list(shelfFile.values())
keysList = list(shelfFile.keys())
itemsList = list(shelfFile.items())

print(valuesList, '\n', keysList, '\n', itemsList)
shelfFile.close()


### in above we have retrieved keys,values and items from dictionary and converted to list and printed output











