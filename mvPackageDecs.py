# Pass the directory you want edited as a command line argument.
# This script will find all java files in that directory and
# all subdirectories and will copy them into a new folder, with
# their package declarations commented out

import sys
import os
from os import walk

def main():
    # Usability
    if len(sys.argv) < 2:
        print("Pass in the directory as a command line argument.")
        sys.exit(0)

    # Store the path to the directory
    path = sys.argv[1]

    # Create a list of the names of every file in the directory
    # and all subdirectories
    files = []

    for (dirpath, dirnames, filenames) in walk(path):
        # Add the directory path to the front of the filenames
        # and put the length of the file in a tuple with the path
        toAdd = [(dirpath + "/" + f, len(f)) for f in filenames]
        files.extend(toAdd)

        # If you don't want to check subdirectories, break here

    # Make a new folder if it doesn't already exist
    if not os.path.exists("./Moved_To"): os.makedirs("./Moved_To")


    for (f, l) in files:
        # Check if f is a java file
        if f[-5:] == ".java":
            lines = open(f, 'r').readlines()

            for x in range(0, len(lines)):

                # Comment the line that has the package declaration
                if lines[x][:7] == "package":
                    lines[x] = "// " + lines[x]
                    break


            fw = open("./Moved_To/" + f[-l:], 'w')

            # Write the lines back into a new file in the new directory
            for line in lines:
                fw.write(line)

            fw.close()

# End main function

if __name__ == '__main__':
    main()