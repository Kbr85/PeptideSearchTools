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

#region -------------------------------------------------------------> Imports
import os
import platform

import wx
import wx.adv
#region -------------------------------------------------------------> Imports

DEVELOPMENT = True # # Control variables with different values in dev or prod

#region ------------------------------------------------------------> Classess
class PeptideSearchToolApp(wx.App):
	""" Initial Setup of the App """
	
	#region ----------------------------------------------> Overridden methods
	def OnInit(self):
		""" Initialize the app """
		
		#region -------------------------------------------> Show SplashScreen
		cwd = os.path.abspath(os.path.dirname(__file__))
		cOS = platform.system()

		if cOS == 'Darwin':
			if DEVELOPMENT:
				image_loc = (
					cwd 
					+ '/RESOURCES/IMAGES/SPLASHSCREEN/splashscreen.png'
				)
			else:
				image_loc = (
					cwd 
					+ '/PeptideSearchTools.app/Contents/Resources/IMAGES/SPLASHSCREEN/splashscreen.png'
				)
		else:
			image_loc = cwd + '/RESOURCES/IMAGES/SPLASHSCREEN/splashscreen.png'
		
		bitmap = wx.Bitmap(image_loc, type=wx.BITMAP_TYPE_PNG)
		
		SplashWindow(bitmap)
		#endregion ----------------------------------------> Show SplashScreen

		return True
	#---
	#endregion -------------------------------------------> Overridden methods
#---

class SplashWindow(wx.adv.SplashScreen):
	"""Create splash screen 
		
		Parameter
		---------
		bitmap : bitmap
			Image for the splash window
	"""
	#region --------------------------------------------------> Instance setup
	def __init__(self, bitmap):
		""""""
		#region -----------------------------------------------> Initial setup
		super().__init__(
			bitmap, 
			wx.adv.SPLASH_CENTER_ON_SCREEN|wx.adv.SPLASH_TIMEOUT,
			1000,
			None,	
		)
		#endregion --------------------------------------------> Initial setup
	
		#region --------------------------------------------------------> Bind
		self.Bind(wx.EVT_CLOSE, self.OnClose)
		#endregion -----------------------------------------------------> Bind
		
		#region ---------------------------------------------> Position & Show
		self.Show()
		#endregion ------------------------------------------> Position & Show
	#---
	#endregion -----------------------------------------------> Instance setup

	#region ----------------------------------------------> Overridden methods
	def OnClose(self, event):
		""" Finish app configuration.

			Overridden method
		"""

		#region	-----------------------------------------------------> Imports
		import config.config as config
		import menu.menu as menu
		import gui.window as window
		#endregion---------------------------------------------------> Imports

		#region -----------------------------------------------------> MenuBar
		if config.cOS == "Darwin":
			wx.MenuBar.MacSetCommonMenuBar(menu.MainMenuBar())
		else:
			pass
		#endregion --------------------------------------------------> MenuBar

		#region ------------------------------------------> Create main window
		window.MainWindow()
		#endregion ---------------------------------------> Create main window

		#region --------------------------------------------> Destroy & Return
		self.Destroy()
		return True
		#endregion -----------------------------------------> Destroy & Return
	#---
	#endregion -------------------------------------------> Overridden methods
#---

#endregion ---------------------------------------------------------> Classess

#region -----------------------------------------------------------> Start App
if __name__ == "__main__":
	app = PeptideSearchToolApp()
	app.MainLoop()
else:
	pass
#endregion --------------------------------------------------------> Start App

