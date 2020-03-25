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


""" This module creates the base class for the windows showing help like
	information -> menu.Help and menu.LicAgreement
"""


#--- Imports
import wx

import config.config as config
import menu.menu as menu
from gui.win.win_base import BaseWin
#---


class HelpWinBase(BaseWin):
	""" Creates the windows to show the help and lic. agreement """

	#region --------------------------------------------------- Instance Setup
	def __init__(self, parent=None):
		"""  """

	 #--> Initial Setup
		super().__init__(None)
	 #---
	 #--> Widgets
	  #--> TextCtrl
		self.MyText = wx.TextCtrl(
			self.winPanel, 
			size=config.size['TextCtrl'][self.nameWin], 
			style=wx.TE_MULTILINE|wx.TE_WORDWRAP|wx.TE_READONLY)
	  #---
	  #--> Button
		self.buttonOk = wx.Button(self.winPanel, label='Ok')
	  #---
	 #---
	 #--> Sizer
		self.sizer.Add(
			self.MyText,
			pos=(0,0),
			flag=wx.EXPAND|wx.ALL, 
			border=5,
		)
		self.sizer.Add(
			self.buttonOk,
			pos=(1,0),
			flag=wx.ALIGN_CENTER|wx.ALL, 
			border=5,
		)
		self.sizer.Fit(self.winPanel)
	 #---
	 #--> Bind
		self.buttonOk.Bind(wx.EVT_BUTTON, self.OnOkBtn)
	 #---
	 #--> Show 		
		self.Show()
	 #---
	#---
	#endregion ------------------------------------------------ Instance Setup

	# --------------------------------------------------- Methods of the class
	#region ------------------------------------------------------------- Bind
	def OnOkBtn(self, event):
		""" Just close the window """
	
		self.OnClose(event)
		return True
	#---
	#endregion ---------------------------------------------------------- Bind
#---

