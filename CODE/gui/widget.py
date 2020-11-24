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

"""Classes and methods to create GUI elements formed by more than one widget 
from wxPython or one widget with a fairly complicated initialization process.
"""

#region -------------------------------------------------------------> Imports
import wx

import dat4s_core.widget.wx_widget as dtsWidget

import config.config as config
#endregion ----------------------------------------------------------> Imports

#region ------------------------------------------------------------> Classess
class ButtonGroup():
	"""Group of three buttons at the bottom of the tabs. This includes the run
		button. 
		
		Parameters
		----------
		parent : wx widget
			Parent of the widgets

		Attributes
		----------
		btnClear : wx.Button
			Button bound to self.OnClear
		btnValue : wx.Button
			Button bound to self.OnValue
		btnRun : dtsWidget.BtnRun 
			Button to start the analysis
		Sizer : wx.FlexGridSizer
			To align the buttons
	"""

	#region -----------------------------------------------------> Class setup
	#endregion --------------------------------------------------> Class setup	

	#region --------------------------------------------------> Instance setup
	def __init__(self, parent):
		""""""
		#region -----------------------------------------------> Initial setup
		
		#endregion --------------------------------------------> Initial setup

		#region -----------------------------------------------------> Widgets
		self.btnClear = wx.Button(
			parent = parent,
			label  = config.label['ButtonGroup']['Clear'],
		)
		self.btnValue = wx.Button(
			parent = parent,
			label  = config.label['ButtonGroup']['Value'],
		)
		self.btnRun = dtsWidget.ButtonRun(
			parent = parent,
			label  = config.label['ButtonGroup']['Clear'],
		)
		#endregion --------------------------------------------------> Widgets

		#region ------------------------------------------------------> Sizers
		self.Sizer = wx.FlexGridSizer(1, 3, 1, 1)
		self.Sizer.Add(
			self.btnClear,
			border = 2,
			flag   = wx.EXPAND|wx.ALL
		)
		self.Sizer.Add(
			self.btnValue, 
			border = 2,
			flag   = wx.EXPAND|wx.ALL
		)
		self.Sizer.Add(
			self.btnRun,
			border = 2,
			flag   = wx.EXPAND|wx.ALL
		)
		#endregion ---------------------------------------------------> Sizers

		#region --------------------------------------------------------> Bind
		self.btnClear.Bind(wx.EVT_BUTTON, self.OnClear)
		self.btnValue.Bind(wx.EVT_BUTTON, self.OnValue)
		#endregion -----------------------------------------------------> Bind
	#endregion -----------------------------------------------> Instance setup

	#region ---------------------------------------------------> Class methods
	def OnClear(self, event):
		""" Clear all user provided input. Override as needed.

			Parameters
			----------
			event: wx.Event
		"""
		return True
	#---

	def OnValue(self, event):
		""" Load default values for GUI's fields. Override as needed.

			Parameters
			----------
			event: wx.Event
		"""
		return True
	#---
	#endregion ------------------------------------------------> Class methods
#---
#endregion ---------------------------------------------------------> Classess