# ------------------------------------------------------------------------------
# Author: Kenny Bravo Rodriguez 2019 (kenny.bravorodriguez@mpi-dortmund.mpg.de)
# 
# Copyright (c) 2019 Max Planck Institute of Molecular Physiology
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

"""Individuals tabs for the App
"""

#region -------------------------------------------------------------- Imports
import wx

import config.config as config
import gui.widget as pstWidget
#endregion ----------------------------------------------------------- Imports

#region -------------------------------------------------------> Base Classess
class BaseTab():
	"""Base Tab for the application.

		Contains the wx.StaticBox, wx.StaticBoxSizer and Button at the tops.
		The rest of the GUI elements are added in the child classess

		Parameters
		----------
		parent: wx widget
			Parent of the widgets

		Attributes
		----------
		sbFile : wx.StaticBox
			StaticBox to contain the input/output file information
		sbValue : wx.StaticBox
			StaticBox to contain the user-defined values
		sbColumn : wx.StaticBox
			StaticBox to contain the column numbers in the input files
		btnGroup : pstWidget.ButtonGroup
			Contains the three buttons at the bottom of each tab
		sizersbFile : wx.StaticBoxSizer
			StaticBoxSizer for sbFile
		sizersbFileWid : wx.FlexGridSizer
			FlexGridSizer for widgets in sbFile
		sizersbValue : wx.StaticBoxSizer
			StaticBoxSizer for sbValue
		sizersbValueWid : wx.FlexGridSizer
			FlexGridSizer for widgets in sbValue
		sizersbColumn : wx.StaticBoxSizer
			StaticBoxSizer for sbColumn
		sizersbColumnWid : wx.FlexGridSizer
			FlexGridSizer for widgets in sbColumn
	"""

	#region -----------------------------------------------------> Class setup
	#endregion --------------------------------------------------> Class setup	

	#region --------------------------------------------------> Instance setup
	def __init__(self, parent):
		""""""
		#region -----------------------------------------------> Initial setup

		#endregion --------------------------------------------> Initial setup

		#region -----------------------------------------------------> Widgets
		#--> wx.StaticBox
		self.sbFile = wx.StaticBox(
			parent, 
			label=config.label['BaseTab']['File'],
		)
		self.sbValue = wx.StaticBox(
			parent, 
			label=config.label['BaseTab']['Value'],
		)
		self.sbColumn = wx.StaticBox(
			parent, 
			label=config.label['BaseTab']['Column'],
		)
		#--> wx.Buttons
		self.btnGroup = pstWidget.ButtonGroup(parent)
		#endregion --------------------------------------------------> Widgets

		#region ------------------------------------------------------> Sizers
		self.sizersbFile    = wx.StaticBoxSizer(self.sbFile, wx.VERTICAL)
		self.sizersbFileWid = wx.FlexGridSizer(3, 2, 1, 1)
		self.sizersbFile.Add(
			self.sizersbFileWid,  
			border = 2,
			flag   = wx.EXPAND|wx.ALL
		)
		self.sizersbValue    = wx.StaticBoxSizer(self.sbValue, wx.VERTICAL)
		self.sizersbValueWid = wx.FlexGridSizer(3, 2, 1, 1)
		self.sizersbValue.Add(
			self.sizersbValueWid,  
			border = 2,
			flag   = wx.EXPAND|wx.ALL
		)
		self.sizersbColumn    = wx.StaticBoxSizer(self.sbColumn, wx.VERTICAL)
		self.sizersbColumnWid = wx.FlexGridSizer(3, 2, 1, 1)
		self.sizersbColumn.Add(
			self.sizersbColumnWid,  
			border = 2,
			flag   = wx.EXPAND|wx.ALL
		)
		#endregion ---------------------------------------------------> Sizers
	#endregion -----------------------------------------------> Instance setup
#---
#endregion ----------------------------------------------------> Base Classess

#region ------------------------------------------------------------> Classess
class Peptide(wx.Panel, BaseTab):
	"""Tab to perform the peptide search analysis 
		
		Parameters
		----------

		Attributes
		----------

		Raises
		------
	"""

	#region -----------------------------------------------------> Class setup
	#endregion --------------------------------------------------> Class setup	

	#region --------------------------------------------------> Instance setup
	def __init__(self, parent, name):
		""""""
		#region -----------------------------------------------> Initial setup
		wx.Panel.__init__(self, parent, name=name)
		BaseTab.__init__(self, self)
		#endregion --------------------------------------------> Initial setup

		#region -----------------------------------------------------> Widgets
		
		#endregion --------------------------------------------------> Widgets

		#region ------------------------------------------------------> Sizers
		self.Sizer = wx.GridBagSizer(1, 1)
		self.Sizer.Add(
			self.sizersbFile,
			pos    = (0,0),
			flag   = wx.EXPAND|wx.ALL,
			border = 2
		)
		self.Sizer.Add(
			self.sizersbValue,
			pos    = (1,0),
			flag   = wx.EXPAND|wx.ALL,
			border = 2
		)
		self.Sizer.Add(
			self.sizersbColumn, 
			pos    = (2,0),
			flag   = wx.EXPAND|wx.ALL,
			border = 2
		)
		self.Sizer.Add(
			self.btnGroup.Sizer,
			pos    = (3,0),
			flag   = wx.ALIGN_CENTER|wx.ALL,
			border = 2
		)
		self.Sizer.AddGrowableCol(0, 1)
		#endregion ---------------------------------------------------> Sizers
	#endregion -----------------------------------------------> Instance setup
#---
#endregion ---------------------------------------------------------> Classess