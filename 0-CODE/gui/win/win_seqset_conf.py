# ------------------------------------------------------------------------------
# 	Copyright (C) 2019-2020 Kenny Bravo Rodriguez

# 	This program is distributed for free in the hope that it will be useful,
# 	but WITHOUT ANY WARRANTY; without even the implied warranty of
# 	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

# 	See the accompaning licence for more details.
# ------------------------------------------------------------------------------

""" This module contain the class to configure the consensus search tab """

#--- Imports
## Standard modules
import wx
import ast 
## My modules
import config.config as config
from gui.win.win_base import BaseWin
from gui.win.win_supp import GuiCheck
#---

class ConsensusSearchConfig(BaseWin, GuiCheck):
	""" Configure window for searching in Consensus Tab  """

	def __init__(self):
		""" """
	 
	 #--- Initial Setup
		self.nameWin = config.winName['confSearch']
		self.parentW = config.win[config.winName['main']]
		super().__init__(config.win[config.winName['main']])
	 #--- Widgets
	  #--> ScrolledWindow
		self.swMatrix = wx.ScrolledWindow(
			self.winPanel, 
			size=config.size['ScrolledW'][self.nameWin],
		)
		self.swMatrix.SetBackgroundColour('WHITE')	 
	  #--> TextCtrl
		self.tcNRes = wx.TextCtrl(
			self.winPanel, 
			value = '',
			size  = config.size['TextCtrl'][self.nameWin]['NRes'],
			style = wx.TE_CENTRE,
		)
	  #--- StaticText
		self.stNRes = wx.StaticText(
			self.winPanel, 
			label='Number of residues:',
		)	
	  #--- Buttons
		self.buttonCreate = wx.Button(self.winPanel, label='Create matrix')
		self.buttonCancel = wx.Button(self.winPanel, label='Cancel')
		self.buttonOk     = wx.Button(self.winPanel, label='Ok')
	 #--- Sizers
	  #--- Add new elements
	   #--- Number of residue
		self.sizerNRes = wx.FlexGridSizer(1,3,1,1)
		self.sizerNRes.Add(
			self.stNRes,
			flag=wx.ALIGN_CENTER_VERTICAL|wx.ALL,
			border=5,
		)
		self.sizerNRes.Add(
			self.tcNRes,
			flag=wx.EXPAND|wx.ALL,
			border=5,
		)
		self.sizerNRes.Add(
			self.buttonCreate,
			flag=wx.ALIGN_CENTER|wx.ALL,
			border=5,
		)
	   #--- Cancel Ok buttons
		self.sizerButtons = wx.FlexGridSizer(1,2,1,1)
		self.sizerButtons.Add(
			self.buttonCancel,
			flag=wx.ALIGN_CENTER|wx.ALL,
			border=5,
		)
		self.sizerButtons.Add(
			self.buttonOk,
			flag=wx.ALIGN_CENTER|wx.ALL,
			border=5,
		)
	   #--- Scrolled Window
		self.sizerSW = wx.FlexGridSizer(1,3,1,1)
		self.swMatrix.SetSizer(self.sizerSW)
	  #--- Add to main sizer
		self.sizer.Add(
			self.sizerNRes,
			pos=(0,0),
			flag=wx.ALIGN_CENTER|wx.ALL,
			border=5,
			span=(0,3),
		)
		self.sizer.Add(
			self.swMatrix,
			pos=(1,0),
			flag=wx.EXPAND|wx.ALL,
			border=5,
			span=(0,3),
		)
		self.sizer.Add(
			self.sizerButtons,
			pos=(2,2),
			flag=wx.ALIGN_RIGHT|wx.ALL,
			border=5,
		)
		self.sizerSW.Fit(self.swMatrix)
		self.sizer.Fit(self.winPanel)
	 #--- Bind
		self.buttonCancel.Bind(wx.EVT_BUTTON, self.OnCancel)
		self.buttonCreate.Bind(wx.EVT_BUTTON, self.OnCreate)
		self.buttonOk.Bind(wx.EVT_BUTTON, self.OnOk)
	 #--- If there is something in the parent window try to read and use it
		self.InitVal()
	 #--- Show
		self.Show()
	#---
 	
	#--- Methods of the class
	def InitVal(self):
		""" Try to read and use initial values in parent wx.TextCtrl """
	 #--- Get value
		myString = self.parentW.pageC.tcUserValue.GetValue()
		if myString == '':
			return False
		else:
			myDict = ast.literal_eval(myString)
			if isinstance(myDict, dict):
				NRow = len(myDict) - 1
				self.tcNRes.SetValue(str(NRow))
				self.OnCreate('event')
				Pos = myDict[config.dictKey[self.nameWin]['PosKey']]
				for i, (k, v) in enumerate(myDict.items(), start=1):
					if k != config.dictKey[self.nameWin]['PosKey']:
						self.tcAAList[i].SetValue(v)
						if Pos:
							self.tcPosList[i].SetValue(str(k))
						else:
							pass
				return True
			else:
				return False	 
	#---

	def OnCancel(self, event):
		""" Just close the window """  
		self.Close()
		return True
	#---

	def OnOk(self, event):
		""" Export the typed results to the Consensus tab in the main window """
	
	 #--- Check that some matrix was formed.
		try:
			self.do['TRow']
		except AttributeError:
			self.Close()
			return False
	 #--- Variables
		myDict = {}
		Pos = True
		for k, v in enumerate(self.tcPosList):
			if k != 0:
				tKey = v.GetValue() 
				if tKey == '':
					myDict[k] = self.tcAAList[k].GetValue().upper()
					Pos = False
				else:
					myDict[tKey] = self.tcAAList[k].GetValue().upper()
			else:
				pass
		myDict[config.dictKey[self.nameWin]['PosKey']] = Pos
	 #--- Export
		self.parentW.pageC.tcUserValue.SetValue(str(myDict))
	 #--- Close the window
		self.Close()
	 #--- Return
		return True
	#---

	def OnCreate(self, event):
		""" Create the extra widgets needed to fill the scrolled window based
			on the requested number of residues in the consensus sequence
		"""
	 #--- Variables
	  #--- Needed to use GuiCheck
		self.d = {}
		self.do = {}
	 #--- Check residue number
		if self.GuiCheckInteger(
			'NRes',
			self.tcNRes,
			config.fatalErrorsMsg[self.nameWin]['NRes']
		):
			pass
		else:
			return False
	 #--- Variables, here to avoid this if no NRes
		self.do['TRow'] = self.do['NRes'] + 1
		self.tcAAList   = []
		self.tcPosList  = []
		self.stPosList  = []
	 #--- Modify self.sizerSWContent
		self.sizerSW.SetRows(self.do['TRow'])
	 #--- Clean previous input
		self.sizerSW.Clear(delete_windows=True)	
	 #--- Create and show new windows
		self.CreateShowWidgets(self.do['NRes'])
		return True
	#---

	def CreateShowWidgets(self, NRow):
		""" Create the widgets and place them in the sizer """
	 #--- Create the header
		self.stPosList.append(wx.StaticText(
			self.swMatrix,
			label='Position',
			)
		)
		self.tcPosList.append(wx.StaticText(
			self.swMatrix,
			label='Residue number',
			)
		)
		self.tcAAList.append(wx.StaticText(
			self.swMatrix,
			label='Amino acids',
			)
		)	
	 #--- Create the needed rows
		for a in range(1, NRow+1, 1):
			self.stPosList.append(wx.StaticText(
				self.swMatrix,
				label=str(a),
				)
			)
			self.tcPosList.append(wx.TextCtrl(
				self.swMatrix,
				size=config.size['TextCtrl'][self.nameWin]['Pos'],
				style=wx.TE_CENTRE,
				)
			)
			self.tcAAList.append(wx.TextCtrl(
				self.swMatrix,
				size=config.size['TextCtrl'][self.nameWin]['AA'],
				)
			)
	 #--- Add to sizer
		for k, v in enumerate(self.tcAAList):
			if k > 0:
				border = 2
			else:
				border = 5
			self.sizerSW.Add(
				self.stPosList[k],
				flag=wx.ALIGN_CENTER|wx.ALL,
				border=border,
			)
			self.sizerSW.Add(
				self.tcPosList[k],
				flag=wx.ALIGN_CENTER|wx.ALL,
				border=border,				
			)
			self.sizerSW.Add(
				v,
				flag=wx.ALIGN_CENTER|wx.ALL,
				border=border,				
			)
	 #--- Fit Sizer
		self.sizerSW.Fit(self.swMatrix)
	 #--- Adjust the size of the scrolled window
		self.swMatrix.SetSize(config.size["ScrolledW"][self.nameWin])
		self.swMatrix.SetVirtualSize(self.sizerSW.GetSize())
		self.swMatrix.SetScrollRate(20,20)
	 #--- Return
		return True
	#---
#---
