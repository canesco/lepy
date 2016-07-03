HOW TO USE THE SKELETON
========================

1. Make copy of skeleton directory. Name it after new project.
2. Rename (move) the NAME module to be the name of project or whatever.
3. Delete pyc-Files
4. Create module.py with (Class) methods and (def) functions/methods

5. Edit setup.py to have all the information for the project.
    - packages (file name without .py)
    - scripts (scripts to execute with code related to module)
    - name (module name for later import)

6. Rename tests/NAME_tests.py to module name.
7. Write tests
8. Double check it's all working by *nosetests*.
9. Start coding in module.py

=======================================================================
TESTING GUIDELINES
==================
- test files go to tests/ and are named xy_tests.py
- one test file for each module
- keep test cases (functions) short

========================================================================
CREATE AN ARCHIVE FILE FOR DISTRIBUTION
=======================================
terminal: python setup.py sdist (creating tar.gz for sharing)
--> download, unpack, install:

========================================================================
INSTALLING & USING THE PACKAGE
==============================
- go to directory
- python setup.py install
- scripts should now be callable from everywhere
- start python --> from package import module --> module.function(x,y) etc.

=========================================================================
REMOVING PACKAGE
================
pip uninstall *package*
