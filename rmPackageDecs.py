# Pass the directory you want edited as a command line argument.
# This script will find all java files in that directory and
# all subdirectories and will comment out the package declaration
# (if there is one).
# Use "undo" as a second command line argument to uncomment the
# package declarations.

import sys
from os import walk

# Usability
if len(sys.argv) < 2:
    print("Pass in the directory to purge as a command line argument.")
    print("If you want to undo the purge, add \"undo\" as a second argument.")
    sys.exit(0)

# Store the path to the directory
path = sys.argv[1]
undo = ""

# Check if user wants to undo the purging
if len(sys.argv) == 3 and sys.argv[2] == "undo":
    undo = "undo"

# Create a list of the names of every file in the directory
# and all subdirectories
files = []

for (dirpath, dirnames, filenames) in walk(path):
    # Add the directory path to the front of the filenames
    pathsToFiles = [dirpath + "/" + f for f in filenames]
    files.extend(pathsToFiles)
    # If you don't want to check subdirectories, break here


for f in files:
    # Check if f is a java file
    if f[-5:] == ".java":
        lines = open(f, 'r').readlines()

        for x in range(0, len(lines)):

            # Comment the line that has the package declaration if "undo" was
            # not passed as an argument
            if lines[x][:7] == "package" and undo != "undo":
                lines[x] = "// " + lines[x]
                break

            # Uncomment the package declaration if undo was an argument
            if lines[x][:10] == "// package" and undo == "undo":
                lines[x] = lines[x][3:]

            # If you find the word "public", there must have been no package
            # declaration, so break
            if(lines[x][:6] == "public"):
                break


        fw = open(f, 'w')

        # Write the lines back into the file
        for line in lines:
            fw.write(line)

        fw.close()