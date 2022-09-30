import os
import subprocess

# This is a scripting module.
# It is to find all pictures of jpg, png, ... from one directory
# and copy it to another directory.
# Ultimately, it will search the whole drive then all the drives in a PC.
# It's main purpose is to search for all pictures in a PC with or without multiple
# drives.

os.chdir('\\Users\\Henry\\Desktop\\git\\')


def pr(something):
    print(something)


pr(os.listdir())

pr(os.name)
