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

#region ----------------------------------------------------------> Base menus
class MenuMethods():
	"""Hold common methods for the individual menu Classes
	
		Methods
		-------
		CreateTab(config.name['X'])
			Creates the tab for X
	"""
	#region ---------------------------------------------------> Class methods
	def CreateTab(self, event):
		""" Creates the selected tab 
		
			Parameters
			----------
			event : wx.Event
				Event information
		"""

		win = self.GetWindow()

		if win.CreateTab(self.tab[event.GetId()]):
			return True
		else:
			return False
	#---	
	#endregion ------------------------------------------------> Class methods
#endregion -------------------------------------------------------> Base menus

#region ----------------------------------------------------> Individual menus
class SearchMenu(wx.Menu, MenuMethods):
	"""Search menu of the app
	
		Attributes
		----------
		tab : dict
			To know which tab to create based on the selected menu item
	"""

	#region -----------------------------------------------------> Class setup
	tab = {
		1 : config.name['Tab']['PeptS'],
		2 : config.name['Tab']['Gene'],
		3 : config.name['Tab']['SeqSet'],
	}
	#endregion --------------------------------------------------> Class setup
	
	#region --------------------------------------------------> Instance setup
	def __init__(self):
		""" """
		#region -----------------------------------------------> Initial setup
		super().__init__()
	 	#endregion --------------------------------------------> Initial setup

		#region --------------------------------------------------> Menu items
		self.Append(1, config.title['PeptS']+'\tAlt+Ctrl+P')
		self.Append(2, config.title['Gene']+'\tAlt+Ctrl+G')
		self.Append(3, config.title['SeqSet']+'\tAlt+Ctrl+C')
		#endregion -----------------------------------------------> Menu items

		#region --------------------------------------------------------> Bind
		self.Bind(wx.EVT_MENU, self.CreateTab, id=1)
		self.Bind(wx.EVT_MENU, self.CreateTab, id=2)
		self.Bind(wx.EVT_MENU, self.CreateTab, id=3)
		#endregion -----------------------------------------------------> Bind
	 #---
	#---
	#endregion -----------------------------------------------> Instance setup
#---

class HelpMenu(wx.Menu, MenuMethods):
	"""Help menu of the app
	
		Attributes
		----------
		tab : dict
			To know which tab to create based on the selected menu item	
	"""

	#region -----------------------------------------------------> Class setup
	tab = {
		1 : config.name['Tab']['Help'],
		2 : config.name['Tab']['LicAgr'],
	}
	#endregion --------------------------------------------------> Class setup

	#region --------------------------------------------------- Instance Setup
	def __init__(self):
		""" """
		#region -----------------------------------------------> Initial setup
		super().__init__()
	 	#endregion --------------------------------------------> Initial setup

		#region --------------------------------------------------> Menu items
		self.Append(1, config.title['Help'])
		self.AppendSeparator()
		self.Append(2, config.title['LicAgr'])
		#endregion -----------------------------------------------> Menu items

		#region --------------------------------------------------------> Bind
		self.Bind(wx.EVT_MENU, self.CreateTab, id=1)
		self.Bind(wx.EVT_MENU, self.CreateTab, id=2)
		#endregion -----------------------------------------------------> Bind
	 #---
	#---
	#endregion -----------------------------------------------> Instance setup
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


