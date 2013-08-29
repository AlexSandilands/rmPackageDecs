# Pass the directory you want edited as a command line argument.
# This script will find all java files in that directory and
# all subdirectories and will remove the package declaration (if there is one).

import sys
from os import walk

if len(sys.argv) < 2:
    print("Pass in the directory you want to purge as a command line argument.")
    sys.exit(0)

# Store the path to the directory
path = sys.argv[1]

# Create a list of the names of every file in the directory
# and all subdirectories
files = []
for (dirpath, dirnames, filenames) in walk(path):
    # Add the directory path to the front of the filenames
    pathsToFiles = [dirpath + "/" + f for f in filenames]
    files.extend(pathsToFiles)


for f in files:
    # Check if f is a java file
    if(f[-5:] == ".java"):
        lines = open(f, 'r').readlines()

        for x in range(0, len(lines)):
            if(lines[x][:7] == "package"):
                # Delete the line that has the package declaration
                del lines[x]
                break

            # If you find the word "public", there must have been no package
            # declaration, so break
            if(lines[x][:6] == "public"):
                break


        fw = open(f, 'w')

        # Write the lines back into the file
        for line in lines:
            fw.write(line)

        fw.close()