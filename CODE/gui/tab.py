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
import _thread

import wx

import dat4s_core.widget.wx_widget as dtsWidget
import dat4s_core.validator.validator as dtsValidator

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
	 	#region -------------------------------------------------> Restart GUI
		self.btnGroup.btnRun.Enable()
		self.btnGroup.btnRun.SetLabel(config.label['ButtonGroup']['Run'])
		#endregion ----------------------------------------------> Restart GUI

		#region -------------------------------------------> Restart variables
		self.runEnd = False
		#endregion ----------------------------------------> Restart variables
		return True
	#---
	#endregion ------------------------------------------------> Class methods

#---
#endregion ----------------------------------------------------> Base Classess

#region ------------------------------------------------------------> Classess
class Peptide(wx.Panel, BaseTab):
	"""Tab to perform the peptide search analysis 
		
		Parameters
		----------
		parent: wx widget
			Parent of the widgets
		name : str
			Name of the Tab

		Attributes
		----------
		dataFile : dtsWidget.ButtonTextCtrlFF
			wx.Button & wx.TextCtrl for Data file
		outFile : dtsWidget.ButtonTextCtrlFF
			wx.Button & wx.TextCtrl for the Output file
		firstRes : dtsWidget.StaticTextCtrl
			wx.StaticText & wx.TextCtrl for the First Residue
		startRes : dtsWidget.StaticTextCtrl
			wx.StaticText & wx.TextCtrl for the Start Residue
		colExtract : dtsWidget.StaticTextCtrl
			wx.StaticText & wx.TextCtrl for the Columns to Extract
		Sizer : wx.GridBagSizer
			Main sizer of the tab
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
		#--> wx.Button & wx.TextCtrl
		self.dataFile = dtsWidget.ButtonTextCtrlFF(
			self.sbFile,
			btnLabel  = config.label['Peptide']['DataFile'],
			tcHint    = config.hint['Peptide']['DataFile'],
			ext       = config.extLong['Data'],
			validator = dtsValidator.IsNotEmpty(
				self,
				config.msg['Error']['Peptide']['DataFile'],
			),
		)
		self.outFile = dtsWidget.ButtonTextCtrlFF(
			self.sbFile,
			btnLabel  = config.label['Peptide']['OutFile'],
			tcHint    = config.hint['Peptide']['OutFile'],
			ext       = config.extLong['Data'],
			mode      = 'save',
			validator = dtsValidator.IsNotEmpty(
				self,
				config.msg['Error']['Peptide']['OutFile'],
			),
		)
		#--> wx.StaticText & wx.TextCtrl
		self.firstRes = dtsWidget.StaticTextCtrl(
			self.sbValue,
			stLabel  = config.label['Peptide']['FirstResidue'],
			tcHint   = config.hint['Peptide']['FirstResidue'],
			validator = dtsValidator.Number(
				self,
				config.msg['Error']['Peptide']['FirstResidue'],
				ref  = 1,
			),
		)
		self.startRes = dtsWidget.StaticTextCtrl(
			self.sbColumn,
			stLabel = config.label['Peptide']['StartResidue'],
			tcHint   = config.hint['Peptide']['StartResidue'],
			validator = dtsValidator.Number(
				self,
				config.msg['Error']['Peptide']['StartResidue'],
			),
		)
		self.colExtract = dtsWidget.StaticTextCtrl(
			self.sbColumn,
			stLabel = config.label['Peptide']['ColExtract'],
			tcHint   = config.hint['Peptide']['ColExtract'],
			validator = None,
		)
		#endregion --------------------------------------------------> Widgets

		#region ------------------------------------------------------> Sizers
		#--> wx.StaticBox File
		self.sizersbFileWid.Add(
			self.dataFile.btn,
			border = 5,
			flag   = wx.ALIGN_CENTER_VERTICAL|wx.EXPAND|wx.ALL,
		)
		self.sizersbFileWid.Add(
			self.dataFile.tc,
			border = 5,
			flag   = wx.EXPAND|wx.ALL,
		)
		self.sizersbFileWid.Add(
			self.outFile.btn,
			border = 5,
			flag   = wx.ALIGN_CENTER_VERTICAL|wx.EXPAND|wx.ALL,
		)
		self.sizersbFileWid.Add(
			self.outFile.tc,
			border = 5,
			flag   = wx.EXPAND|wx.ALL,
		)	
		#--> wx.StaticBox Value
		self.sizersbValueWid.Add(
			self.firstRes.st,
			border = 5,
			flag   = wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL,
		)
		self.sizersbValueWid.Add(
			self.firstRes.tc,
			border = 5,
			flag   = wx.EXPAND|wx.ALL,
		)
		#--> wx.StaticBox Value
		self.sizersbColumnWid.Add(
			self.startRes.st,
			border = 5,
			flag   = wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL,
		)
		self.sizersbColumnWid.Add(
			self.startRes.tc,
			border = 5,
			flag   = wx.EXPAND|wx.ALL,
		)
		self.sizersbColumnWid.Add(
			self.colExtract.st,
			border = 5,
			flag   = wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL,
		)
		self.sizersbColumnWid.Add(
			self.colExtract.tc,
			border = 5,
			flag   = wx.EXPAND|wx.ALL,
		)		
		#--> Main Sizer
		self.Sizer = wx.GridBagSizer(1, 1)
		self.Sizer.Add(
			self.sizersbFile,
			pos    = (0,0),
			flag   = wx.EXPAND|wx.ALL,
			border = 5
		)
		self.Sizer.Add(
			self.sizersbValue,
			pos    = (1,0),
			flag   = wx.EXPAND|wx.ALL,
			border = 5
		)
		self.Sizer.Add(
			self.sizersbColumn, 
			pos    = (2,0),
			flag   = wx.EXPAND|wx.ALL,
			border = 5
		)
		self.Sizer.Add(
			self.btnGroup.Sizer,
			pos    = (3,0),
			flag   = wx.ALIGN_CENTER|wx.ALL,
			border = 5
		)
		self.Sizer.AddGrowableCol(0, 1)
		self.SetSizer(self.Sizer)
		self.Sizer.Fit(self)
		#endregion ---------------------------------------------------> Sizers

		#region ----------------------------> Test & Default production values
		if config.development:
			self.dataFile.tc.SetValue("/Users/bravo/Dropbox/SOFTWARE-DEVELOPMENT/APPS/PEPTIDE_SEARCH_TOOLS/LOCAL/DATA/NEW-DATA/peptides.txt")
			self.outFile.tc.SetValue("/Users/bravo/TEMP-GUI/BORRAR-PeptideSearchTools/peptide-out.txt")
			self.firstRes.tc.SetValue("2")
			self.startRes.tc.SetValue("36")
			self.colExtract.tc.SetValue("0 38 36 37")
		else:
			self.colExtract.tc.SetValue("NA")
		#endregion -------------------------> Test & Default production values
	#---
	#endregion -----------------------------------------------> Instance setup

	#region ---------------------------------------------------> Class methods

	#endregion ------------------------------------------------> Class methods
#---
#endregion ---------------------------------------------------------> Classess