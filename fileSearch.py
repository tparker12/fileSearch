# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 13:14:50 2016

@author: Tanner Parker
"""

import sys
import os
import shutil

# imports for dialogue boxes
import tkinter
# from tkinter import filedialog
from tkinter.filedialog import askdirectory

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
    # root = Tkinter.Tk()
    root = tkinter.Tk()
    # withdraw() allows the window to dissapear 
    # found at https://www.daniweb.com/programming/software-development/threads/210657/open-directory-dialog-box
    root.withdraw()
    # dirname = tkFileDialog.askdirectory()
    dirname = askdirectory()
    return dirname

# /home/tanner/Desktop/firstFolder

print ("This script is meant for scrubbing files of a specified type and listing them.")
print ("It also allows you to copy the files after collecting them into a folder of your choice.")

print ("Please enter a starting directory..")
directory = askForDirectory()
#directory = raw_input()

print ('For image files then press 1')
print ('For Word files then press 2')
print ('For video files then press 3')
print ('For audio files then press 4')
print ('For .jpg files then press 5')
print ('For .txt files then press 6')
choice = int(input('Please enter your choice: '))

# variables to hold custom paths...this is meant to be used later on.
desktop = '/home/tanner/Desktop/'
school = '/home/tanner/Desktop/School'
pictures = '/home/tanner/Pictures'
videos = '/home/tanner/Videos'

# make tuples to hold file extensions
imageExtensions = ('.jpg', '.png', '.bmp', '.gif')
# tuple to hold word doc extensions
wordExtensions = ('.odt', '.doc', '.docx')
# tuple for video extensions
videoExtensions = ('.mov', '.MOV', '.mpeg', '.mp4', '.avi', '.mkv')
# tuple for audio extensions
audioExtensions = ('.wav', '.mp3', '.ogg')

# create a list to store successfull matches
matches = []

for root, dirnames, filenames in os.walk(directory):
    for filename in filenames:
        if choice == 1:
            if filename.endswith(imageExtensions):
                matches.append(os.path.join(root, filename))
        elif choice == 2:
            if filename.endswith(wordExtensions):
                matches.append(os.path.join(root, filename))
        elif choice == 3:
            if filename.endswith(videoExtensions):
                matches.append(os.path.join(root, filename))
        elif choice == 4:
            if filename.endswith(audioExtensions):
                matches.append(os.path.join(root, filename))
        elif choice == 5:
            if filename.endswith('.jpg'):
                matches.append(os.path.join(root, filename))
        elif choice == 6:
            if filename.endswith('.txt'):
                matches.append(os.path.join(root, filename))
        else:
            print ('You did not press a specified number.')
            sys.exit()
# if the list is empty say so..these are new changes.
if len(matches) == 0:
    print (len(matches))
    print ('There were no files of the specified type within the directory you gave.')
else:
    print (matches)
    print ("Would you like to copy these to a new folder? Y or N?")
    answer = input()
    if answer == 'y' or 'Y':
        print ('Specify directory path to move files into.')
        direc = askForDirectory()
        #print 'Note: The folder you specify will be created on the Desktop.'
        #newDir = raw_input()
        # concatenates the specified folder with the path to the desktop
        #newDir1 = desktop + newDir
        # checks that the directory doesn't already exist, if not; makes it.
        if not os.path.exists(direc):
            os.makedirs(direc)
        # loops through the list of matches and copy's them to the new folder.
        for x in matches:
            copyFile(x, direc)
        print ("Congrats, you moved all the files into %s" % direc)
        sys.exit()
    else:
        print ("You have chosen not to move the files to a new folder, goodbye.")
        sys.exit()