# ------------------------------------------------------------------------------
# 	Copyright (C) 2019-2020 Kenny Bravo Rodriguez

# 	This program is distributed for free in the hope that it will be useful,
# 	but WITHOUT ANY WARRANTY; without even the implied warranty of
# 	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

# 	See the accompaning licence for more details.
# ------------------------------------------------------------------------------

""" This module generates the main window of the app """

#--- Imports
## Standard modules
import wx
## My modules
import config.config as config
import menu.menu as menu
from gui.win.win_base import BaseWin
from gui.win.win_tab_peptide import Peptide
from gui.win.win_tab_gene    import GeneFromFasta
from gui.win.win_tab_seqset  import Consensus
#---

class MainWin(BaseWin):
	""" This class creates the notebook """

	def __init__(self):
		""" """
	 #--- Initial setup
		self.nameWin = config.winName['main']
		super().__init__(None)
	 #--- Widgets
		self.notebook = wx.Notebook(self.winPanel)
		self.statusbar = self.CreateStatusBar()
	  #--- Tabs for the notebook 
		self.pageP = Peptide(self.notebook, self.statusbar)
		self.pageF = GeneFromFasta(self.notebook, self.statusbar)
		self.pageC = Consensus(self.notebook, self.statusbar)
		self.notebook.AddPage(self.pageP, config.tabName['pept'])
		self.notebook.AddPage(self.pageF, config.tabName['gene'])
		self.notebook.AddPage(self.pageC, config.tabName['seqset'])
	 #--- Sizers
		self.sizer.Add(
			self.notebook, 
			pos=(0,0), 
			flag=wx.EXPAND|wx.ALL, 
			border=5
		)
		self.sizer.Fit(self.winPanel)
	 #--- Position and Size
		self.Center()
		self.SetMinSize(self.GetSize())
	 #--- Show copyright in the statusbar but only one time
		if config.win['copyShow']:
			self.statusbar.SetStatusText("Copyright © 2019-2020 Kenny Bravo "
				"Rodriguez. All rights reserved."
			)
			config.win['copyShow'] = False
		else:
			pass
	 #--- Show
		self.Show()
	#---
#---