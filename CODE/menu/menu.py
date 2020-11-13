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


""" This module creates the menu of the app """


#region -------------------------------------------------------------> Imports
import wx

import config.config as config
import gui.gui_methods as gmethods
#endregion ----------------------------------------------------------> Imports

#region ----------------------------------------------------> Individual menus
class SearchMenu(wx.Menu):
	"""Search menu of the app"""

	#region --------------------------------------------------- Instance Setup
	def __init__(self):
		""" """
		#region -----------------------------------------------> Initial setup
		super().__init__()
	 	#endregion --------------------------------------------> Initial setup

		#region --------------------------------------------------> Menu items
		self.pept   = self.Append(-1, config.tabName['pept']+'\tAlt+Ctrl+P')
		self.gene   = self.Append(-1, config.tabName['gene']+'\tAlt+Ctrl+G')
		self.seqset = self.Append(-1, config.tabName['seqset']+'\tAlt+Ctrl+C')
		#endregion -----------------------------------------------> Menu items

		#region --------------------------------------------------------> Bind
		self.Bind(wx.EVT_MENU, self.OnTabPeptide, source=self.pept)
		self.Bind(wx.EVT_MENU, self.OnTabGene,    source=self.gene)
		self.Bind(wx.EVT_MENU, self.OnTabSeqSet,  source=self.seqset)
		#endregion -----------------------------------------------------> Bind
	 #---
	#---
	#endregion -----------------------------------------------> Instance setup

	#region ---------------------------------------------------> Class methods
	def OnTabPeptide(self, event):
		""" Creates the main window and show the peptide tab """

		gmethods.TabSelect(config.tabOrder[config.tabName['pept']])
		return True
	#---

	def OnTabGene(self, event):
		""" Creates the main window and change to the gene tab """

		gmethods.TabSelect(config.tabOrder[config.tabName['gene']])
		return True
	#---

	def OnTabSeqSet(self, event):
		""" Creates the main window and change to the consensus tab """

		gmethods.TabSelect(config.tabOrder[config.tabName['seqset']])
		return True
	#---	
	#endregion ------------------------------------------------> Class methods
#---

class HelpMenu(wx.Menu):
	"""Help menu of the app"""

	#region --------------------------------------------------- Instance Setup
	def __init__(self):
		""" """
		#region -----------------------------------------------> Initial setup
		super().__init__()
	 	#endregion --------------------------------------------> Initial setup

		#region --------------------------------------------------> Menu items
		self.help = self.Append(-1, config.winName['help'])
		self.AppendSeparator()
		self.lic = self.Append(-1, config.winName['licagr'])
		#endregion -----------------------------------------------> Menu items

		#region --------------------------------------------------------> Bind
		self.Bind(wx.EVT_MENU, self.OnHelp,   source = self.help)
		self.Bind(wx.EVT_MENU, self.OnLicAgr, source = self.lic)
		#endregion -----------------------------------------------------> Bind
	 #---
	#---
	#endregion -----------------------------------------------> Instance setup

	#region ---------------------------------------------------> Class methods
	def OnLicAgr(self, event):
		""" Show the window for the Lic Agreement """

		gmethods.WinMainTypeCreate(config.winName['licagr'])
		return True
	#---

	def OnHelp(self, event):
		""" Creates the help window """

		gmethods.WinMainTypeCreate(config.winName['help'])
		return True
	#endregion ------------------------------------------------> Class methods
#---

#endregion -------------------------------------------------> Individual menus

#region ------------------------------------------------------------> MenuBars
class MainMenuBar(wx.MenuBar):
	""" Main menu of the app """

	#region --------------------------------------------------- Instance Setup
	def __init__(self):
		""" """
		#region -----------------------------------------------> Initial setup
		super().__init__()
	 	#endregion --------------------------------------------> Initial setup
		
		#region -------------------------------------------------------> Menus
		search = SearchMenu()
		helpM = HelpMenu() 

		self.Append(search, '&Search')
		self.Append(helpM, '&Help')
		#endregion ----------------------------------------------------> Menus
	#---
	#endregion ------------------------------------------------ Instance Setup
#---
#endregion ---------------------------------------------------------> MenuBars


