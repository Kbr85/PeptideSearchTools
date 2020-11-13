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


""" This module generates the tab to locate the  N-terminally peptide in a 
	MaxQuant peptide.txt file
"""


#--- Imports
import wx
from pathlib import Path

import config.config     as config
import data.data_methods as dmethods
from gui.win.win_tab_base import BaseTab
from gui.win.win_supp import MyWarningMessageOK
#---


class Peptide(BaseTab):
	""" Class to create the panel extracting the terminal peptides from a 
		MaxQuant peptide.txt file
	"""

	#region --------------------------------------------------- Instance Setup
	def __init__(self, parent, statusbar):
		""" """

	 #--> Initial Setup
		self.nameTab = config.tabName['pept']
		super().__init__(parent=parent, statusbar=statusbar)
	 #---
	 #--> Widgets
	  #--> Text Control
		self.tcStartResCol = wx.TextCtrl(
			self.boxColumns, 
			value='', 
			size=config.size['TextCtrl']['Column'][self.nameTab],
		)
		self.tcCol2ExtrCol = wx.TextCtrl(
			self.boxColumns, 
			value='', 
			size=config.size['TextCtrl']['Column'][self.nameTab],
		)
	  #---
	  #--> Static Text
		self.stStartResCol = wx.StaticText(
			self.boxColumns, 
			label='Start Residue', 
			style=wx.ALIGN_RIGHT
		)
		self.stCol2ExtrCol = wx.StaticText(
			self.boxColumns, 
			label='Columns to Extract', 
			style=wx.ALIGN_RIGHT
		)
	  #---
	 #---
	 #--> Sizers
	  #--> Add New Elements
		self.sizerboxColumnsWid.Add(
			self.stStartResCol, 
			border=2, 
			flag=wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.ALL
		)
		self.sizerboxColumnsWid.Add(
			self.tcStartResCol, 
			border=2, 
			# flag=wx.EXPAND|wx.ALIGN_CENTER|wx.ALL
			flag=wx.EXPAND|wx.ALL
		)
		self.sizerboxColumnsWid.Add(
			self.stCol2ExtrCol, 
			border=2, 
			flag=wx.ALIGN_CENTER|wx.ALL
		)
		self.sizerboxColumnsWid.Add(
			self.tcCol2ExtrCol, 
			border=2, 
			# flag=wx.EXPAND|wx.ALIGN_CENTER|wx.ALL
			flag=wx.EXPAND|wx.ALL
		)
	  #---	 
	  #--> Set & Fit
		self.tabPanel.SetSizer(self.sizerTab)
		self.sizerTab.Fit(self.tabPanel)
	  #---
	 #---
	 #--> Initial values, DELETE before releasing
		# self.tcInputFile.SetValue('/Users/bravo/Dropbox/SCRIPTS/Tanja_Bange/Notebook-PeptideTxt-Fasta/LOCAL/DATA/NEW-DATA/peptides.txt')
		# self.tcOutFile.SetValue('/Users/bravo/Desktop/peptide.txt')
	 #---
	#---
	#endregion ------------------------------------------------ Instance Setup

 	# --------------------------------------------------- Methods of the class
	#region ------------------------------------------------------------- Bind
	def OnDef(self, event):
		""" Set default values """

		self.tcUserValue.SetValue('2')
		self.tcStartResCol.SetValue('36')
		self.tcCol2ExtrCol.SetValue('0 38 36 37')
		return True
	#---
	#endregion ---------------------------------------------------------- Bind

	#region ----------------------------------------------------- Run Analysis
	def CheckInput(self):
		""" Check the input """
	
	 #--> Input file
		if self.GuiCheckInputFile(
			'iFile',
			self.tcInputFile,
			config.fatalErrorsMsg[self.nameTab]['iFile'],
		):
			pass
		else:
			return False
	 #---
	 #--> Output file
		if self.GuiCheckOutFile(
			'oFile',
			self.tcOutFile,
			config.fatalErrorsMsg[self.nameTab]['oFile'],
		):
			pass
		else:
			return False
	 #---
	 #--> First residue
		if self.GuiCheckInteger(
			'fRes',
			self.tcUserValue,
			config.fatalErrorsMsg[self.nameTab]['fRes'],
		):
			pass
		else:
			return False
	 #---
	 #--> Start residue
		if self.GuiCheckInteger(
			'fResCol',
			self.tcStartResCol,
			config.fatalErrorsMsg[self.nameTab]['fResCol'],
			comp='egt',
		):
			pass
		else:
			return False
	 #---
	 #--> Columns to extract
		if self.GuiCheckListNumber(
			'Col2Ext',
			self.tcCol2ExtrCol,
			config.fatalErrorsMsg[self.nameTab]['col2Ext'],
		):
			pass
		else:
			return False
	 #---
	 #--> Return
		return True
	 #---
	#---

	def DataProcessing(self):
		""" Extract the selected columns from the rows with peptides starting  
			in the selected residue number
		"""

	 #--> Variables and read file
		iFile = open(str(self.do['iFile']), 'r')
		self.lempty = 0
		self.ltotal = 0
		self.ptotal = 0
		self.dataO = []
	 #---
	 #--> Process file
		for line in iFile:
			self.ltotal += 1	
		 #--> To considerer mac \n or windows \r\n files
			l = line.split('\n')[0]
			ll = l.split('\r')[0]
		 #---
			lll = ll.split('\t')
			if self.ltotal == 1:
			 #--- Set the header for the output file
				self.header = []
				for i in self.do['Col2Ext']:
					self.header.append(lll[i])
				self.header = '\t'.join(self.header)
			else:
				pass
			if lll[0] == '':
				self.lempty += 1
			else:
				try:
					tres = int(lll[self.do['fResCol']])
					go = True
				except Exception:
					self.lempty += 1
					go = False
				if go:
					if tres <= self.do['fRes']:
						ltemp = []
						for i in self.do['Col2Ext']:
							ltemp.append(lll[i])
						self.dataO.append(ltemp)
						self.ptotal += 1
					else:
						pass
				else:
					pass
			self.statusbar.SetStatusText(
				'Extracting peptides: Peptides Found  ' 
				+ str(self.ptotal) 
				+ ',  Empty Lines Found:  ' 
				+ str(self.lempty) 
				+ ',  Total Analyzed Lines:  ' 
				+ str(self.ltotal)
			)
			wx.Yield()
		iFile.close()	
	 #---
	 #--> Return
		return True
	 #---
	#---

	def WriteOutput(self):
		""" Write the output """

	 #--> Check there is something to write	
		if self.ptotal == 0:
			MyWarningMessageOK(config.fatalErrorsMsg[self.nameTab]['NoPeptide'])
			return False
		else:
		 #--> Write input data
			oFile = open(str(self.do['oFile']), 'w')
			oFile.write('Input data:\n')
			dmethods.FFsWriteDict(oFile, self.d, config.helperDict[self.nameTab])
			oFile.write('\n')
		 #---
		 #--> Write output
			oFile.write('Output data:\n')
			oFile.write(str(self.header) + '\n')
			dmethods.FFsWriteList(oFile, self.dataO)
			oFile.write('\n\n')
		 #---
		 #--> File last line
			dmethods.FFsWriteLastLine(oFile)
		 #---
		 #--> Close file and final summary in statusbar
			oFile.close()
			self.statusbar.SetStatusText(
				'All done!!! Peptides Found  ' 
				+ str(self.ptotal) 
				+ ',  Empty Lines Found:  ' 
				+ str(self.lempty) 
				+ ',  Total Analyzed Lines:  ' 
				+ str(self.ltotal)
			)
		 #---
	 #---
	 #-->
		return True
	 #---
	#---
	#endregion -------------------------------------------------- Run Analysis
#---




