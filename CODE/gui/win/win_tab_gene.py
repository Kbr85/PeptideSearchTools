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

""" This module generates the tab to extract the N-terminally peptides from a 
	multifasta file. Proteins in the multifasta file are filtered by a list of
	genes given in a txt file
"""

#--- Imports
import wx
from operator import itemgetter
from pathlib import Path

import config.config     as config
import data.data_methods as dmethods
from gui.win.win_tab_base import BaseTab
from gui.win.win_supp import (
	MyOpenFile,
	MyFatalErrorMessage,
	MyWarningMessageOK,
)
#---

class GeneFromFasta(BaseTab):
	""" Class to extract the first N residue from all proteins present in a 
		fasta file filtered by gene name
	"""

	#region --------------------------------------------------- Instance Setup
	def __init__(self, parent, statusbar):
		""" """

	 #--> Initial Setup
		self.nameTab = config.tabName['gene']
		super().__init__(parent=parent, statusbar=statusbar)
	 #---
	 #--> Widget
	  #--> TextCtrl
		self.tcGeneFile = wx.TextCtrl(
			self.boxFiles,   
			value="", 
			size=config.size['TextCtrl']['File'][self.nameTab], 
			style=wx.TE_READONLY
		)
	  #---
	  #--> Button
		self.buttonGeneFile = wx.Button(
			self.boxFiles, 
			label=config.tabLabel[self.nameTab]['gene'],
		)
	  #---
	 #---
	 #--> Sizers 
	  #--> Add new items
		self.sizerboxFilesWid.Detach(self.buttonOutFile)
		self.sizerboxFilesWid.Detach(self.tcOutFile)
		self.sizerboxFilesWid.Add(
			self.buttonGeneFile, 
			border=2, 
			# flag=wx.EXPAND|wx.ALIGN_CENTER|wx.ALL
			flag=wx.EXPAND|wx.ALL
		)
		self.sizerboxFilesWid.Add(
			self.tcGeneFile, 
			border=2, 
			# flag=wx.EXPAND|wx.ALIGN_CENTER|wx.ALL
			flag=wx.EXPAND|wx.ALL
		)
		self.sizerboxFilesWid.Add(
			self.buttonOutFile, 
			border=2, 
			# flag=wx.EXPAND|wx.ALIGN_CENTER|wx.ALL
			flag=wx.EXPAND|wx.ALL
		)
		self.sizerboxFilesWid.Add(
			self.tcOutFile, 
			border=2, 
			# flag=wx.EXPAND|wx.ALIGN_CENTER|wx.ALL
			flag=wx.EXPAND|wx.ALL
		)
	  #---		
	  #--> Remove not needed items
		self.sizerboxColumns.ShowItems(show=False)
	  #---
	  #--> Set & Fit
		self.tabPanel.SetSizer(self.sizerTab)
		self.sizerTab.Fit(self.tabPanel)
	  #---
	 #--> Bind
		self.buttonGeneFile.Bind(wx.EVT_BUTTON, self.OnGeneFile)
	 #---
	 #--> Initial values, DELETE before releasing
		# self.tcInputFile.SetValue('/Users/bravo/Dropbox/SCRIPTS/Tanja_Bange/Notebook-PeptideTxt-Fasta/LOCAL/DATA/NEW-DATA/HUMAN_ref_Jan2019.fasta')
		# self.tcGeneFile.SetValue("/Users/bravo/Dropbox/SCRIPTS/Tanja_Bange/Notebook-PeptideTxt-Fasta/LOCAL/DATA/NEW-DATA/XIAP_GeneNAMES.txt")
		# self.tcOutFile.SetValue('/Users/bravo/Desktop/gene.txt')
	 #---
	#---
	#endregion ------------------------------------------------ Instance Setup

	# --------------------------------------------------- Methods of the class
	#region ------------------------------------------------------------- Bind
	def OnGeneFile(self, event):
		""" Select gene file """

	 #--> Configure
		msg = config.myGeneFile[self.nameTab]['Msg']
		ext = config.myGeneFile[self.nameTab]['ExtLong']
	 #---
	 #--> Get file
		dlg = MyOpenFile(msg, ext)
		if dlg.ShowModal() == wx.ID_OK:
			self.tcGeneFile.SetValue(dlg.GetPaths()[0])
			return True
		else:
			return False	
	 #---
	#---

	def OnDef(self, event):
		""" Set default values """

		self.tcUserValue.SetValue('5 10 20 50')
		return True
	#---
	#endregion ---------------------------------------------------------- Bind

	#region ----------------------------------------------------- Run analysis
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
	 #--> Gen file
		if self.GuiCheckInputFile(
			'gFile',
			self.tcGeneFile,
			config.fatalErrorsMsg[self.nameTab]['gFile'],
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
		if self.GuiCheckListNumber(
			'r2ext',
			self.tcUserValue,
			config.fatalErrorsMsg[self.nameTab]['r2extract'],
			comp='gt',
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
		""" Read the fasta file and the gene file and extract the N-term 
			peptides to the desire length of all proteins that belong to the 
			genes.
		"""
	
	 #--> Get the list of genes
		GFile = open(str(self.do['gFile']), 'r')
		genes = []
		for line in GFile:
		 #--- To considerer mac \n or windows \r\n files
			l = line.split('\n')[0]
			ll = l.split('\r')[0]
			ll = ll.strip()
			if ll == '':
				pass
			else:
				if ';' in ll:
					lll = ll[1:-1].split(';')
					for v in lll:
						genes.append(v)
				else:
					genes.append(ll)
		genes = list(set(genes))
		GFile.close()
	 #---
	 #--> Check that something was in the file and scan the fasta file
		if len(genes) == 0:
			MyFatalErrorMessage(config.fatalErrorsMsg[self.nameTab]['noGene'])
			return False
		else:
		 #--> Scan the fasta file
			self.ltotal    = 0
			self.lempty    = 0
			self.prottotal = 0
			self.protsselT = 0
			searchP   = False
			self.dataO     = []
			FFile = open(str(self.do['iFile']), 'r')
			for line in FFile:
				self.ltotal += 1	
			 #--> To considerer mac \n or windows \r\n files
				l  = line.split('\n')[0]
				ll = l.split('\r')[0]
			 #---
				ll = ll.strip()
				if ll == '':
					self.lempty += 1
				elif ll[0] == '>':
					self.prottotal += 1
					if searchP:
						lseq = ''.join(lseq)
						for i in self.do['r2ext']:
							ltemp.append(lseq[0:i])
						self.dataO.append(ltemp)	
					else:
						pass
					if 'GN=' in ll:
						genInll = [s for s in ll.split() if 'GN=' in s][0].split('=')[1]
						if genInll in genes:
							searchP = True
							self.protsselT += 1
							ltemp = []
							lseq = []
							ltemp.append(genInll)
							ltemp.append(ll.split('|')[1])
						else:
							searchP = False
					else:
						searchP = False
				else:
					if searchP:
						lseq.append(ll)
					else:
						pass
				if self.ltotal % 100 == 0:
					self.statusbar.SetStatusText(
						'Extracting peptides:  Match Proteins:  ' 
						+ str(self.protsselT) 
						+ ',  Total Proteins:  ' 
						+ str(self.prottotal) 
						+ ',  Empty lines:  ' 
						+ str(self.lempty) 
						+ ',  Total lines:  ' 
						+ str(self.ltotal)
					)
					wx.Yield()
				else:
					pass	
			FFile.close()
		 #--> Last pass to catch the last protein
			if searchP:
				lseq = ''.join(lseq)
				for i in self.do['r2ext']:
					ltemp.append(lseq[0:i])
				self.dataO.append(ltemp)	
			else:
				pass
	 #---
	 #--> Return
		return True
	 #---
	#---

	def WriteOutput(self):
		""" Write the output """
	 
	 #--> Check there is something to write
		if self.protsselT == 0:
			MyWarningMessageOK(config.fatalErrorsMsg[self.nameTab]['noProt'])
			return False
		else:
		 #--> Input data
			oFile = open(str(self.do['oFile']), 'w')
			oFile.write('Input data:\n')
			dmethods.FFsWriteDict(oFile, self.d, config.helperDict[self.nameTab])
			oFile.write('\n')
		 #---
		 #--> Output Data
		  #--- Header
			oFile.write('Output data:\n')
			oFile.write('Gene\tProtein\t')
			end = len(self.do['r2ext'])
			for k, i in enumerate(self.do['r2ext'], start=1):
				if k < end:
					oFile.write('1-' + str(i) + '\t')
				else:
					oFile.write('1-' + str(i) + '\n')
			end = len(self.dataO)
		  #---
		  #--> Data
			self.dataO.sort(key=itemgetter(0, 1))
			dmethods.FFsWriteList(oFile, self.dataO)
			oFile.write('\n\n')
		  #---
		  #--> File last line
			dmethods.FFsWriteLastLine(oFile)
		  #---
		 #---
		 #--> Close
			oFile.close()
			self.statusbar.SetStatusText(
				'All done!!! Match Proteins:  ' 
				+ str(self.protsselT) 
				+ ',  Total Proteins:  ' 
				+ str(self.prottotal) 
				+ ',  Empty lines:  ' 
				+ str(self.lempty) 
				+ ',  Total lines:  ' 
				+ str(self.ltotal)
			)
		 #---
	 #---
	 #-->	
		return True
	 #---
	#---
	#endregion -------------------------------------------------- Run analysis
#---




