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
import wx.lib.agw.aui as aui

import dat4s_core.widget.wx_widget as dtsWidget
import dat4s_core.validator.validator as dtsValidator

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
			ext       = config.extLong['Data'],
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
			self.fastaFile.tc.SetValue("/Users/bravo/Dropbox/SOFTWARE-DEVELOPMENT/APPS/PEPTIDE_SEARCH_TOOLS/LOCAL/DATA/NEW-DATA/HUMAN_ref_Jan2019-cut-long.fasta")
			self.geneFile.tc.SetValue("/Users/bravo/Dropbox/SOFTWARE-DEVELOPMENT/APPS/PEPTIDE_SEARCH_TOOLS/LOCAL/DATA/NEW-DATA/XIAP_GeneNAMES.txt")
			self.outFile.tc.SetValue("/Users/bravo/TEMP-GUI/BORRAR-PeptideSearchTools/gene-out.txt")
			self.residueExtract.tc.SetValue("5 10 20 50")
		else:
			self.colExtract.tc.SetValue("NA")
		#endregion -------------------------> Test & Default production values
	#---
	#endregion -----------------------------------------------> Instance setup
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