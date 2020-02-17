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


""" This module contains the base class for all windows in the app """


#--- Imports
import wx

import config.config as config
import menu.menu as menu
#---


class BaseWin(wx.Frame):
	""" Base class for all the windows """

	def __init__(self, parent, title=None, style=None, size=None):
		""" """

	 #--> Initial Setup
		if style is None:
			style = wx.DEFAULT_FRAME_STYLE&~(wx.RESIZE_BORDER|wx.MAXIMIZE_BOX)
		else:
			pass
		if title is None:
			self.title = config.title[self.nameWin]
		else:
			self.title = title
		if size is None:
			self.size = config.size['window'][self.nameWin]
		else:
			self.size = size
		super().__init__(
			parent=parent, 
			title=self.title, 
			style=style,
			size=self.size,
		)
	 #--- Menu
		if config.cOS == "Darwin":
			pass
		else:
			self.menubar = menu.MainMenuBar()
			self.SetMenuBar(self.menubar) 
	 #--- Widgets
	  #--- Panels
		self.winPanel = wx.Panel(self)	
	 #--- Sizer
		self.sizer = wx.GridBagSizer(1, 1)	
		self.winPanel.SetSizer(self.sizer)
	 #--- Bind
		self.Bind(wx.EVT_CLOSE, self.OnClose)
		self.Bind(wx.EVT_CHAR_HOOK, self.CloseThisWin)
	#---

 #--- Methods of the class
	def OnClose(self, event):
		""" Update config.winOpen, config.WinNameVar and close the window """
	
	 #--- Handle child windows
		parent = config.win[self.nameWin].GetTopLevelParent()
		for child in parent.GetChildren():
			if isinstance(child, wx.Frame):
				child.Close()
			else:
				pass		
	 #--- Remove from Open list
		config.win['Open'].remove(config.win[self.nameWin])
	 #--- Set win to None to be able to create a new window like this
		if self.nameWin in config.win.keys():
			config.win[self.nameWin] = None
		else:
			pass
	 #--- Destroy & Return
		self.Destroy()
		return True
	#--- 

	def CloseThisWin(self, event):
		""" Close this window with keyboard Ctr/Cmd+D """
	
	 #--- Get pressed key & Close or pass
		if event.ControlDown():
			if event.GetUnicodeKey() == 68:
				self.Close()
				return True
			else:
				pass
		else:
			pass
	 #--- Skip event for furhter system processing of the keyboard input
		event.Skip()		
	 #--- Return
		return True
	#---
#---