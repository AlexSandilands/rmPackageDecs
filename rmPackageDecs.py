# Pass the directory you want edited as a command line argument.
# This script will find all java files in the directory and
# all subdirectories and remove the package declaration (if there is one).

import sys
from os import walk

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
    if(f[-4:] == ".txt"):
        lines = open(f, 'r').readlines()

        # Check if the first line has a package declaration
        # Edit this is the package declarations are somewhere other
        # than the first line, perhaps do a for loop over the first 10 lines,
        # or if it comes to it just loop until you find one.
        if(lines[0][:7] == "package"):
            # Delete the line that has the package declaration
            del lines[0]

        fw = open(f, 'w')

        # Write the lines back into the file
        for line in lines:
            fw.write(line)

        fw.close()