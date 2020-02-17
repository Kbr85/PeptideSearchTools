# ------------------------------------------------------------------------------
# Author: Kenny Bravo Rodriguez 2019 (kenny.bravorodriguez@mpi-dortmund.mpg.de)
# 
# Copyright (c) 2019-2020 Max Planck Institute of Molecular Physiology
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


""" This module generates the main window of the app """


#--- Imports
import wx

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
			self.statusbar.SetStatusText(config.msg['Copyright'])
			config.win['copyShow'] = False
		else:
			pass
	 #--- Show
		self.Show()
	#---
#---