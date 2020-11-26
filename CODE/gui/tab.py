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
from operator import itemgetter

import wx
import wx.lib.agw.aui as aui

import dat4s_core.data.filefolder as dtsFF
import dat4s_core.data.string as dtsStr
import dat4s_core.validator.validator as dtsValidator
import dat4s_core.widget.wx_widget as dtsWidget
import dat4s_core.widget.wx_window as dtsWindow

import config.config as config
import gui.pane as pstPane
import gui.widget as pstWidget
#endregion ----------------------------------------------------------- Imports



#region -------------------------------------------------------------> Classes
class GeneTab(wx.Panel, pstWidget.UserInput):
	"""Tab for the gene search
	
		Parameters
		----------
		parent : wx widget or None
			Parent of the tab
		name : str
			To identify the tab
		statusbar : wx.StatusBar
			Statusbar of the main window to show msgs

		Attributes
		----------
		parent : wx widget or None
			Parent of the tab

	"""
	#region --------------------------------------------------> Instance setup
	def __init__(self, parent, name, statusbar):
		""""""
		#region -----------------------------------------------> Initial setup
		self.parent = parent

		wx.Panel.__init__(self, parent, name=name)
		pstWidget.UserInput.__init__(self, self)
		#endregion --------------------------------------------> Initial setup

		#region -----------------------------------------------------> Widgets
		#--> Statusbar
		self.statusbar = statusbar
		#--> wx.Button & wx.TextCtrl
		self.fastaFile = dtsWidget.ButtonTextCtrlFF(
			self.sbFile,
			btnLabel  = config.label['Gene']['FastaFile'],
			tcHint    = config.hint['Gene']['FastaFile'],
			ext       = config.extLong['Seq'],
			validator = dtsValidator.IsNotEmpty(
				parent,
				config.msg['Error']['Gene']['FastaFile'],
			),
		)
		self.geneFile = dtsWidget.ButtonTextCtrlFF(
			self.sbFile,
			btnLabel  = config.label['Gene']['GeneFile'],
			tcHint    = config.hint['Gene']['GeneFile'],
			ext       = config.extLong['Data'],
			validator = dtsValidator.IsNotEmpty(
				parent,
				config.msg['Error']['Gene']['GeneFile'],
			),
		)		
		self.outFile = dtsWidget.ButtonTextCtrlFF(
			self.sbFile,
			btnLabel  = config.label['Gene']['OutFile'],
			tcHint    = config.hint['Gene']['OutFile'],
			ext       = config.extLong['Data'],
			mode      = 'save',
			validator = dtsValidator.IsNotEmpty(
				parent,
				config.msg['Error']['Gene']['OutFile'],
			),
		)
		#--> wx.StaticText & wx.TextCtrl
		self.residueExtract = dtsWidget.StaticTextCtrl(
			self.sbValue,
			stLabel   = config.label['Gene']['ResidueExtract'],
			tcHint    = config.hint['Gene']['ResidueExtract'],
			validator = dtsValidator.NumberList(
				parent,
				config.msg['Error']['Gene']['ResidueExtract'],
				refMin = 1,
			),
		)
		#endregion --------------------------------------------------> Widgets

		#region ------------------------------------------------------> Sizers
		#--> wx.StaticBox File
		self.sizersbFileWid.Add(
			self.fastaFile.btn,
			border = 5,
			flag   = wx.ALIGN_CENTER_VERTICAL|wx.EXPAND|wx.ALL,
		)
		self.sizersbFileWid.Add(
			self.fastaFile.tc,
			border = 5,
			flag   = wx.EXPAND|wx.ALL,
		)
		self.sizersbFileWid.Add(
			self.geneFile.btn,
			border = 5,
			flag   = wx.ALIGN_CENTER_VERTICAL|wx.EXPAND|wx.ALL,
		)
		self.sizersbFileWid.Add(
			self.geneFile.tc,
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
			self.residueExtract.st,
			border = 5,
			flag   = wx.ALIGN_CENTER_VERTICAL|wx.EXPAND|wx.ALL,
		)
		self.sizersbValueWid.Add(
			self.residueExtract.tc,
			border = 5,
			flag   = wx.EXPAND|wx.ALL,
		)
		#--> wx.StaticBox Column
		self.sizersbColumn.ShowItems(False)
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
			self.btnGroup.Sizer,
			pos    = (2,0),
			flag   = wx.ALIGN_CENTER|wx.ALL,
			border = 5
		)
		self.Sizer.AddGrowableCol(0, 1)
		self.SetSizer(self.Sizer)
		self.Sizer.Fit(self)
		#endregion ---------------------------------------------------> Sizers

		#region ----------------------------> Test & Default production values
		if config.development:
			self.fastaFile.tc.SetValue("/Users/bravo/Dropbox/SOFTWARE-DEVELOPMENT/APPS/PEPTIDE_SEARCH_TOOLS/LOCAL/DATA/NEW-DATA/HUMAN_ref_Jan2019.fasta")
			self.geneFile.tc.SetValue("/Users/bravo/Dropbox/SOFTWARE-DEVELOPMENT/APPS/PEPTIDE_SEARCH_TOOLS/LOCAL/DATA/NEW-DATA/XIAP_GeneNAMES.txt")
			self.outFile.tc.SetValue("/Users/bravo/TEMP-GUI/BORRAR-PeptideSearchTools/gene-out.txt")
			self.residueExtract.tc.SetValue("5 10 20 50")
		else:
			self.colExtract.tc.SetValue("NA")
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
		msg = f"{msgM}: {config.label['Gene']['FastaFile']}"
		wx.CallAfter(dtsWidget.StatusBarUpdate, self.statusbar, msg)
		if self.fastaFile.tc.GetValidator().Validate(self):
			pass
		else:
			return False

		msg = f"{msgM}: {config.label['Gene']['GeneFile']}"
		wx.CallAfter(dtsWidget.StatusBarUpdate, self.statusbar, msg)
		if self.geneFile.tc.GetValidator().Validate(self):
			pass
		else:
			return False

		msg = f"{msgM}: {config.label['Gene']['OutFile']}"
		wx.CallAfter(dtsWidget.StatusBarUpdate, self.statusbar, msg)
		if self.outFile.tc.GetValidator().Validate(self):
			pass
		else:
			return False

		msg = f"{msgM}: {config.label['Gene']['ResidueExtract']}"
		wx.CallAfter(dtsWidget.StatusBarUpdate, self.statusbar, msg)
		if self.residueExtract.tc.GetValidator().Validate(self):
			pass
		else:
			return False
		#endregion ----------------------------------------> Individual Fields

		#region ------------------------------------------------> File content
		#--> Gene names
		self.gFile    = self.geneFile.tc.GetValue()
		self.geneList = []
		with open(self.gFile, 'r') as gFile:
			for line in gFile:
				g = "".join(line.split())
				g = g.replace('"', "")
				if g == '':
					continue
				else:
					pass
				self.geneList.append(g)
				if ";" in g:
					[self.geneList.append(x) for x in g.split(";")]
				else:
					pass
		if not self.geneList:
			msg = config.error['Gene']['NoGene']
			dtsWindow.MessageDialog('errorF', msg, parent=self.parent)
			return False
		else:
			pass
		#---
		#endregion ---------------------------------------------> File content

		return True
	#---

	def PrepareRun(self):
		"""Prepare the run """
		#region ---------------------------------------------------------> Msg
		msg = config.msg['Step']['Prepare']
		wx.CallAfter(dtsWidget.StatusBarUpdate, self.statusbar, msg)
		#endregion ------------------------------------------------------> Msg

		#region -----------------------------------------------------> Prepare
		# Gene associated variables set in CheckInput since it is necesary to 
		# Check Gene file content
		#--> Input values
		self.fFile  = self.fastaFile.tc.GetValue()
		self.oFile  = self.outFile.tc.GetValue()
		self.resExt = list(
			map(
				int, 
				self.residueExtract.tc.GetValue().split()
			)
		)
		resExtStr = " ".join(self.residueExtract.tc.GetValue().split())
		#---
		#--> Needed for the analysis
		self.ltotal    = 0
		self.lempty    = 0
		self.prottotal = 0
		self.protsselT = 0
		self.searchP   = False
		self.dataO     = []
		#---
		#--> For output
		self.d = {
			config.label['Gene']['FastaFile']     : self.fFile,
			config.label['Gene']['GeneFile']      : self.gFile,
			config.label['Gene']['OutFile']       : self.oFile,
			config.label['Gene']['ResidueExtract']: resExtStr,
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
		with open(self.fFile, 'r') as File:
			for line in File:
				self.ltotal += 1
				#--> Remove new line characters and strip line
				l = dtsStr.Str2List(line, strip='b')[0]
				#--> Discard empty lines
				if l == '':
					self.lempty += 1
				#--> Process line containing a fasta header
				elif l[0] == '>':
					self.prottotal += 1
					#--> Finish processing of previous sequence
					if self.searchP:
						lseq = ''.join(lseq)
						for i in self.resExt:
							ltemp.append(lseq[0:i])
						self.dataO.append(ltemp)
					else:
						pass
					#--> Setup analysis of a new protein
					if 'GN=' in l:
						tGene = [s for s in l.split() if 'GN=' in s][0].split('=')[1]
						if tGene in self.geneList:
							self.searchP = True
							self.protsselT += 1
							ltemp = []
							lseq = []
							ltemp.append(tGene)
							ltemp.append(l.split('|')[1])
						else:
							self.searchP = False
					else:
						self.searchP = False
				#--> Process line containing a sequence line
				else:
					if self.searchP:
						lseq.append(l)
					else:
						pass
				#--> Update statusbar
				if not self.ltotal % 100:
					msg = (
						f"Analysing --> Total lines: {self.ltotal}, "
						f"Empty lines: {self.lempty}, "
						f"Total Proteins: {self.prottotal}, "
						f"Matched Proteins:  {self.protsselT}"
					)
					wx.CallAfter(dtsWidget.StatusBarUpdate, self.statusbar, msg)
				else:
					pass
		#--> Last pass to catch the last protein
		if self.searchP:
			lseq = ''.join(lseq)
			for i in self.resExt:
				ltemp.append(lseq[0:i])
			self.dataO.append(ltemp)
		else:
			pass
		#---
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
		if self.protsselT == 0:
			msg = config.msg['Error']['Gene']['NoProtFound']
			dtsWindow.MessageDialog('errorF', msg, self)
			return False
		else:
			pass
		#endregion ------------------------> Check there is something to write	

		# #region -------------------------------------------------------> Write
		#--> Write input data
		oFile = open(self.oFile, 'w')
		oFile.write('Input data:\n')
		dtsFF.WriteDict2File(oFile, self.d)
		oFile.write('\n')
		#---
		#--> Write output
		oFile.write('Output data:\n')
		header = 'Gene\tProtein\t' + "\t".join(['1-'+str(x) for x in self.resExt])
		oFile.write(header+'\n')

		self.dataO.sort(key=itemgetter(0, 1))
		dtsFF.WriteList2File(oFile, self.dataO)
		oFile.write('\n')
		#---
		#--> File last line
		dtsFF.WriteLastLine2File(oFile, config.title['MainW'])
		#---
	 	#--> Close file and final summary in statusbar
		oFile.close()
		msg = (
			f"Final count --> Total lines: {self.ltotal}, "
			f"Empty lines: {self.lempty}, "
			f"Total Proteins: {self.prottotal}, "
			f"Matched Proteins:  {self.protsselT}"
		)
		wx.CallAfter(dtsWidget.StatusBarUpdate, self.statusbar, msg)
		#---
		# #endregion ----------------------------------------------------> Write

		return True
	#---

	def RunEnd(self):
		""""""
		if self.RunEnd:
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

class PeptideTab(wx.Panel):
	"""Tab for the peptide search 
	
		Parameters
		----------
		parent : wx widget or None
			Parent of the tab
		name : str
			To identify the tab
		statusbar : wx.StatusBar
			Statusbar of the main window to show msgs

		Attributes
		----------
		lc : dtsWidget.ListZebra
			This is a wx.ListCtrl to display the column's name in the Data File
		userInput : pstPane.PeptidePane
			User input section of the Tab
		_mgr : aui.AuiManager()
			aui manager for the tab
	"""
	#region --------------------------------------------------> Instance setup
	def __init__(self, parent, name, statusbar):
		""""""
		#region -----------------------------------------------> Initial setup
		super().__init__(parent, name=name)
		#endregion --------------------------------------------> Initial setup
		
		#region -----------------------------------------------------> Widgets
		self.lc = dtsWidget.ListZebra(
			self, 
			colLabel = config.label['Peptide']['Column'],
			colSize = config.size['ListCtrl']['Peptide'],
		)
		self.userInput = pstPane.PeptidePane(self, statusbar, lc=self.lc)
		#endregion --------------------------------------------------> Widgets

		#region -------------------------------------------------> AUI Control
		self._mgr = aui.AuiManager()
		self._mgr.SetManagedWindow(self)
		#--> Add standard panels
		self._mgr.AddPane(
			self.userInput,
			aui.AuiPaneInfo(
				).CenterPane(
				).Caption(
					config.title['UserInput']
				).CaptionVisible(
				).Floatable(
					b=False
				).CloseButton(
					visible=False
				).Movable(
					b=False
				).PaneBorder(
					visible=False,
			),
		)
		self._mgr.AddPane(
			self.lc,
			aui.AuiPaneInfo(
				).Right(
				).Caption(
					config.title['ListCtrl']
				).Floatable(
					b=False
				).CloseButton(
					visible=False
				).Movable(
					b=False
				).PaneBorder(
					visible=False,
			),
		)
		#---
		self._mgr.Update()
		#endregion ----------------------------------------------> AUI Control
	#---
	#endregion -----------------------------------------------> Instance setup
#---
#endregion ----------------------------------------------------------> Classes