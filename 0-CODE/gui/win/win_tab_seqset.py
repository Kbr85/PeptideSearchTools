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


""" This module generates the tab to compute the ocurrence of a set of sequences
	in a multifasta file
"""


#--- Imports
import wx
import itertools
import pandas as pd
from pathlib import Path

import config.config     as config
import data.data_methods as dmethods
import gui.gui_methods as gmethods
from gui.win.win_tab_base import BaseTab
from gui.win.win_supp import MyWarningMessageOK
#---


class Consensus(BaseTab):
	""" Class to create the panel computing the probability to find a set of
		sequences in a given multifasta file
	"""

	def __init__(self, parent, statusbar):
		""" """

	 #--- Initial Setup
		self.nameTab = config.tabName['seqset']
		self.ScanDict = {
			True : self.ScanSeqWithPos,
			False: self.ScanSeqNoPos, 
		}
		super().__init__(parent=parent, statusbar=statusbar)
	 #--- Widgets		
	  #--- Button
		self.buttonConf = wx.Button(self.boxValues, label='Configure')
	  #--- Check Box
		self.cbCompProt = wx.CheckBox(
			self.boxValues,
			label=config.tabLabel[self.nameTab]['cbCompProt'],
		)	
	 #--- Sizers
	  #--- Add New Elements	
		self.sizerboxValuesWid.Add(
			self.buttonConf,
			pos=(0,2),
			flag=wx.ALIGN_RIGHT|wx.ALL,
			border=2,
		)
		self.sizerboxValuesWid.Add(
			self.cbCompProt,
			pos=(1,0),
			flag=wx.ALIGN_LEFT|wx.ALL,
			border=2,
			span=(0,2),
		)			

	  #--- Remove elements
		self.sizerboxColumns.ShowItems(show=False) 
	  #--- Set & Fit
		self.tabPanel.SetSizer(self.sizerTab)
		self.sizerTab.Fit(self.tabPanel)
	 #--- Bind
		self.buttonConf.Bind(wx.EVT_BUTTON, self.OnConf)
	 #--- Initial values, DELETE before releasing
		# self.tcInputFile.SetValue('/Users/kenny/Dropbox/SCRIPTS/Tanja_Bange/Notebook-PeptideTxt-Fasta/LOCAL/DATA/NEW-DATA/HUMAN_ref_Jan2019-cut.fasta')
		# self.tcOutFile.SetValue('/Users/kenny/Desktop/consensus.txt')
	#---

 #--- Methods of the class
	def OnConf(self, event): 
		""" Show the configure window """

		gmethods.WinMainTypeCreate(config.winName['confSearch'])
		return True
	#---

	def OnDef(self, event):
		""" Set default values """

		#self.tcUserValue.SetValue("{2: 'A W', 3: 'S T', 4: 'I A', 'Pos': True}")
		self.tcUserValue.SetValue("{2: 'A S', 3: 'E V T Q I D S M L F R G', 4: 'P A G V C K M S R', 5: 'V I D E F G L W A Y', 'Pos': True}")
		self.cbCompProt.SetValue(True)
		return True
	#---

	def CheckInput(self):
		""" Check the input """
	
	 #--- Input file
		if self.GuiCheckInputFile(
			'iFile',
			self.tcInputFile,
			config.fatalErrorsMsg[self.nameTab]['iFile'],
		):
			pass
		else:
			return False
	 #--- Output file
		if self.GuiCheckOutFile(
			'oFile',
			self.tcOutFile,
			config.fatalErrorsMsg[self.nameTab]['oFile'],
		):
			pass
		else:
			return False
	 #--- Positions & AAs
		if self.GuiCheckPosAADict(
			'PosAA',
			'PosAAL',
			self.tcUserValue,
			config.fatalErrorsMsg[self.nameTab]['PosAA'],
		):
			pass
		else:
			return False
	 #--- CheckBox
		if self.cbCompProt.GetValue():
			self.d['CompProt'] = self.do['CompProt'] = True
		else:
			self.d['CompProt'] = self.do['CompProt'] = False			
	 #--- Return
		return True
	#---

	def DataProcessing(self):
		""" Process the data """

	 #--- Generate output data frame and fill info from the given sequences
		allAA = []
		for k, v in self.do['PosAA'].items():
			if k != config.dictKey[config.winName['confSearch']]['PosKey']:
				allAA.append(v)
			else:
				pass
		self.dataO = pd.concat([pd.DataFrame([[''.join(v), 0, 0, 0, '']], columns=config.dataFrame['Header'][self.nameTab]) for v in itertools.product(*allAA)], 
			ignore_index=True
		)
	 #--- Variables
		self.ltotal    = 0
		self.lempty    = 0
		self.prottotal = 0
		self.protsselT = 0
		searchP = False
		FFile   = open(str(self.do['iFile']), 'r')
		for line in FFile:
			self.ltotal += 1	
		 #--- To considerer mac \n or windows \r\n files
			l  = line.split('\n')[0]
			ll = l.split('\r')[0]
			ll = ll.strip()
			if ll == '':
				self.lempty += 1
			elif ll[0] == '>':
				self.prottotal += 1
				if searchP:
					tseq = ''.join(lseq)
					self.ScanDict[self.do['PosAA'][config.dictKey[config.winName['confSearch']]['PosKey']]](
						tseq, 
						tprot,
					)
				else:
					pass
			 #--- Check for sequences that are only fragments
				if 'Fragment' in ll:
					if self.do['CompProt']:
						searchP = False
					else:
						searchP = True
						self.protsselT += 1
						tprot = ll.split('|')[1]
						lseq = []						
				else:
					searchP = True
					self.protsselT += 1
					tprot = ll.split('|')[1]
					lseq = []
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
	 #--- Last pass to catch the last protein
		if searchP:
			tseq = ''.join(lseq)
			self.ScanDict[self.do['PosAA'][config.dictKey[config.winName['confSearch']]['PosKey']]](tseq, tprot)	
		else:
			pass 
	 #--- Calculate %
		self.dataO['%_AP'] = 100.0 * (self.dataO['Appearance'] / self.protsselT)
		self.dataO['%_TP'] = 100.0 * (self.dataO['Appearance'] / self.prottotal)
		self.sum = self.dataO['Appearance'].sum()
	 #--- Sort on Appearance
		self.dataO.sort_values(
			by = ['Appearance', 'Sequence'],
			ascending = [False, True],
			inplace   = True,
		)
	 #--- Return
		return True
	#---

	def ScanSeqWithPos(self, tseq, tprot):
		""" Extract AA in tseq for the given positions and compares to the seqs
			in self.dataO and update self.dataO. 
			---
			tseq : protein sequence (str)
			tprot: protein id in the multifasta file (str)
			self.dataO : pd.DataFrame with the following structure
			  Sequence Appearance %_AP %_TP Prot_IDs
			0      QRS          0    0    0       ''        
		"""

	 #--- Get sequence in the given positions
		seq = []
		for k in self.do['PosAAL']:
			try:
				seq.append(tseq[k])
			except IndexError:
				return False	
		seq = ''.join(seq)
	 #--- Filter self.dataO and get index
		dfo = self.dataO[self.dataO.loc[:,'Sequence'].str.contains(seq)]
		idx = dfo.index.values.astype(int)
		idxL = len(idx)
	 #--- Check if something was found
		if idxL > 1 or idxL == 0:
			return False
		else:
	 	 #--- Update self.dataO
			idx = idx[0]
			self.dataO.iloc[idx, 1] += 1
			if self.dataO.iloc[idx,4] == '':
				self.dataO.iloc[idx,4] = tprot
			else:
				self.dataO.iloc[idx,4] = self.dataO.iloc[idx,4] + ', ' + tprot
	 #--- Return
		return True
	#---

	def ScanSeqNoPos(self, tseq, tprot):
		""" When no positions are given consider the consensus sequence as 
			continuous and then just try to find each consensus sequence in tseq
			at least one time
			---
			tseq : protein sequence (str)
			tprot: protein id in the multifasta file (str)
			self.dataO : pd.DataFrame with the following structure
			  Sequence Appearance %_AP %_TP Prot_IDs
			0      QRS          0    0    0 ''        
		"""

		self.dataO[['Appearance', 'Prot_IDs']] = self.dataO.apply(
			self.ScanSeqNoPosLookSeq,
			axis=1,
			args=(tseq, tprot),
			raw=True,
		)
		return True
	#---

	def ScanSeqNoPosLookSeq(self, row, tseq, tprot):
		""" Search the seq in row in tseq and update columns in self.dataO 
			---
			row  : numpy rray from pd.row
			tseq : protein sequence (str)
			tprot: protein id (str)
		"""

		if row[0] in tseq:
			a = row[1] + 1
			if row[4] == '':
				myID = tprot
			else:
				myID = row[4] + ', ' + tprot
			return pd.Series([a, myID])
		else:
			return pd.Series([row[1], row[4]])
	#---

	def WriteOutput(self):
		""" Write the output """

	 #--- Check there is something to write	
		if self.sum == 0:
			MyWarningMessageOK(config.fatalErrorsMsg[self.nameTab]['NoSeq'])
			return False
		else:
		 #--- Write input data
			oFile = open(str(self.do['oFile']), 'w')
			oFile.write('Input data:\n')
			dmethods.FFsWriteDict(oFile, self.d, config.helperDict[self.nameTab])
			oFile.write('\n')
		 #--- Write output
			oFile.write('Output data:\n')
			oFile.write('Total proteins:\t' + str(self.prottotal) + '\n')
			oFile.write('Total analyzed proteins:\t' + str(self.protsselT) + '\n')
			oFile.write('Total consensus sequence (Absolute):\t' + str(self.sum) + '\n')
			oFile.write('Total consensus sequence (Percent, TP):\t' + str(self.sum * 100.0 / self.prottotal) + '\n')
			oFile.write('Total consensus sequence (Percent, AP):\t' + str(self.sum * 100.0 / self.protsselT) + '\n')
			oFile.write('\n')
			dmethods.FFsWriteCSV(oFile, self.dataO)
			oFile.write('\n\n')
		 #--- File last line
			dmethods.FFsWriteLastLine(oFile)
		 #--- Close file and final summary in statusbar
			oFile.close()
			self.statusbar.SetStatusText(
				'All done!!! Consensus sequences found:  ' 
				+ str(self.sum) 
				+ ',  Empty Lines Found:  ' 
				+ str(self.lempty) 
				+ ',  Total Analyzed Lines:  ' 
				+ str(self.ltotal)
			)
		return True
	#---
#---




