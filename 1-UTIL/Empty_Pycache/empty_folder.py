"""
	This will travel all folders starting in the given root location.
	All files inside the given folder name will be deleted.
	For example, found all __pycache__ folders in a given root folder 
	(recursively) and delete all files inside the found __pychache__ folders.
"""
# Import
import os
from pathlib import Path

# Variables
root = Path('/Users/bravo/Dropbox/SCRIPTS/Tanja_Bange/Notebook-PeptideTxt-Fasta/CODE')
folder = ['__pycache__']

for dirRoot, dirName, dirFiles in os.walk(root, topdown=False):
	dirRootPath = Path(dirRoot)
	if dirRootPath.name in folder:
		for name in dirFiles:
			thefile = dirRootPath / name
			thefile.unlink() 
	else:
		pass


