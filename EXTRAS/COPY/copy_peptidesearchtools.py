#region -------------------------------------------------------------> Imports
import platform
import shutil
import getpass

from distutils.dir_util import copy_tree
from pathlib            import Path
#endregion ----------------------------------------------------------> Imports

#region -----------------------------------------------------------> VARIABLES
cwd      = Path.cwd()
user     = getpass.getuser()
cOS      = platform.system()

if cOS == 'Darwin':
	pathF = '/Users/'  
	spec  = Path(pathF + user + '/Dropbox/SOFTWARE-DEVELOPMENT/APPS/PEPTIDE_SEARCH_TOOLS/GIT/RESOURCES/BUNDLE/MAC/PeptideSearchTools.spec')
else:
	pathF = 'C:/Users/'
	spec  = Path(pathF + user + '/Dropbox/SOFTWARE-DEVELOPMENT/APPS/PEPTIDE_SEARCH_TOOLS/GIT/RESOURCES/BUNDLE/WIN/PeptideSearchTools.spec')
	specH = Path(pathF + user + '/Dropbox/SOFTWARE-DEVELOPMENT/APPS/PEPTIDE_SEARCH_TOOLS/GIT/RESOURCES/BUNDLE/WIN/version.txt')

basePath = Path(
	pathF 
	+ user 
	+ '/Dropbox/SOFTWARE-DEVELOPMENT/APPS/PEPTIDE_SEARCH_TOOLS/GIT'
)
#--> FOLDERS TO COPY
source = basePath / 'CODE'
img    = basePath / 'RESOURCES/IMAGES'
lic    = basePath / 'RESOURCES/LICENSE'
#--> FILES TO COPY
licensetxt = basePath / 'License.txt'
#endregion --------------------------------------------------------> VARIABLES

#region ------------------------------------------------------> Ask permission
print("The content of folder:")
print(str(cwd))
print("will be deleted")
print("Are you sure about this?")
var = input("Y/N:")
#endregion ---------------------------------------------------> Ask permission

#region ---------------------------------------------------------------> Copy
if var == "Y" or var == "y":
 #--> DELETE PLAYGROUND
	print('')
	print('Deleting content of folder: ' + str(cwd))
	for item in cwd.iterdir():
		print('Deleting: ' + str(item)) 
		if item.is_dir():
			shutil.rmtree(item)
		else:
			item.unlink()
 #---
 #--> COPY FILES AND FOLDERS
  #--> CODE
	print('')
	print('Copying Peptide Search Tools files')
	copy_tree(str(source), str(cwd))
  #---
  #--> RESOURCE
   #--> CREATE FOLDER
	res = cwd / 'RESOURCES'
	res.mkdir()
   #---
   #--> IMAGES
	print('')
	print('Copying Resources: IMAGES')
	resI = res / 'IMAGES'
	copy_tree(str(img), str(resI))
   #---
   #--> IMAGES
	print('')
	print('Copying Resources: LICENSE')
	resI = res / 'LICENSE'
	copy_tree(str(lic), str(resI))
   #---   
  #---
  #--> SPEC
	print('')
	print('Copying Bundle spec files')		
	loc = cwd / spec.name
	shutil.copyfile(spec, loc)
	if cOS == 'Windows':
		loc = cwd / specH.name
		shutil.copyfile(specH, loc)		
	else:
		pass  
  #---
  #--> FINAL PRINT
	print("\nAll Done. Enjoy!!")
  #---
 #---
else:
 #--> QUIT
	print("You typed: " + var)
	print("Nothing will be done")
 #---
#endregion ------------------------------------------------------------> Copy


