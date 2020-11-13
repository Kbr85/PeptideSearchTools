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

"""Main window of the App
"""

#region -------------------------------------------------------------- Imports
import wx
import wx.lib.agw.aui as aui

import dat4s_core.widget.wx_window as dtsWindow

import config.config as config
import menu.menu as menu
#endregion ----------------------------------------------------------- Imports

#region ------------------------------------------------------------> Classess
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

		# self.tabMethods = {
		# 	'PeptS' : self.CreateTab_PeptS,
		# 	'Gene'  : self.CreateTab_Gene,
		# 	'SeqSet': self.CreateTab_SeqSet,
		# 	'LicAgr': self.CreateTab_LicAgr,
		# 	'Help'  : self.CreateTab_Help,
		# }

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
			agwStyle=aui.AUI_NB_TOP|aui.AUI_NB_CLOSE_ON_ALL_TABS,
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
			print(config.file['License'])
		 #--> Create tab
			self.notebook.AddPage(
				dtsWindow.LicenseWin(
					self.notebook,
					config.file['License'],
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
		 #--> Focus
			self.notebook.SetSelection(self.notebook.GetPageIndex(win))
	#---
	#endregion -------------------------------------------------> Menu methods
#---
#endregion ---------------------------------------------------------> Classess