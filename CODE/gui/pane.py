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

"""Classes and methods to create Pane elements to be used with the 
	wx.lib.agw.aui library.
"""

#region -------------------------------------------------------------> Imports
import wx

import dat4s_core.data.filefolder as dtsFF
import dat4s_core.data.string as dtsStr
import dat4s_core.widget.wx_widget as dtsWidget
import dat4s_core.widget.wx_window as dtsWindow
import dat4s_core.validator.validator as dtsValidator

import config.config as config
import gui.widget as pstWidget
#endregion ----------------------------------------------------------> Imports

#region -------------------------------------------------------------> Classes
class PeptidePane(wx.Panel, pstWidget.UserInput):
	"""Pane for user input in the Peptide tab
		
		Parameters
		----------
		parent: wx widget
			Parent of the widgets
		name : str
			To id the pane and its elements
		statusbar : wx.StatusBar
			Main status bar in the app to display msgs

		Attributes
		----------
		parent : wx widget
			Parent of the pane
		name : str
			To id the pane and its elements
		statusbar : wx.StatusBar
			Main status bar in the app to display msgs
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
	def __init__(self, parent, name, statusbar, lc=None):
		""""""
		#region -----------------------------------------------> Initial setup
		self.parent = parent
		self.name   = name

		wx.Panel.__init__(self, parent)
		pstWidget.UserInput.__init__(self, self)
		#endregion --------------------------------------------> Initial setup

		#region -----------------------------------------------------> Widgets
		#--> Statusbar
		self.statusbar = statusbar
		#--> wx.Button & wx.TextCtrl
		self.dataFile = dtsWidget.ButtonTextCtrlFF(
			self.sbFile,
			btnLabel  = config.label[name]['DataFile'],
			tcHint    = config.hint[name]['DataFile'],
			ext       = config.extLong['Data'],
			listCtrl  = lc,
			validator = dtsValidator.IsNotEmpty(
				parent,
				config.msg['Error'][name]['DataFile'],
			),
		)
		self.outFile = dtsWidget.ButtonTextCtrlFF(
			self.sbFile,
			btnLabel  = config.label[name]['OutFile'],
			tcHint    = config.hint[name]['OutFile'],
			ext       = config.extLong['Data'],
			mode      = 'save',
			validator = dtsValidator.IsNotEmpty(
				parent,
				config.msg['Error'][name]['OutFile'],
			),
		)
		#--> wx.StaticText & wx.TextCtrl
		self.firstRes = dtsWidget.StaticTextCtrl(
			self.sbValue,
			stLabel   = config.label[name]['FirstResidue'],
			tcHint    = config.hint[name]['FirstResidue'],
			validator = dtsValidator.NumberList(
				parent,
				config.msg['Error'][name]['FirstResidue'],
				refMin = 1,
			),
		)
		self.startRes = dtsWidget.StaticTextCtrl(
			self.sbColumn,
			stLabel   = config.label[name]['StartResidue'],
			tcHint    = config.hint[name]['StartResidue'],
			validator = dtsValidator.NumberList(
				parent,
				config.msg['Error'][name]['StartResidue'],
				refMin = 0
			),
		)
		self.colExtract = dtsWidget.StaticTextCtrl(
			self.sbColumn,
			stLabel   = config.label[name]['ColExtract'],
			tcHint    = config.hint[name]['ColExtract'],
			validator = dtsValidator.NumberList(
				parent,
				config.msg['Error'][name]['ColExtract'],
				isList = True,
				refMin = 0,
			),
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
			pass
		#endregion -------------------------> Test & Default production values
	#---
	#endregion -----------------------------------------------> Instance setup

	#region ---------------------------------------------------> Class methods
	def CheckInput(self):
		"""Chek user input. Overrides BaseTab.CheckInput"""
		#region ---------------------------------------------------------> Msg
		msgM = config.msg['Step']['Check']
		#endregion ------------------------------------------------------> Msg
		
		#region -------------------------------------------> Individual Fields
		msg = f"{msgM}: {config.label[self.name]['DataFile']}"
		wx.CallAfter(dtsWidget.StatusBarUpdate, self.statusbar, msg)
		if self.dataFile.tc.GetValidator().Validate(self):
			pass
		else:
			return False

		msg = f"{msgM}: {config.label[self.name]['OutFile']}"
		wx.CallAfter(dtsWidget.StatusBarUpdate, self.statusbar, msg)
		if self.outFile.tc.GetValidator().Validate(self):
			pass
		else:
			return False

		msg = f"{msgM}: {config.label[self.name]['FirstResidue']}"
		wx.CallAfter(dtsWidget.StatusBarUpdate, self.statusbar, msg)
		if self.firstRes.tc.GetValidator().Validate(self):
			pass
		else:
			return False
		
		msg = f"{msgM}: {config.label[self.name]['StartResidue']}"
		wx.CallAfter(dtsWidget.StatusBarUpdate, self.statusbar, msg)
		if self.startRes.tc.GetValidator().Validate(
			self, 
			refMax=self.dataFile.Ncol
		):
			pass
		else:
			return False

		msg = f"{msgM}: {config.label[self.name]['ColExtract']}"
		wx.CallAfter(dtsWidget.StatusBarUpdate, self.statusbar, msg)
		if self.colExtract.tc.GetValidator().Validate(
			self, 
			refMax=self.dataFile.Ncol
		):
			pass
		else:
			return False
		#endregion ------------------------------------------> Indivual Fields

		return True
	#---

	def PrepareRun(self):
		"""Prepare the run """
		#region ---------------------------------------------------------> Msg
		msg = config.msg['Step']['Prepare']
		wx.CallAfter(dtsWidget.StatusBarUpdate, self.statusbar, msg)
		#endregion ------------------------------------------------------> Msg

		#region -----------------------------------------------------> Prepare
		#--> Input values
		self.iFile  = self.dataFile.tc.GetValue()
		self.oFile  = self.outFile.tc.GetValue()
		self.fRes   = int(" ".join(self.firstRes.tc.GetValue().split()))
		self.sRes   = int(" ".join(self.startRes.tc.GetValue().split()))
		self.colExt = list(
			map(
				int, 
				self.colExtract.tc.GetValue().split()
			)
		)
		colExtStr = " ".join(self.colExtract.tc.GetValue().split())
		#---
		#--> Needed for the analysis
		self.lempty   = 0
		self.ltotal   = 0
		self.ptotal   = 0
		self.dataO    = []
		#---
		#--> For output
		self.d = {
			config.label[self.name]['DataFile']    : self.iFile,
			config.label[self.name]['OutFile']     : self.oFile,
			config.label[self.name]['FirstResidue']: self.fRes,
			config.label[self.name]['StartResidue']: self.sRes,
			config.label[self.name]['ColExtract']  : colExtStr,
		}
		#---
		#endregion --------------------------------------------------> Prepare
		
		return True
	#---

	def RunAnalysis(self):
		"""Run the analysis"""
		#region ---------------------------------------------------------> Msg
		msg = config.msg['Step']['Run']
		wx.CallAfter(dtsWidget.StatusBarUpdate, self.statusbar, msg)
		#endregion ------------------------------------------------------> Msg

		#region -----------------------------------------------------> Process
		with open(self.iFile, 'r') as iFile:
			for line in iFile:
				self.ltotal += 1
				l = dtsStr.Str2List(line, sep='\t')
				if self.ltotal == 1:
				 #--- Set the header for the output file
					self.header = []
					for i in self.colExt:
						self.header.append(l[i])
					self.header = '\t'.join(self.header)
				else:
					pass
				if l[0] == '':
					self.lempty += 1
				else:
					try:
						tres = int(l[self.sRes])
						go = True
					except Exception:
						self.lempty += 1
						go = False
					if go:
						if tres <= self.fRes:
							ltemp = []
							for i in self.colExt:
								ltemp.append(l[i])
							self.dataO.append(ltemp)
							self.ptotal += 1
						else:
							pass
					else:
						pass
				if not self.ltotal % 100:
					msg = (
						f"Analysing --> Total Lines: {self.ltotal}, " 
						f"Empty Lines: {self.lempty}, "
						f"Peptides: {self.ptotal}"
					)
					wx.CallAfter(dtsWidget.StatusBarUpdate, self.statusbar, msg)
				else:
					pass
		#endregion --------------------------------------------------> Process

		return True
	#---

	def WriteOutput(self):
		""" Write the output """
		#region ---------------------------------------------------------> Msg
		msg = config.msg['Step']['Output']
		wx.CallAfter(dtsWidget.StatusBarUpdate, self.statusbar, msg)
		#endregion ------------------------------------------------------> Msg

		#region ---------------------------> Check there is something to write	
		if self.ptotal == 0:
			msg = config.msg['Error'][self.name]['NoPeptide']
			dtsWindow.MessageDialog('errorF', msg, self)
			return False
		else:
			pass
		#endregion ------------------------> Check there is something to write	

		#region -------------------------------------------------------> Write
		#--> Write input data
		oFile = open(self.oFile, 'w')
		oFile.write('Input data:\n')
		dtsFF.WriteDict2File(oFile, self.d)
		oFile.write('\n')
		#---
		#--> Write output
		oFile.write('Output data:\n')
		oFile.write(str(self.header) + '\n')
		dtsFF.WriteList2File(oFile, self.dataO)
		oFile.write('\n')
		#---
		#--> File last line
		dtsFF.WriteLastLine2File(oFile, config.title['MainW'])
		#---
	 	#--> Close file and final summary in statusbar
		oFile.close()

		msg = (
			f"Final count --> Total Lines: {self.ltotal}, " 
			f"Empty Lines: {self.lempty}, "
			f"Peptides: {self.ptotal}"
		)
		wx.CallAfter(dtsWidget.StatusBarUpdate, self.statusbar, msg)
		#---
		#endregion ----------------------------------------------------> Write

		return True
	#---

	def RunEnd(self):
		""""""
		if self.runEnd:
			#--> Remove value of Output File to avoid overwriting it
			self.outFile.tc.SetValue("")
		else:
			pass
		#--> Standard ending 
		super().RunEnd()
		#---
	#---
	#endregion ------------------------------------------------> Class methods
#---
#endregion ----------------------------------------------------------> Classes