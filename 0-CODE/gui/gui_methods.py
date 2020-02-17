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


""" This module contains methods related to the GUI of the app """


#--- Imports
import wx

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