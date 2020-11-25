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

"""Individuals tabs for the App
"""

#region -------------------------------------------------------------- Imports
import wx
import wx.lib.agw.aui as aui

import dat4s_core.widget.wx_widget as dtsWidget

import config.config as config
import gui.pane as pstPane
#endregion ----------------------------------------------------------- Imports



#region -------------------------------------------------------------> Classes
class PeptideTab(wx.Panel):
	"""Tab for the peptide search 
	
		Parameters
		----------
		parent : wx widget or None
			Parent of the tab
		name : str
			To identify the tab
		statusbar : wx.StatusBar
			Statusbar of the main window to show msgs

		Attributes
		----------
		lc : dtsWidget.ListZebra
			This is a wx.ListCtrl to display the column's name in the Data File
		userInput : pstPane.PeptidePane
			User input section of the Tab
		_mgr : aui.AuiManager()
			aui manager for the tab
	"""
	#region --------------------------------------------------> Instance setup
	def __init__(self, parent, name, statusbar):
		""""""
		#region -----------------------------------------------> Initial setup
		super().__init__(parent, name=name)
		#endregion --------------------------------------------> Initial setup
		
		#region -----------------------------------------------------> Widgets
		self.lc = dtsWidget.ListZebra(
			self, 
			colLabel = config.label['Peptide']['Column'],
			colSize = config.size['ListCtrl']['Peptide'],
		)
		self.userInput = pstPane.PeptidePane(self, statusbar, lc=self.lc)
		#endregion --------------------------------------------------> Widgets

		#region -------------------------------------------------> AUI Control
		self._mgr = aui.AuiManager()
		self._mgr.SetManagedWindow(self)
		#--> Add standard panels
		self._mgr.AddPane(
			self.userInput,
			aui.AuiPaneInfo(
				).CenterPane(
				).Caption(
					config.title['UserInput']
				).CaptionVisible(
				).Floatable(
					b=False
				).CloseButton(
					visible=False
				).Movable(
					b=False
				).PaneBorder(
					visible=False,
			),
		)
		self._mgr.AddPane(
			self.lc,
			aui.AuiPaneInfo(
				).Right(
				).Caption(
					config.title['ListCtrl']
				).Floatable(
					b=False
				).CloseButton(
					visible=False
				).Movable(
					b=False
				).PaneBorder(
					visible=False,
			),
		)
		#---
		self._mgr.Update()
		#endregion ----------------------------------------------> AUI Control
	#---
	#endregion -----------------------------------------------> Instance setup
#---
#endregion ----------------------------------------------------------> Classes