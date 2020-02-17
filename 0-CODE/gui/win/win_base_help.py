# ------------------------------------------------------------------------------
# 	Copyright (C) 2019-2020 Kenny Bravo Rodriguez

# 	This program is distributed for free in the hope that it will be useful,
# 	but WITHOUT ANY WARRANTY; without even the implied warranty of
# 	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

# 	See the accompaning licence for more details.
# ------------------------------------------------------------------------------

""" This module creates the base class for the windows showing help like
	menu.Help and menu.LicAgreement
"""

#--- Imports
## Standard modules
import wx
## My modules
import config.config as config
import menu.menu as menu
from gui.win.win_base import BaseWin
#---

class HelpWinBase(BaseWin):
	""" Creates the windows to show the help and lic. agreement """

	def __init__(self, parent=None):
		"""  """

	 #--- Initial Setup
		super().__init__(None)
	 #--- Widgets
	  #--- TextCtrl
		self.MyText = wx.TextCtrl(
			self.winPanel, 
			size=config.size['TextCtrl'][self.nameWin], 
			style=wx.TE_MULTILINE|wx.TE_WORDWRAP|wx.TE_READONLY)
	  #--> Button
		self.buttonOk = wx.Button(self.winPanel, label='Ok')
	 #--- Sizer
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
	 #--- Bind
		self.buttonOk.Bind(wx.EVT_BUTTON, self.OnOkBtn)
	 #--- Show 		
		self.Show()
	#---
 #--- Methods of the class
	def OnOkBtn(self, event):
		""" Just close the window """
		self.OnClose(event)
		return True
	#---
#---

