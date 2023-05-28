# py-copy-directory-structure

## Purpose
The program copies a source directory structure without copying the exact "files", just the "folders".

Note: The results directory is a demonstration of the result. The <code>dummy.txt</code> files in the results folder are for github upload purpose only as github doesn't upload empty folders.

## Instructions
### Prerequisites:
- PySimpleGUI
    <pre> pip3 install pysimplegui </pre>
- py2app (only needed for conversion to Mac application)
    <pre> pip3 install py2app </pre>

### Run without packing
    python3 -m CopyDirectoryStructure

### Compilation to application file for Mac
    python3 setup.py py2app
    
## Application screenshot
<img width="1543" alt="Screenshot 2023-05-28 at 2 04 42 AM" src="https://github.com/darwindev2002/py-copy-directory-structure/assets/44953914/8597b7f7-7622-47fd-902e-e1b4bbed3676">
