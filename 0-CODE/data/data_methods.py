# ------------------------------------------------------------------------------
# Author: Kenny Bravo Rodriguez 2019 (kenny.bravorodriguez@mpi-dortmund.mpg.de)
# 
# Copyright (c) 2019-2020 Max Planck Institute of Molecular Physiology
#
# This complete copyright notice must be included in any revised version of the
# source code. Additional authorship citations may be added, but existing
# author citations must be preserved.
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
# ------------------------------------------------------------------------------


""" This module implements methods to handle data """


#--- Imports
from pathlib import Path 
import config.config as config
#---


#------------------------------------------------------------------------- Files
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
#------------------------------------------------------------------------- Files


#----------------------------------------------------------------------- Strings
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
#----------------------------------------------------------------------- Strings