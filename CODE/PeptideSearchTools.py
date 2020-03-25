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


""" This module starts the application """


#--- Imports
import wx

import config.config as config
import menu.menu as menu
import gui.gui_methods as gmethods
from gui.win.win_main import MainWin 
from gui.win.win_help import HelpWin
from gui.win.win_lic_agreement import LicAgreementWin
from gui.win.win_seqset_conf import ConsensusSearchConfig
#---


class PeptideSearchToolApp(wx.App):
	""" Initial Setup of the App """
	
	def OnInit(self):
		""" Initialize the app """
		
	 #--> Set special configuration values that require a running wx.App
		self.AppInit()
	 #---
	 #--> Show the main frame & Return
		gmethods.WinMainTypeCreate(config.winName["main"])
	 #---
	 #--> Return
		return True
	 #---
	#---


	def AppInit(self):
		""" Define parameters that requires a wx.App to be already running """
	   
	 #--> MenuBar
		if config.cOS == "Darwin":
			wx.MenuBar.MacSetCommonMenuBar(menu.MainMenuBar())
		else:
			pass
	 #---
	 #--> Configuration options
	  #--> Pointers
		config.pointer['gmethods']['WinCreate'] = { # Modules/util windows
			config.winName['main']      : MainWin,
			config.winName['licagr']    : LicAgreementWin,
			config.winName['help']      : HelpWin,
			config.winName['confSearch']: ConsensusSearchConfig,
		}
	 #---
	 #--> Return
		return True
	 #---
	#---
#---


if __name__ == "__main__":
	app = PeptideSearchToolApp()
	app.MainLoop()
else:
	pass