# ------------------------------------------------------------------------------
# 	Copyright (C) 2019-2020 Kenny Bravo Rodriguez

# 	This program is distributed for free in the hope that it will be useful,
# 	but WITHOUT ANY WARRANTY; without even the implied warranty of
# 	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

# 	See the accompaning licence for more details.
# ------------------------------------------------------------------------------

""" This module starts the application """

#--- Imports
## Standard modules
import wx
## My modules
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
	 #--> Show the main frame & Return
		gmethods.WinMainTypeCreate(config.winName["main"])
		return True
	#---
	####---- Methods of the class
	def AppInit(self):
		""" Define parameters that requires a wx.App to be already running """
	   
	 #--> MenuBar
		if config.cOS == "Darwin":
			wx.MenuBar.MacSetCommonMenuBar(menu.MainMenuBar())
		else:
			pass
	 #--> Configuration options
	  #--> Pointers
		config.pointer['gmethods']['WinCreate'] = { # Modules/util windows
			config.winName['main']      : MainWin,
			config.winName['licagr']    : LicAgreementWin,
			config.winName['help']      : HelpWin,
			config.winName['confSearch']: ConsensusSearchConfig,
		}
	 #--> Return
		return True
	#---
#---

if __name__ == "__main__":
	app = PeptideSearchToolApp()
	app.MainLoop()
else:
	pass