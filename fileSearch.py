# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 13:14:50 2016

@author: Tanner Parker
"""

import sys
import os
import shutil
from send2trash import send2trash
import tkinter
from tkinter.filedialog import askdirectory

# takes an empty list and a directory and walks it to fill the list.
def findMatches(List, directory):
    for root, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            if choice == 1:
                if filename.endswith(imageExtensions):
                    List.append(os.path.join(root, filename))
                    print ("Match found")
            elif choice == 2:
                if filename.endswith(wordExtensions):
                    List.append(os.path.join(root, filename))
                    print ("Match found")
            elif choice == 3:
                if filename.endswith(videoExtensions):
                    List.append(os.path.join(root, filename))
                    print ("Match found")
            elif choice == 4:
                if filename.endswith(audioExtensions):
                    List.append(os.path.join(root, filename))
                    print ("Match found")
            elif choice == 5:
                if filename.endswith('.jpg'):
                    List.append(os.path.join(root, filename))
                    print ("Match found")
            elif choice == 6:
                if filename.endswith('.txt'):
                    List.append(os.path.join(root, filename))
                    print ("Match found")
            else:
                print ('You did not press a specified number.')
                sys.exit()

# method for copying a file with shutil
def copyFile(src, dest):
    try:
        shutil.copy2(src, dest)
    # eg. src and dest are the same file
    except shutil.Error as e:
        print('Error: %s' % e)
    # eg. source or destination doesn't exist
    except IOError as e:
        print('Error: %s' % e.strerror)

# method to call a gui to select a directory
# found at http://stackoverflow.com/questions/25282883/how-can-i-use-the-output-from-tkfiledialog-askdirectory-to-fill-a-tkinter-entry
def askForDirectory():
    root = tkinter.Tk()
    root.withdraw()
    dirname = askdirectory()
    return dirname

# takes a list of files and asks to specify a directory for the files to be moved to.
def moveFiles(List):
    print ('Specify directory path to move files into.')
    direc = askForDirectory()
    if not os.path.exists(direc):
            os.makedirs(direc)
    for x in List:
        try:
            copyFile(x, direc)
        except shutil.Error as e:
            print ('Error: %s' % e)
        except IOError as e:
            print ('Error: %s' % e.strerror)
    print ("Congrats, you moved all the files into %s" % direc)

# passed a list that it loops through and safely deletes
def deleteFiles(List):
    for m in List:
        send2trash(m)
    print ("You have now moved all the originals to the trash.")
    print ("Congrats!")               

######             START OF SCRIPT             ######

print ("This script is meant for scrubbing files of a specified type and listing them.")
print ("It also allows you to copy the files after collecting them into a folder of your choice.")
print ("Please enter a starting directory..")
myDir = askForDirectory()
print ('For image files then press 1', '\n','For Word files then press 2', '\n',
       'For video files then press 3', '\n','For audio files then press 4', '\n',
       'For .jpg files then press 5', '\n','For .txt files then press 6')
choice = int(input('Please enter your choice: '))
# make tuples to hold file extensions
imageExtensions = ('.jpg', '.png', '.bmp', '.gif')
wordExtensions = ('.odt', '.doc', '.docx')
videoExtensions = ('.mov', '.MOV', '.mpeg', '.mp4', '.avi', '.mkv', '.webm')
audioExtensions = ('.wav', '.mp3', '.ogg')
# You need somewhere to store whatever files your script finds with a matching file extension
# create a list to store successfull matches
matches = []
findMatches(matches, myDir)
if len(matches) == 0:
    print ('There were no files of the specified type within the directory you gave.')
    sys.exit()
else:
    print (matches)
    print ("Would you like to copy these to a new folder? Y or N?", '\n',
           "You can just press Enter to end the program.")
    answer = input()
    if answer == 'y' or 'Y':
        moveFiles(matches) # Move files to new folder
        print ("Would you like to delete the original files as well? Y or N?")
        finalAnswer = input()
        if finalAnswer == 'y' or 'Y':
            deleteFiles(matches)
        else:
            sys.exit()
    else:
        print ("You have chosen not to move the files to a new folder, goodbye.")
        sys.exit()
######            END OF SCRIPT           ######