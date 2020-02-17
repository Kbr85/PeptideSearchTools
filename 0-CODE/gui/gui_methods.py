# ------------------------------------------------------------------------------
# 	Copyright (C) 2019-2020 Kenny Bravo Rodriguez

# 	This program is distributed for free in the hope that it will be useful,
# 	but WITHOUT ANY WARRANTY; without even the implied warranty of
# 	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

# 	See the accompaning licence for more details.
# ------------------------------------------------------------------------------

""" This module contains methods related to the GUI of the app """

#--- Imports
## Standard modules
import wx
## My modules
import config.config as config
#---


def WinMainTypeCreate(winID):
	""" Creates the main like windows in the GUI.
		---
		winID : config.winName[key]
	"""

 #--> Create window or Raise already created window
	if config.win[winID] is None:
		config.win[winID] = config.pointer['gmethods']['WinCreate'][winID]()
		config.win['Open'].append(config.win[winID])
		config.win[winID].Raise()
	else:
		config.win[winID].Iconize(False)
		config.win[winID].Raise()
 #--> Return
	return True	
#---

def TabSelect(tabID):
	""" Creates the main window and change to the selected tab """
	
 #--- Creates the main window, just in case it was deleted
	WinMainTypeCreate(config.winName['main'])
 #--- Select the peptide Tab
	config.win[config.winName['main']].notebook.ChangeSelection(tabID)

	return True
#---