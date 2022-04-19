

import shutil


#shutil.copy('C:\\Users\\burha\\MyPythonScripts\\TxtFiles\\spam.txt', 'C:\\Users\\burha\\MyPythonScripts\\CpyTxtFiles\\')

# copied spam.txt from TxtFiles to CpyTxtFiles folder using the shutil.copy method


#shutil.copy('C:\\Users\\burha\\MyPythonScripts\\TxtFiles\\spam.txt', 'C:\\Users\\burha\\MyPythonScripts\\CpyTxtFiles\\spamrenamed.txt')

# this time, copied but also renamed the copied file to spamrenamed, using the shutil.copy method


# shutil.copytree('C:\\Users\\burha\\MyPythonScripts\\TxtFiles', 'C:\\Users\\burha\\MyPythonScripts\\TxtFilesBackup')

# copied entire directory and contents (i.e made a backup folder of an existing folder)



#shutil.move('C:\\Users\\burha\\MyPythonScripts\\TxtFiles\\spam.txt', 'C:\\Users\\burha\\MyPythonScripts\\CpyTxtFiles\\')

# moved a file



shutil.move('C:\\Users\\burha\\MyPythonScripts\\TxtFiles\\spam.txt', 'C:\\Users\\burha\\MyPythonScripts\\TxtFiles\\spamrenamedusingmove.txt')

# renamed a file by using the same location and move method (move used as a method to rename existing file in its original location)
