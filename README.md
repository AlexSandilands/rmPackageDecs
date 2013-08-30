rmPackageDecs
=============

This is a python script I wrote when marking computer science assignments. 
It removes all the package declarations in all files in a directory 
(including subdirectories) in order to be able to edit and recompile code from the command line easier.

Usability
-------------

$ python rmPackageDecs.py [directory] [undo]

This will comment out every package declaration in directory.

The undo is optional, if you want to uncomment the previously commented 
package declarations then use undo as a second argument.
