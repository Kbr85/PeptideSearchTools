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

"""Main windows and dialogs of the App
"""

#region -------------------------------------------------------------- Imports
import ast

import wx
import wx.lib.agw.aui as aui

import dat4s_core.validator.validator as dtsValidator
import dat4s_core.widget.wx_widget as dtsWidget
import dat4s_core.widget.wx_window as dtsWindow

import config.config as config
import menu.menu as menu
import gui.tab as pstTab
#endregion ----------------------------------------------------------- Imports

#region -------------------------------------------------------------> Classes
class MainWindow(wx.Frame):
	"""Creates the main window of the App 
	
		Parameters
		----------
		parent : wx widget or None
		
		Attributes
		----------
		name : str
			Name to id the window
		tabMethods: dict
			Methods to create the tabs
		menubar : wx.MenuBar
			wx.Menubar associated with the window
		statusbar : wx.StatusBar
			wx.StatusBar associated with the window
		notebook : wx.lib.agw.aui.auibook.AuiNotebook
			Notebook associated with the window
		Sizer : wx.BoxSizer
			Sizer for the window
	"""
	#region --------------------------------------------------> Instance setup
	def __init__(self, parent=None):
		""""""
		#region -----------------------------------------------> Initial setup
		self.name = config.name['Window']['MainW']

		self.tabMethods = {
			'Peptide'  : pstTab.PeptideTab,
			'Gene'     : pstTab.GeneTab,
			'Consensus': pstTab.ConsensusTab,
			'LicAgr'   : dtsWindow.TxtContentWin,
			'Help'     : dtsWindow.TxtContentWin,
		}

		super().__init__(
			parent = parent,
			size   = config.size[self.name],
			title  = config.title['MainW'],
		)
		#endregion --------------------------------------------> Initial setup

		#region ---------------------------------------------> Default MenuBar
		self.menubar = menu.MainMenuBar()
		self.SetMenuBar(self.menubar) 
		#endregion ------------------------------------------> Default MenuBar

		#region -----------------------------------------------------> Widgets
		self.statusbar = self.CreateStatusBar()

		self.notebook = aui.auibook.AuiNotebook(
			self,
			agwStyle=aui.AUI_NB_TOP|aui.AUI_NB_CLOSE_ON_ALL_TABS|aui.AUI_NB_TAB_MOVE,
		)
		#endregion --------------------------------------------------> Widgets

		#region ------------------------------------------------------> Sizers
		self.Sizer = wx.BoxSizer(wx.HORIZONTAL)
		self.Sizer.Add(self.notebook, 1, wx.EXPAND|wx.ALL, 5)
		self.SetSizer(self.Sizer)
		#endregion ---------------------------------------------------> Sizers

		#region ---------------------------------------------> Position & Show
		self.Center()
		self.Show()
		#endregion ------------------------------------------> Position & Show
	#---
	#endregion -----------------------------------------------> Instance setup

	#region ----------------------------------------------------> Menu methods
	def CreateTab(self, name):
		"""Create a tab
		
			Parameters
			----------
			name : str
				One of the values in config.name for tabs
		"""
		#region -----------------------------------------------------> Get tab
		win = self.FindWindowByName(name)
		#endregion --------------------------------------------------> Get tab
		if win is None:
		 #--> Create tab
			if name in ('LicAgr', 'Help'):
				self.notebook.AddPage(
					dtsWindow.TxtContentWin(
						self.notebook,
						config.file[name],
						name,
					),
					config.title[name],
				)
				self.notebook.SetSelection(
					self.notebook.GetPageIndex(
						self.FindWindowByName(
							name
						)
					)
				)
			else:
				self.notebook.AddPage(
					self.tabMethods[name](
						self.notebook,
						name,
						self.statusbar,
					),
					config.title[name],
				)
				self.notebook.SetSelection(
					self.notebook.GetPageIndex(
						self.FindWindowByName(
							name
						)
					)
				)
		else:
		 #--> Focus
			self.notebook.SetSelection(self.notebook.GetPageIndex(win))
	#---
	#endregion -------------------------------------------------> Menu methods
#---

class ConsensusConf(wx.Dialog):
	"""Window to configure the consensus search 
	
		Parameters
		----------
		parent : wx widget
			Parent of the window
		name : str
			To id the window and its elements
		title : str
			Title of the window

		Attributes
		----------
		parent : wx widget
			Parent of the window 
		name : str
			To id the window and its elements
		tcPosList : list or None
			To know if widgets have been created
		nRes : dts.Widget.StaticTextCtrlButton
			Create field widgets
		swMatrix : wx.ScrolledWindow
			Region to contain the fields
		btnSizer : wx.Sizer
			Sizer with the Cancel/Ok buttons
		swSizer : wx.FlexGridSizer
			Sizer for the fields
		Sizer : wx.FlexGridSizer
			Main sizer of the window
	"""
	#region --------------------------------------------------> Instance setup
	def __init__(self, parent, name, title=None):
		""""""
		#region -----------------------------------------------> Initial setup
		self.parent    = parent
		self.name      = name
		self.tcPosList = None

		tTitle = config.title['ConsConf'] if title is None else title
		style  = wx.CAPTION|wx.CLOSE_BOX|wx.RESIZE_BORDER
		super().__init__(parent, title=tTitle, style=style)
		#region -----------------------------------------------> Initial setup

		#region -----------------------------------------------------> Widgets
		self.nRes = dtsWidget.StaticTextCtrlButton(
			self,
			setSizer  = True,
			stLabel   = config.label[name]['Number'],
			btnLabel  = config.label[name]['Create'],
			validator = dtsValidator.NumberList(
				self,
				config.msg['Error'][name]['Number'],
				refMin = 1,
			),
		)
		self.swMatrix = wx.ScrolledWindow(
			self, 
			size = config.size['ScrolledW'][name],
		)
		self.swMatrix.SetBackgroundColour('WHITE')
		#endregion --------------------------------------------------> Widgets
		
		#region ------------------------------------------------------> Sizers
		#--> Button Sizers
		self.btnSizer = self.CreateStdDialogButtonSizer(
			wx.OK|wx.CANCEL
		)
		#--> Field sizer
		self.swSizer = wx.FlexGridSizer(1,3,1,1)
		self.swMatrix.SetSizer(self.swSizer)
		self.swSizer.AddGrowableCol(2, 1)
		#--> Main sizer
		self.Sizer = wx.FlexGridSizer(3, 1, 1, 1)
		self.Sizer.Add(
			self.nRes.Sizer,
			border = 5,
			flag   = wx.ALIGN_CENTER|wx.ALL,
		)
		self.Sizer.Add(
			self.swMatrix,
			border = 5,
			flag   = wx.EXPAND|wx.ALL,
		)
		self.Sizer.Add(
			self.btnSizer,
			border = 5,
			flag   = wx.ALIGN_RIGHT|wx.ALIGN_BOTTOM|wx.ALL
		)
		#-->
		self.Sizer.AddGrowableCol(0, 1)
		self.Sizer.AddGrowableRow(1, 1)
		self.SetSizer(self.Sizer)
		self.Sizer.Fit(self)
		#endregion ---------------------------------------------------> Sizers

		#region ----------------------------------------------------> Position
		self.CenterOnParent()
		#endregion -------------------------------------------------> Position

		#region --------------------------------------------------------> Bind
		self.nRes.btn.Bind(wx.EVT_BUTTON, self.OnCreate)
		self.Bind(wx.EVT_BUTTON, self.OnOkCheck)
		#endregion -----------------------------------------------------> Bind

		#region ----------------------------------------------> Initial Values
		self.OnInitVal()
		#endregion -------------------------------------------> Initial Values
	#---
	#endregion -----------------------------------------------> Instance setup

	#region ---------------------------------------------------> Class methods
	def OnOkCheck(self, event):
		"""Check widgets created after window initialization and perform checks
			involving several widgets 
		
			Parameters
			----------
			event : wx.Event
				Information about the event
		"""
		#region ----------------------------------------------> Skip if Cancel
		if event.GetEventObject().GetId() == wx.ID_OK:
			pass
		else:
			event.Skip()
			return True
		#endregion -------------------------------------------> Skip if Cancel

		#region ---------------------------------------------------> Variables
		values = []
		#endregion ------------------------------------------------> Variables

		#region -------------------------------------------------------> Check
		#--> Make sure there are widgets to check
		if self.tcPosList is None:
			event.Skip()
			return False
		else:
			pass
		#--> Check widgets
		for k,v in enumerate(self.tcPosList):
			#--> Skip first item, it is not a wx.TextCtrl
			if k == 0:
				continue
			else:
				pass
			#--> Check content
			if v.GetValidator().Validate(self):
				pass
			else:
				return False
			#--> Check unique values
			if (p := v.GetValue()) not in values:
				values.append(p)
			else:
				msg = config.msg['Error'][self.name]['PosUnique']
				dtsWindow.MessageDialog('errorF', msg, parent=self)
				return False
		#endregion ----------------------------------------------------> Check

		event.Skip()
	#---

	def OnInitVal(self):
		"""Fill the fields in the window if parent.posAA is not empty """
		#region -------------------------------> Get string from parent window
		tStr = self.parent.posAA.tc.GetValue()
		#endregion ----------------------------> Get string from parent window
		
		#region ----------------------------------------> Create & fill fields
		if tStr == '':
			return False
		else:
			tDict = ast.literal_eval(tStr)
			#--> To exclude the position key
			NRow = len(tDict) - 1
			Pos = tDict[config.dictKey[self.name]['PosKey']]
			#--> Create fields
			self.nRes.tc.SetValue(str(NRow))
			self.OnCreate('event')
			#--> Fill fields
			for i, (k, v) in enumerate(tDict.items(), start=1):
				if k != config.dictKey[self.name]['PosKey']:
					self.tcAAList[i].SetValue(v)
					if Pos:
						self.tcPosList[i].SetValue(str(k))
					else:
						pass
			#-->
			return True
		#endregion -------------------------------------> Create & fill fields
	#---

	def OnCreate(self, event):
		"""Create the fields for configuring the positions 

			Parameters
			----------
			event : wx.Event
				Information about the event
		"""
	 	#region ----------------------------------------------------> Validate
		if self.nRes.tc.GetValidator().Validate(self):
			pass
		else:
			return False
		#endregion -------------------------------------------------> Validate

		#region ---------------------------------------------------> Variables
		self.nRow = int(self.nRes.tc.GetValue())
		self.tcAAList   = []
		self.tcPosList  = []
		self.stPosList  = []
		#endregion ------------------------------------------------> Variables

		#region -----------------------------------------------> Create fields
		#--> Create the header
		self.stPosList.append(wx.StaticText(
			self.swMatrix,
			label='Position',
			)
		)
		self.tcPosList.append(wx.StaticText(
			self.swMatrix,
			label = config.label[self.name]['Position'],
			)
		)
		self.tcAAList.append(wx.StaticText(
			self.swMatrix,
			label = config.label[self.name]['AA'],
			)
		)
		#--> Create the fields
		for a in range(self.nRow):
			#--> Consensus position
			self.stPosList.append(wx.StaticText(
				self.swMatrix,
				label = str(a+1),
				)
			)
			#--> Residue number
			self.tcPosList.append(
				wx.TextCtrl(
					self.swMatrix,
					size  = config.size['TextCtrl'][self.name]['Position'],
					style = wx.TE_CENTRE,
					validator = dtsValidator.NumberList(
						self,
						config.msg['Error'][self.name]['Position'],
						refMin = 1,
					),
				)
			)
			self.tcPosList[a+1].SetHint(config.hint[self.name]['Position'])
			#--> Amino Acids
			self.tcAAList.append(
				wx.TextCtrl(
					self.swMatrix,
					size = config.size['TextCtrl'][self.name]['AA'],
				)
			)
			self.tcAAList[a+1].SetHint(config.hint[self.name]['AA'])
		#endregion --------------------------------------------> Create fields

		#region ------------------------------------------------------> Sizers
		#--> Delete old
		self.swSizer.Clear(delete_windows=True)
		#--> Update number of rows in the sizer. +1 because of the header
		self.swSizer.SetRows(self.nRow+1)
		#--> Add
		for k, v in enumerate(self.tcAAList):
			#--> Extra border to separate the header from the fields
			if k > 0:
				border = 2
				flagAA = wx.EXPAND|wx.ALL
			else:
				flagAA = wx.ALIGN_CENTER|wx.ALL
				border = 5
			#--> Add
			self.swSizer.Add(
				self.stPosList[k],
				flag   = wx.ALIGN_CENTER|wx.ALL,
				border = border,
			)
			self.swSizer.Add(
				self.tcPosList[k],
				flag   = wx.ALIGN_CENTER|wx.ALL,
				border = border,
			)
			self.swSizer.Add(
				v,
				flag   = flagAA,
				border = border,
		)
		#--> Fit Sizer
		self.swSizer.FitInside(self.swMatrix)
	 	#--> Adjust the size of the scrolled window
		self.swMatrix.SetVirtualSize(self.swSizer.GetSize())
		self.swMatrix.SetScrollRate(20,20)
		#endregion ---------------------------------------------------> Sizers
	#---
	#endregion ------------------------------------------------> Class methods
#---
#endregion ----------------------------------------------------------> Classes