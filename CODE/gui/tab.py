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
import ast
import itertools
from operator import itemgetter

import wx
import wx.lib.agw.aui as aui

import dat4s_core.data.filefolder as dtsFF
import dat4s_core.data.string as dtsStr
import dat4s_core.validator.validator as dtsValidator
import dat4s_core.widget.wx_widget as dtsWidget
import dat4s_core.widget.wx_window as dtsWindow

import config.config as config
import gui.pane as pstPane
import gui.widget as pstWidget
import gui.window as pstWindow
#endregion ----------------------------------------------------------- Imports



#region -------------------------------------------------------------> Classes
class ConsensusTab(wx.Panel, pstWidget.UserInput):
	"""Tab to search consensus sequence in peptides
	
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
		parent : wx widget or None
			Parent of the tab
		name : str
			To id the tab and its elements
	"""
	#region --------------------------------------------------> Instance setup
	def __init__(self, parent, name, statusbar):
		""""""
		#region -----------------------------------------------> Initial setup
		self.parent = parent
		self.name   = name
		
		wx.Panel.__init__(self, parent, name=name)
		pstWidget.UserInput.__init__(self, self)
		#endregion --------------------------------------------> Initial setup

		#region -----------------------------------------------------> Widgets
		#--> Statusbar
		self.statusbar = statusbar
		#--> wx.Button & wx.TextCtrl
		self.fastaFile = dtsWidget.ButtonTextCtrlFF(
			self.sbFile,
			btnLabel  = config.label[name]['FastaFile'],
			tcHint    = config.hint[name]['FastaFile'],
			ext       = config.extLong['Seq'],
			validator = dtsValidator.IsNotEmpty(
				parent,
				config.msg['Error'][name]['FastaFile'],
			),
		)
		self.outFile = dtsWidget.ButtonTextCtrlFF(
			self.sbFile,
			btnLabel  = config.label[name]['OutFile'],
			tcHint    = config.hint[name]['OutFile'],
			ext       = config.extLong['Data'],
			mode      = 'save',
			validator = dtsValidator.IsNotEmpty(
				parent,
				config.msg['Error'][name]['OutFile'],
			),
		)
		self.posAA = dtsWidget.ButtonTextCtrl(
			self.sbValue,
			btnLabel  = config.label[name]['PosAA'],
			tcHint    = config.hint[name]['PosAA'],
			validator = dtsValidator.IsNotEmpty(
				parent,
				config.msg['Error'][name]['PosAA'],
			),
		)
		#--> CheckBox
		self.cbCompProt = wx.CheckBox(
			self.sbValue,
			label = config.label[name]['CompProt'],
		)
		#endregion --------------------------------------------------> Widgets

		#region ------------------------------------------------------> Sizers
		#--> wx.StaticBox File
		self.sizersbFileWid.Add(
			self.fastaFile.btn,
			border = 5,
			flag   = wx.ALIGN_CENTER_VERTICAL|wx.EXPAND|wx.ALL,
		)
		self.sizersbFileWid.Add(
			self.fastaFile.tc,
			border = 5,
			flag   = wx.ALIGN_CENTER_VERTICAL|wx.EXPAND|wx.ALL,
		)
		self.sizersbFileWid.Add(
			self.outFile.btn,
			border = 5,
			flag   = wx.ALIGN_CENTER_VERTICAL|wx.EXPAND|wx.ALL,
		)
		self.sizersbFileWid.Add(
			self.outFile.tc,
			border = 5,
			flag   = wx.EXPAND|wx.ALL,
		)
		#--> wx.StaticBox Value
		self.sizersbValue.Remove(self.sizersbValueWid) # Nedd GridBag instead of FlexGrid
		self.sizersbValueWid = wx.GridBagSizer(1, 1)
		self.sizersbValue.Add(
			self.sizersbValueWid,
			border = 2,
			flag   = wx.EXPAND|wx.ALL
		)
		self.sizersbValueWid.Add(
			self.posAA.btn,
			pos    = (0,0),
			border = 5,
			flag   = wx.ALIGN_CENTER_VERTICAL|wx.EXPAND|wx.ALL,
		)
		self.sizersbValueWid.Add(
			self.posAA.tc,
			pos    = (0,1),
			border = 5,
			flag   = wx.EXPAND|wx.ALL,
		)
		self.sizersbValueWid.Add(
			self.cbCompProt,
			pos    = (1,0),
			border = 5,
			span   = (0,2),
			flag   = wx.EXPAND|wx.ALL,
		)
		self.sizersbValueWid.AddGrowableCol(1, 1)
		#--> wx.StaticBox Column
		self.sizersbColumn.ShowItems(False)
		#--> Main Sizer
		self.Sizer = wx.GridBagSizer(1, 1)
		self.Sizer.Add(
			self.sizersbFile,
			pos    = (0,0),
			flag   = wx.EXPAND|wx.ALL,
			border = 5
		)
		self.Sizer.Add(
			self.sizersbValue,
			pos    = (1,0),
			flag   = wx.EXPAND|wx.ALL,
			border = 5
		)
		self.Sizer.Add(
			self.btnGroup.Sizer,
			pos    = (2,0),
			flag   = wx.ALIGN_CENTER|wx.ALL,
			border = 5
		)
		self.Sizer.AddGrowableCol(0, 1)
		self.SetSizer(self.Sizer)
		self.Sizer.Fit(self)
		#endregion ---------------------------------------------------> Sizers

		#region --------------------------------------------------------> Bind
		self.posAA.btn.Bind(wx.EVT_BUTTON, self.OnPosAA)
		#endregion -----------------------------------------------------> Bind

		#region ----------------------------> Test & Default production values
		if config.development:
			self.fastaFile.tc.SetValue("/Users/bravo/Dropbox/SOFTWARE-DEVELOPMENT/APPS/PEPTIDE_SEARCH_TOOLS/LOCAL/DATA/NEW-DATA/HUMAN_ref_Jan2019-cut-long.fasta")
			self.outFile.tc.SetValue("/Users/bravo/TEMP-GUI/BORRAR-PeptideSearchTools/consensus-out.txt")
			self.posAA.tc.SetValue("{2: 'A W', 3: 'S T', 4: 'I A', 'Pos': True}")
		else:
			pass
		#endregion -------------------------> Test & Default production values
	#---
	#endregion -----------------------------------------------> Instance setup

	#region ---------------------------------------------------> Class methods
	def OnPosAA(self, event):
		"""Launch the configuration window to set the postions and the AAs

			Parameters
			----------
			event : wx.Event
				Information about the event
		"""
		with pstWindow.ConsensusConf(self, 'ConsensusConf') as dlg:
			if dlg.ShowModal() == wx.ID_OK:
				dlg.OnExport(self.posAA.tc)
			else:
				pass
	#---

	def CheckInput(self):
		"""Check user input"""
		#region ---------------------------------------------------------> Msg
		msgM = config.msg['Step']['Check']
		#endregion ------------------------------------------------------> Msg
		
		#region -------------------------------------------> Individual Fields
		msg = f"{msgM}: {config.label[self.name]['FastaFile']}"
		wx.CallAfter(dtsWidget.StatusBarUpdate, self.statusbar, msg)
		if self.fastaFile.tc.GetValidator().Validate(self):
			pass
		else:
			return False
		
		msg = f"{msgM}: {config.label[self.name]['OutFile']}"
		wx.CallAfter(dtsWidget.StatusBarUpdate, self.statusbar, msg)
		if self.outFile.tc.GetValidator().Validate(self):
			pass
		else:
			return False

		msg = f"{msgM}: {config.label[self.name]['PosAA']}"
		wx.CallAfter(dtsWidget.StatusBarUpdate, self.statusbar, msg)
		if self.posAA.tc.GetValidator().Validate(self):
			pass
		else:
			return False
		#endregion ----------------------------------------> Individual Fields
		
		return True
	#---

	def PrepareRun(self):
		"""Prepare the run """
		#region ---------------------------------------------------------> Msg
		msg = config.msg['Step']['Prepare']
		wx.CallAfter(dtsWidget.StatusBarUpdate, self.statusbar, msg)
		#endregion ------------------------------------------------------> Msg

		#region -----------------------------------------------------> Prepare
		#--> Input
		self.iFile    = self.fastaFile.tc.GetValue()
		self.oFile    = self.outFile.tc.GetValue()
		self.posAAVal = ast.literal_eval(self.posAA.tc.GetValue())
		self.full     = self.cbCompProt.GetValue()
		#--> Output
		self.d = {
			config.label[self.name]['FastaFile']: self.iFile,
			config.label[self.name]['OutFile'] : self.oFile,
			config.label[self.name]['PosAA']   : self.posAA.tc.GetValue(),
			config.label[self.name]['CompProt']: self.full,
		}
		#--> Needed variables
		self.ltotal    = 0
		self.lempty    = 0
		self.prottotal = 0
		self.protsselT = 0
		self.protfrag  = 0
		#-> Signal if conSeq must be search in protSeq
		self.searchP   = False 
		#-> Value of Pos key to avoid using the printed name and config....
		self.Pos = self.posAAVal[config.dictKey[self.name]['PosKey']]
		#-> List of residues in which to look for the conSeq or None 
		self.resID = [k for k in self.posAAVal.keys()][0:-1] if self.Pos else None
		#-> List of possible AA in each position [['A', 'C'], ['K', 'R'] ...]
		self.allAA = [x.split() for x in self.posAAVal.values() if type(x) == str]
		#-> Count the appearances of conSeqs in the fasta proteins
		self.seqProt = {} # = {'SeqA' : {Count: 0, PerCent: 0, pID: ''},}
		for v in itertools.product(*self.allAA):
			self.seqProt["".join(v)] = {'Count':0, 'PerCent':0, 'pID':''}
		#-> Count the appearances of conSeqs in the fasta protein if the 
		#-> search is done in the entire protein sequence
		self.protSeq = {} # {ProtID: [SeqA, SeqB], .....}
		#-> To check there is something to write to the output
		self.countTotal = 0
		#endregion --------------------------------------------------> Prepare

		return True
	#---

	def RunAnalysis(self):
		""" Process the data """
		#region ---------------------------------------------------------> Msg
		msg = config.msg['Step']['Run']
		wx.CallAfter(dtsWidget.StatusBarUpdate, self.statusbar, msg)
		#endregion ------------------------------------------------------> Msg

		#region -----------------------------------------------------> Process
		#--> Read and search file
		with open(self.iFile, 'r') as iFile:
			for line in iFile:
				self.ltotal += 1
				#--> Remove new line characters and strip line
				l = dtsStr.Str2List(line, strip='b')[0]
				#--> Discard empty lines
				if l == '':
					self.lempty += 1
				#--> Process start of new protein in fasta file
				elif l[0] == '>':
					self.prottotal += 1
					#--> Search conSeq in the sequence of the previous protein
					if self.searchP:
						tseq = ''.join(lseq)
						self.SearchConsensusSeq(tseq, tprot)
					else:
						pass
				 	#--> Setup analysis for this protein
					if 'Fragment' in l:
						self.protfrag += 1
						if self.full:
							self.searchP = False
						else:
							self.searchP    = True
							self.protsselT += 1
							tprot = l.split('|')[1]
							lseq  = []
					else:
						self.searchP    = True
						self.protsselT += 1
						tprot = l.split('|')[1]
						lseq  = []
				#--> Proccess sequence line in fasta file
				else:
					if self.searchP:
						lseq.append(l)
					else:
						pass
				#--> Update GUI
				if self.ltotal % 100 == 0:
					msg = (f"Analysing --> Total lines: {self.ltotal}, "
						f"Empty lines: {self.lempty}, "
						f"Total proteins: {self.prottotal}, "
						f"Matched proteins: {len(self.protSeq)}"
					)
					wx.CallAfter(dtsWidget.StatusBarUpdate, self.statusbar, msg)
				else:
					pass
		#--> Last past to catch the last protein
		if self.searchP:
			tseq = ''.join(lseq)
			self.SearchConsensusSeq(tseq, tprot)
		else:
			pass 
		#--> Calculate %
		for k in self.seqProt.keys():
			self.countTotal += self.seqProt[k]['Count']
			self.seqProt[k]['PerCent'] = (
				f"{(100 * self.seqProt[k]['Count'] / self.protsselT):.2f}"
			)
		#--> Sort results
		if self.countTotal == 0:
			pass
		else:
			self.seqProt = {
				k: self.seqProt[k] 
				for k in sorted(
					self.seqProt, 
					key     = lambda x: self.seqProt[x]['Count'],
					reverse = True,
				)
			}
			self.protSeq = {
				k: self.protSeq[k]
				for k in sorted(
					self.protSeq,
					key = lambda x: x,
				)
			}
		#endregion --------------------------------------------------> Process

		return True
	#---

	def SearchConsensusSeq(self, protSeq, protID):
		"""Identify if the consensus sequences appear in the sequence of a 
			proteins & updates the self.seqProt and self.protSeq dict

			Parameters
			----------
			protSeq : str
				Sequence of the protein as str
			protID : str
				Protein ID
		"""
		#region -------------------------> Get sequence in the given positions
		if self.Pos:
			try:
				seq = "".join([protSeq[x-1] for x in self.resID])
			except IndexError:
				return False
		else:
			seq = protSeq
		#endregion ----------------------> Get sequence in the given positions

		#region ------------------------------------------------------> Update
		for k in self.seqProt.keys():
			if k in seq:
				#--> Update self.seqProt
				self.seqProt[k]['Count'] += 1
				self.seqProt[k]['pID'] += protID+', '
				#--> Update self.protSeq
				if protID in self.protSeq:
					self.protSeq[protID] += k+', '
				else:
					self.protSeq[protID] = k+', '
			else:
				pass
		#endregion ---------------------------------------------------> Update

		return True
	#---

	def WriteOutput(self):
		""""""
		#region ---------------------------------------------------------> Msg
		msg = config.msg['Step']['Output']
		wx.CallAfter(dtsWidget.StatusBarUpdate, self.statusbar, msg)
		#endregion ------------------------------------------------------> Msg

		#region ---------------------------> Check there is something to write	
		if self.countTotal == 0:
			msg = config.msg['Error'][self.name]['NoConsensusFound']
			dtsWindow.MessageDialog('errorF', msg, self)
			return False
		else:
			pass
		#endregion ------------------------> Check there is something to write	

		#region -------------------------------------------------------> Write
		#--> Write input data
		oFile = open(self.oFile, 'w')
		oFile.write('Input data:\n')
		dtsFF.WriteDict2File(oFile, self.d)
		oFile.write('\n')
		#---
		#--> Write output
		oFile.write('Output data:\n')
		oFile.write(f"Total proteins\t{self.prottotal}\n")
		oFile.write(f"Complete proteins\t{self.prottotal-self.protfrag}\n")
		oFile.write(f"Fragment proteins\t{self.protfrag}\n")
		oFile.write(f"Consensus sequence in proteins\t{len(self.protSeq)}\n")

		header = f'\nCount\tSequence\tPercent\tProtein IDs'
		oFile.write(header+'\n')
		for k,v in self.seqProt.items():
			oFile.write(f"{v['Count']}\t{k}\t{v['PerCent']}\t{v['pID'][0:-2]}\n")

		if not self.Pos:
			oFile.write(f"\nProtein IDs\tSequences\n")
			for k, v in self.protSeq.items():
				oFile.write(f"{k}\t{v[0:-2]}\n")
			oFile.write("\n")
		else:
			pass
		#---
		#--> File last line
		if self.Pos:
			oFile.write("\n")
		else:
			pass
		dtsFF.WriteLastLine2File(oFile, config.title['MainW'])
		#---
	 	#--> Close file and final summary in statusbar
		oFile.close()
		msg = (
			f"Analysing --> Total lines: {self.ltotal}, "
			f"Empty lines: {self.lempty}, "
			f"Total proteins: {self.prottotal}, "
			f"Matched proteins: {len(self.protSeq)}"
		)
		wx.CallAfter(dtsWidget.StatusBarUpdate, self.statusbar, msg)
		#---
		#endregion ----------------------------------------------------> Write

		return True
	#---
	#endregion ------------------------------------------------> Class methods
#---

class GeneTab(wx.Panel, pstWidget.UserInput):
	"""Tab for the gene search
	
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
		parent : wx widget or None
			Parent of the tab
		name : str
			To identify the tab
	"""
	#region --------------------------------------------------> Instance setup
	def __init__(self, parent, name, statusbar):
		""""""
		#region -----------------------------------------------> Initial setup
		self.parent = parent
		self.name   = name

		wx.Panel.__init__(self, parent, name=name)
		pstWidget.UserInput.__init__(self, self)
		#endregion --------------------------------------------> Initial setup

		#region -----------------------------------------------------> Widgets
		#--> Statusbar
		self.statusbar = statusbar
		#--> wx.Button & wx.TextCtrl
		self.fastaFile = dtsWidget.ButtonTextCtrlFF(
			self.sbFile,
			btnLabel  = config.label[name]['FastaFile'],
			tcHint    = config.hint[name]['FastaFile'],
			ext       = config.extLong['Seq'],
			validator = dtsValidator.IsNotEmpty(
				parent,
				config.msg['Error'][name]['FastaFile'],
			),
		)
		self.geneFile = dtsWidget.ButtonTextCtrlFF(
			self.sbFile,
			btnLabel  = config.label[name]['GeneFile'],
			tcHint    = config.hint[name]['GeneFile'],
			ext       = config.extLong['Data'],
			validator = dtsValidator.IsNotEmpty(
				parent,
				config.msg['Error'][name]['GeneFile'],
			),
		)		
		self.outFile = dtsWidget.ButtonTextCtrlFF(
			self.sbFile,
			btnLabel  = config.label[name]['OutFile'],
			tcHint    = config.hint[name]['OutFile'],
			ext       = config.extLong['Data'],
			mode      = 'save',
			validator = dtsValidator.IsNotEmpty(
				parent,
				config.msg['Error'][name]['OutFile'],
			),
		)
		#--> wx.StaticText & wx.TextCtrl
		self.residueExtract = dtsWidget.StaticTextCtrl(
			self.sbValue,
			stLabel   = config.label[name]['ResidueExtract'],
			tcHint    = config.hint[name]['ResidueExtract'],
			validator = dtsValidator.NumberList(
				parent,
				config.msg['Error'][name]['ResidueExtract'],
				isList = True,
				refMin = 1,

			),
		)
		#endregion --------------------------------------------------> Widgets

		#region ------------------------------------------------------> Sizers
		#--> wx.StaticBox File
		self.sizersbFileWid.Add(
			self.fastaFile.btn,
			border = 5,
			flag   = wx.ALIGN_CENTER_VERTICAL|wx.EXPAND|wx.ALL,
		)
		self.sizersbFileWid.Add(
			self.fastaFile.tc,
			border = 5,
			flag   = wx.EXPAND|wx.ALL,
		)
		self.sizersbFileWid.Add(
			self.geneFile.btn,
			border = 5,
			flag   = wx.ALIGN_CENTER_VERTICAL|wx.EXPAND|wx.ALL,
		)
		self.sizersbFileWid.Add(
			self.geneFile.tc,
			border = 5,
			flag   = wx.EXPAND|wx.ALL,
		)
		self.sizersbFileWid.Add(
			self.outFile.btn,
			border = 5,
			flag   = wx.ALIGN_CENTER_VERTICAL|wx.EXPAND|wx.ALL,
		)
		self.sizersbFileWid.Add(
			self.outFile.tc,
			border = 5,
			flag   = wx.EXPAND|wx.ALL,
		)
		#--> wx.StaticBox Value
		self.sizersbValueWid.Add(
			self.residueExtract.st,
			border = 5,
			flag   = wx.ALIGN_CENTER_VERTICAL|wx.EXPAND|wx.ALL,
		)
		self.sizersbValueWid.Add(
			self.residueExtract.tc,
			border = 5,
			flag   = wx.EXPAND|wx.ALL,
		)
		#--> wx.StaticBox Column
		self.sizersbColumn.ShowItems(False)
		#--> Main Sizer
		self.Sizer = wx.GridBagSizer(1, 1)
		self.Sizer.Add(
			self.sizersbFile,
			pos    = (0,0),
			flag   = wx.EXPAND|wx.ALL,
			border = 5
		)
		self.Sizer.Add(
			self.sizersbValue,
			pos    = (1,0),
			flag   = wx.EXPAND|wx.ALL,
			border = 5
		)
		self.Sizer.Add(
			self.btnGroup.Sizer,
			pos    = (2,0),
			flag   = wx.ALIGN_CENTER|wx.ALL,
			border = 5
		)
		self.Sizer.AddGrowableCol(0, 1)
		self.SetSizer(self.Sizer)
		self.Sizer.Fit(self)
		#endregion ---------------------------------------------------> Sizers

		#region ----------------------------> Test & Default production values
		if config.development:
			self.fastaFile.tc.SetValue("/Users/bravo/Dropbox/SOFTWARE-DEVELOPMENT/APPS/PEPTIDE_SEARCH_TOOLS/LOCAL/DATA/NEW-DATA/HUMAN_ref_Jan2019.fasta")
			self.geneFile.tc.SetValue("/Users/bravo/Dropbox/SOFTWARE-DEVELOPMENT/APPS/PEPTIDE_SEARCH_TOOLS/LOCAL/DATA/NEW-DATA/XIAP_GeneNAMES.txt")
			self.outFile.tc.SetValue("/Users/bravo/TEMP-GUI/BORRAR-PeptideSearchTools/gene-out.txt")
			self.residueExtract.tc.SetValue("5 10 20 50")
		else:
			pass
		#endregion -------------------------> Test & Default production values
	#---
	#endregion -----------------------------------------------> Instance setup

	#region ---------------------------------------------------> Class methods
	def CheckInput(self):
		"""Chek user input. Overrides BaseTab.CheckInput"""
		#region ---------------------------------------------------------> Msg
		msgM = config.msg['Step']['Check']
		#endregion ------------------------------------------------------> Msg
		
		#region -------------------------------------------> Individual Fields
		msg = f"{msgM}: {config.label[self.name]['FastaFile']}"
		wx.CallAfter(dtsWidget.StatusBarUpdate, self.statusbar, msg)
		if self.fastaFile.tc.GetValidator().Validate(self):
			pass
		else:
			return False

		msg = f"{msgM}: {config.label[self.name]['GeneFile']}"
		wx.CallAfter(dtsWidget.StatusBarUpdate, self.statusbar, msg)
		if self.geneFile.tc.GetValidator().Validate(self):
			pass
		else:
			return False

		msg = f"{msgM}: {config.label[self.name]['OutFile']}"
		wx.CallAfter(dtsWidget.StatusBarUpdate, self.statusbar, msg)
		if self.outFile.tc.GetValidator().Validate(self):
			pass
		else:
			return False

		msg = f"{msgM}: {config.label[self.name]['ResidueExtract']}"
		wx.CallAfter(dtsWidget.StatusBarUpdate, self.statusbar, msg)
		if self.residueExtract.tc.GetValidator().Validate(self):
			pass
		else:
			return False
		#endregion ----------------------------------------> Individual Fields

		#region ------------------------------------------------> File content
		#--> Gene names
		self.gFile    = self.geneFile.tc.GetValue()
		self.geneList = []
		with open(self.gFile, 'r') as gFile:
			for line in gFile:
				g = "".join(line.split())
				g = g.replace('"', "")
				if g == '':
					continue
				else:
					pass
				self.geneList.append(g)
				if ";" in g:
					[self.geneList.append(x) for x in g.split(";")]
				else:
					pass
		if not self.geneList:
			msg = config.error[self.name]['NoGene']
			dtsWindow.MessageDialog('errorF', msg, parent=self.parent)
			return False
		else:
			pass
		#---
		#endregion ---------------------------------------------> File content

		return True
	#---

	def PrepareRun(self):
		"""Prepare the run """
		#region ---------------------------------------------------------> Msg
		msg = config.msg['Step']['Prepare']
		wx.CallAfter(dtsWidget.StatusBarUpdate, self.statusbar, msg)
		#endregion ------------------------------------------------------> Msg

		#region -----------------------------------------------------> Prepare
		# Gene associated variables set in CheckInput since it is necesary to 
		# Check Gene file content
		#--> Input values
		self.fFile  = self.fastaFile.tc.GetValue()
		self.oFile  = self.outFile.tc.GetValue()
		self.resExt = list(
			map(
				int, 
				self.residueExtract.tc.GetValue().split()
			)
		)
		resExtStr = " ".join(self.residueExtract.tc.GetValue().split())
		#---
		#--> For output
		self.d = {
			config.label[self.name]['FastaFile']     : self.fFile,
			config.label[self.name]['GeneFile']      : self.gFile,
			config.label[self.name]['OutFile']       : self.oFile,
			config.label[self.name]['ResidueExtract']: resExtStr,
		}
		#---
		#--> Needed for the analysis
		self.ltotal    = 0
		self.lempty    = 0
		self.prottotal = 0
		self.protsselT = 0
		self.searchP   = False
		self.dataO     = []
		#---
		#endregion --------------------------------------------------> Prepare
		
		return True
	#---

	def RunAnalysis(self):
		"""Run the analysis"""
		#region ---------------------------------------------------------> Msg
		msg = config.msg['Step']['Run']
		wx.CallAfter(dtsWidget.StatusBarUpdate, self.statusbar, msg)
		#endregion ------------------------------------------------------> Msg

		#region -----------------------------------------------------> Process
		with open(self.fFile, 'r') as File:
			for line in File:
				self.ltotal += 1
				#--> Remove new line characters and strip line
				l = dtsStr.Str2List(line, strip='b')[0]
				#--> Discard empty lines
				if l == '':
					self.lempty += 1
				#--> Process line containing a fasta header
				elif l[0] == '>':
					self.prottotal += 1
					#--> Finish processing of previous sequence
					if self.searchP:
						lseq = ''.join(lseq)
						for i in self.resExt:
							ltemp.append(lseq[0:i])
						self.dataO.append(ltemp)
					else:
						pass
					#--> Setup analysis of a new protein
					if 'GN=' in l:
						tGene = [s for s in l.split() if 'GN=' in s][0].split('=')[1]
						if tGene in self.geneList:
							self.searchP = True
							self.protsselT += 1
							ltemp = []
							lseq = []
							ltemp.append(tGene)
							ltemp.append(l.split('|')[1])
						else:
							self.searchP = False
					else:
						self.searchP = False
				#--> Process line containing a sequence line
				else:
					if self.searchP:
						lseq.append(l)
					else:
						pass
				#--> Update statusbar
				if not self.ltotal % 100:
					msg = (
						f"Analysing --> Total lines: {self.ltotal}, "
						f"Empty lines: {self.lempty}, "
						f"Total Proteins: {self.prottotal}, "
						f"Matched Proteins:  {self.protsselT}"
					)
					wx.CallAfter(dtsWidget.StatusBarUpdate, self.statusbar, msg)
				else:
					pass
		#--> Last pass to catch the last protein
		if self.searchP:
			lseq = ''.join(lseq)
			for i in self.resExt:
				ltemp.append(lseq[0:i])
			self.dataO.append(ltemp)
		else:
			pass
		#---
		#endregion --------------------------------------------------> Process

		return True
	#---

	def WriteOutput(self):
		""" Write the output """
		#region ---------------------------------------------------------> Msg
		msg = config.msg['Step']['Output']
		wx.CallAfter(dtsWidget.StatusBarUpdate, self.statusbar, msg)
		#endregion ------------------------------------------------------> Msg

		#region ---------------------------> Check there is something to write	
		if self.protsselT == 0:
			msg = config.msg['Error'][self.name]['NoProtFound']
			dtsWindow.MessageDialog('errorF', msg, self)
			return False
		else:
			pass
		#endregion ------------------------> Check there is something to write	

		#region -------------------------------------------------------> Write
		#--> Write input data
		oFile = open(self.oFile, 'w')
		oFile.write('Input data:\n')
		dtsFF.WriteDict2File(oFile, self.d)
		oFile.write('\n')
		#---
		#--> Write output
		oFile.write('Output data:\n')
		header = 'Gene\tProtein\t' + "\t".join(['1-'+str(x) for x in self.resExt])
		oFile.write(header+'\n')

		self.dataO.sort(key=itemgetter(0, 1))
		dtsFF.WriteList2File(oFile, self.dataO)
		oFile.write('\n')
		#---
		#--> File last line
		dtsFF.WriteLastLine2File(oFile, config.title['MainW'])
		#---
	 	#--> Close file and final summary in statusbar
		oFile.close()
		msg = (
			f"Final count --> Total lines: {self.ltotal}, "
			f"Empty lines: {self.lempty}, "
			f"Total Proteins: {self.prottotal}, "
			f"Matched Proteins:  {self.protsselT}"
		)
		wx.CallAfter(dtsWidget.StatusBarUpdate, self.statusbar, msg)
		#---
		#endregion ----------------------------------------------------> Write

		return True
	#---
	#endregion ------------------------------------------------> Class methods
#---

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
		parent : wx widget or None
			Parent of the tab
		name : str
			To identify the tab
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
		self.parent = parent
		self.name   = name
		
		super().__init__(parent, name=name)
		#endregion --------------------------------------------> Initial setup
		
		#region -----------------------------------------------------> Widgets
		self.lc = dtsWidget.ListZebra(
			self, 
			colLabel = config.label[name]['Column'],
			colSize = config.size['ListCtrl']['Peptide'],
		)
		self.userInput = pstPane.PeptidePane(self, name, statusbar, lc=self.lc)
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