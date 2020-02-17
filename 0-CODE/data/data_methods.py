# ------------------------------------------------------------------------------
# 	Copyright (C) 2019-2020 Kenny Bravo Rodriguez

# 	This program is distributed for free in the hope that it will be useful,
# 	but WITHOUT ANY WARRANTY; without even the implied warranty of
# 	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

# 	See the accompaning licence for more details.
# ------------------------------------------------------------------------------

""" This module implements methods to handle data """

#--- Imports
## Standard modules
from pathlib import Path
## My modules 
import config.config as config
#---

#--------------------------------------------------- Files (Down) 
def FFsWriteDict(oFile, idict, hDict=None):
	""" Write key, values pairs to the file 
		---
		oFile : open channel to write into
		idict : dict with the key - values pair
		hDict helper Dict for pretty print key values
	"""
	
	for k, v in idict.items():
		if hDict is None:
			j = k
		else:
			j = hDict[k] 
		oFile.write(str(j) + ':\t' + str(v) + "\n")
	oFile.write('\n')
	return True
#---

def FFsWriteList(oFile, iList):
	""" Write list into file 
		oFile : channel to write into
		iList : list to write into oFile
	"""

	lastL = len(iList)
	for k, i in enumerate(iList, start=1):
		li = '\t'.join(i)
		if k < lastL:
			oFile.write(str(li) + '\n')
		else:
			oFile.write(str(li))
	
	return True
#---

def FFsWriteLastLine(oFile):
	""" Write the last line in each file generated with the app 
		---
		oFile: channel two write into
	"""
	oFile.write(
		"File generated with\t" 
		+ config.name
		+ '\t' 
		+ config.version
	)
	return True
#---

def FFsWriteCSV(fileP, df, index=False):
	""" Writes a dataframe to csv formatted file 
		---
		fileP: path to the file (string or Path) or bufer
		df: data frame to be written (DF)
		index: write index columns (Boolean)
	"""
	if isinstance(fileP, Path):
		df.to_csv(str(fileP), sep='\t', na_rep='NA', index=index)
	else:
		df.to_csv(fileP, sep='\t', na_rep='NA', index=index)
	return True
#---
#--------------------------------------------------- Files (Up) 

#--------------------------------------------------- Strings (Down) 
def str2l(myStr, sep, stripOpt=True):
	""" Turns myStr into a list using sep to spearate characters and strip
		the individual cahracters or not
		---
		myStr : string to be splitted into a list (str)
		sep: character to use to split the string (str)
		stripOpt: strip list elements or not (boolean)
	"""
 #--- Split string
	myL = myStr.split(sep)
 #--- Strip list elements
	if stripOpt:
		for k, v in enumerate(myL):
			myL[k] = myL[k].strip()
	else:
		pass
 #--- Returns
	return [True, myL]
#---
#--------------------------------------------------- Strings (Up) 