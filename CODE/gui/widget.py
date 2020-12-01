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

"""Classes and methods to create GUI elements formed by more than one widget 
from wxPython or one widget with a fairly complicated initialization process.
"""

#region -------------------------------------------------------------> Imports
import _thread
from datetime import datetime

import wx

import dat4s_core.widget.wx_widget as dtsWidget
import dat4s_core.widget.wx_window as dtsWindow

import config.config as config
#endregion ----------------------------------------------------------> Imports

#region ------------------------------------------------------------> Classes
class UserInput():
	"""Skeleton for the user input region of the tabs in the application.

		Contains the wx.StaticBox, wx.StaticBoxSizer and Control buttons.
		The rest of the GUI elements are added in the child Classes.

		Parameters
		----------
		parent: wx widget
			Parent of the widgets

		Attributes
		----------
		deltaT : str
			Elapsed time of self.Run
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

		Methods
		-------
		OnRun(event)
			Start new thread to run the analysis
		Run(test)
			Run the steps of the analysis
		CheckInput()
			Check user input. Override as needed.
		PrepareRun()
			Set variables and prepare data for analysis. Override as needed.
		RunAnalysis()
			Run the actual analysis. Override as needed.
		WriteOutput()
			Write output files. Override as needed.
		LoadResults()
			Load results. Override as needed.
		EndRun()
			Restart GUI and variables. Override as needed.
	"""

	#region -----------------------------------------------------> Class setup
	#endregion --------------------------------------------------> Class setup	

	#region --------------------------------------------------> Instance setup
	def __init__(self, parent):
		""""""
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
		self.btnGroup = ButtonGroup(parent)
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

		self.sizersbFileWid.AddGrowableCol(1, 1)
		self.sizersbValueWid.AddGrowableCol(1, 1)
		self.sizersbColumnWid.AddGrowableCol(1, 1)
		#endregion ---------------------------------------------------> Sizers

		#region --------------------------------------------------------> Bind
		self.btnGroup.btnRun.Bind(wx.EVT_BUTTON, self.OnRun)
		#endregion -----------------------------------------------------> Bind
	#---
	#endregion -----------------------------------------------> Instance setup

	#region ---------------------------------------------------> Class methods
	def OnRun(self, event):
		""" Start new thread to run the analysis
		
			Parameter
			---------
			event : wx.Event
				Receive the button event
		"""
		#region -------------------------------------------------> GUI changes
		self.btnGroup.btnRun.Disable()
		self.btnGroup.btnRun.SetLabel('Running')
		self.runEnd = False
		#endregion ----------------------------------------------> GUI changes
	
		#region ------------------------------------------------------> Thread
		_thread.start_new_thread(self.Run, ('test',))
		#endregion ---------------------------------------------------> Thread

		return True
	#---

	def Run(self, test):
		"""Run the analysis's steps

			Messages to the status bar of the app can be set in the individual
			step methods
		
			Parameters
			----------
			test: str
				Just needed by _thread.start_new_thread
		"""
		start = datetime.now()

		#region -------------------------------------------------> Check input
		if self.CheckInput():
			pass
		else:
			self.runEnd = False
			wx.CallAfter(self.RunEnd)
			return False
		#endregion ----------------------------------------------> Check input

		#region -------------------------------------------------> Prepare run
		if self.PrepareRun():
			pass
		else:
			self.runEnd = False
			wx.CallAfter(self.RunEnd)
			return False
		#endregion ----------------------------------------------> Prepare run

		#region ------------------------------------------------> Run analysis
		if self.RunAnalysis():
			pass
		else:
			self.runEnd = False
			wx.CallAfter(self.RunEnd)
			return False
		#endregion ---------------------------------------------> Run analysis

		#region ------------------------------------------------> Write output
		if self.WriteOutput():
			pass
		else:
			self.runEnd = False
			wx.CallAfter(self.RunEnd)
			return False
		#endregion ---------------------------------------------> Write output

		#region ------------------------------------------------> Load results
		if self.LoadResults():
			pass
		else:
			self.runEnd = False
			wx.CallAfter(self.RunEnd)
			return False
		#endregion ---------------------------------------------> Load results

		end = datetime.now()
		self.deltaT = datetime.utcfromtimestamp(
			(end-start).total_seconds()
		).strftime("%H:%M:%S")

		#region -------------------------------------------------> Restart GUI
		self.runEnd = True
		wx.CallAfter(self.RunEnd)
		return True
		#endregion ----------------------------------------------> Restart GUI
	#---

	def CheckInput(self):
		"""Check user input. Override as needed """
		return True
	#---

	def PrepareRun(self):
		"""Set variable and prepare data for analysis. Override as needed """
		return True
	#---

	def RunAnalysis(self):
		"""Run the actual analysis. Override as needed """
		return True
	#---

	def WriteOutput(self):
		"""Write output. Override as needed """
		return True
	#---

	def LoadResults(self):
		"""Load results. Override as needed """
		return True
	#---

	def RunEnd(self):
		"""Restart GUI and needed variables. This is a minimal implementation. 
			Override as needed 
		"""
		#region ---------------------------------------------------------> Msg
		if self.runEnd:
			dtsWindow.MessageDialog(
				'success', 
				f"{config.msg['Success']}\n\nElapsed time: {self.deltaT}",
				parent = self.parent,
			)
		else:
			pass
		#endregion ------------------------------------------------------> Msg
	 	#region -------------------------------------------------> Restart GUI
		self.btnGroup.btnRun.Enable()
		self.btnGroup.btnRun.SetLabel(config.label['ButtonGroup']['Run'])
		self.statusbar.SetStatusText("")
		if self.runEnd:
			#--> Remove value of Output File to avoid overwriting it
			self.outFile.tc.SetValue("")
		else:
			pass
		#endregion ----------------------------------------------> Restart GUI

		#region -------------------------------------------> Restart variables
		self.runEnd = False
		#endregion ----------------------------------------> Restart variables
		return True
	#---
	#endregion ------------------------------------------------> Class methods
#---

class ButtonGroup():
	"""Group of three buttons at the bottom of the tabs. This includes the run
		button. 
		
		Parameters
		----------
		parent : wx widget
			Parent of the widgets

		Attributes
		----------
		parent : wx widget
			Parent of the buttons. It is assume to be the top parent of the 
			windows where the buttons will be placed
		btnClear : wx.Button
			Button bound to self.OnClear
		btnRun : dtsWidget.BtnRun 
			Button to start the analysis
		Sizer : wx.FlexGridSizer
			To align the buttons
	"""

	#region -----------------------------------------------------> Class setup
	#endregion --------------------------------------------------> Class setup	

	#region --------------------------------------------------> Instance setup
	def __init__(self, parent):
		""""""
		#region -----------------------------------------------> Initial setup
		self.parent = parent
		#endregion --------------------------------------------> Initial setup

		#region -----------------------------------------------------> Widgets
		self.btnClear = dtsWidget.ButtonClearAll(
			parent    = parent,
			label     = config.label['ButtonGroup']['Clear'],
		)
		self.btnRun = wx.Button(
			parent = parent,
			label  = config.label['ButtonGroup']['Run'],
		)
		#endregion --------------------------------------------------> Widgets

		#region ------------------------------------------------------> Sizers
		self.Sizer = wx.FlexGridSizer(1, 3, 1, 1)
		self.Sizer.Add(
			self.btnClear,
			border = 10,
			flag   = wx.EXPAND|wx.ALL
		)
		self.Sizer.Add(
			self.btnRun,
			border = 10,
			flag   = wx.EXPAND|wx.ALL
		)
		#endregion ---------------------------------------------------> Sizers
	#endregion -----------------------------------------------> Instance setup
#---
#endregion ---------------------------------------------------------> Classes