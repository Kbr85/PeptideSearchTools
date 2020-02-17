# ------------------------------------------------------------------------------
# 	Copyright (C) 2019-2020 Kenny Bravo Rodriguez

# 	This program is distributed for free in the hope that it will be useful,
# 	but WITHOUT ANY WARRANTY; without even the implied warranty of
# 	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

# 	See the accompaning licence for more details.
# ------------------------------------------------------------------------------

""" This module creates the menu of the app
"""

#--- Imports
## Standard modules
import wx
## My modules
import config.config as config
import gui.gui_methods as gmethods
#---


class MainMenuBar(wx.MenuBar):
	""" Main menu of the app """
	def __init__(self):
		""" """
		super().__init__()
	 #--- Menu items
	  #--- Notebook menu
		NoteBookMenu = wx.Menu()
		NoteBookMenu.Append(101, config.tabName['pept']+'\tAlt+Ctrl+P')
		NoteBookMenu.Append(102, config.tabName['gene']+'\tAlt+Ctrl+G')
		NoteBookMenu.Append(103, config.tabName['seqset']+'\tAlt+Ctrl+C')
	  #--- Help menu
		HelpMenu = wx.Menu()
		HelpMenu.Append(301, config.winName['help'])
		HelpMenu.AppendSeparator()
		HelpMenu.Append(302, config.winName['licagr'])
	 #--- Attach to menubar
		self.Append(NoteBookMenu, '&Search')
		self.Append(HelpMenu, '&Help')
	 #--- Bind
		self.Bind(wx.EVT_MENU, self.OnTabPeptide, id=101)
		self.Bind(wx.EVT_MENU, self.OnTabGene, id=102)
		self.Bind(wx.EVT_MENU, self.OnTabSeqSet, id=103)
		self.Bind(wx.EVT_MENU, self.OnHelp, id=301)
		self.Bind(wx.EVT_MENU, self.OnLicAgr, id=302)
	#---

 #--- Methods of the class
  #--- 100	
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

  #--- 300
	def OnLicAgr(self, event):
		""" Show the window for the Lic Agreement """
		gmethods.WinMainTypeCreate(config.winName['licagr'])
		return True
	#---

	def OnHelp(self, event):
		""" Creates the help window """
		gmethods.WinMainTypeCreate(config.winName['help'])
		return True
	#---
#---