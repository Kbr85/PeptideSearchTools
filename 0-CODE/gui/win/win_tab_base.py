# ------------------------------------------------------------------------------
# 	Copyright (C) 2019-2020 Kenny Bravo Rodriguez

# 	This program is distributed for free in the hope that it will be useful,
# 	but WITHOUT ANY WARRANTY; without even the implied warranty of
# 	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

# 	See the accompaning licence for more details.
# ------------------------------------------------------------------------------

""" This module generates the base class for the tabs in the Notebook """

#--- Imports
## Standard modules
import wx
## My modules
import config.config as config
from gui.win.win_supp import (
	GuiCheck,
	MyOpenFile,
	MySaveFile,
	MySuccessMessage,
)
#---


class BaseTab(wx.Panel, GuiCheck):
	""" This creates the base class for the tabs in the notebook """

	def __init__(self, parent, statusbar=None):
		""""""
		super().__init__(parent=parent)
	 #--- Widgets
	  #--- Panels
		self.tabPanel = wx.Panel(self)
	  #--- Satus bar from main class
		if statusbar is not None:
			self.statusbar = statusbar
		else:
			pass
	  #--- Static boxes
		self.boxFiles = wx.StaticBox(self.tabPanel, label="Files")
		self.boxValues  = wx.StaticBox(
			self.tabPanel, 
			label="User defined values"
		)
		self.boxColumns = wx.StaticBox(
			self.tabPanel, 
			label="Columns in the input file"
		)
	  #--- Text control
		self.tcInputFile = wx.TextCtrl(
			self.boxFiles,   
			value="", 
			size=config.size['TextCtrl']['File'][self.nameTab], 
			style=wx.TE_READONLY
		)
		self.tcOutFile = wx.TextCtrl(
			self.boxFiles,   
			value="", 
			size=config.size['TextCtrl']['File'][self.nameTab], 
			style=wx.TE_READONLY
		)
		self.tcUserValue = wx.TextCtrl(
			self.boxValues,  
			value='', 
			size=config.size['TextCtrl']['Value'][self.nameTab],
		)
	  #--- StaticText
		self.stUserValue = wx.StaticText(
			self.boxValues, 
			label=config.tabLabel[self.nameTab]['firstUserValue'], 
			style=wx.ALIGN_RIGHT
		)				
	  #--- Buttons
		self.buttonInputFile = wx.Button(
			self.boxFiles, 
			label=config.tabLabel[self.nameTab]['input'],
		)
		self.buttonOutFile = wx.Button(
			self.boxFiles, 
			label=config.tabLabel[self.nameTab]['output'],
		)
		self.buttonStart     = wx.Button(self.tabPanel, label='Search')
		self.buttonClear     = wx.Button(self.tabPanel, label='Clear All')
		self.buttonSetDef    = wx.Button(self.tabPanel, label='Default Values')
	 #--- Sizers
	  #--- StaticBoxSizers
	   #--- Files
		self.sizerboxFiles = wx.StaticBoxSizer(self.boxFiles, wx.VERTICAL)
		self.sizerboxFilesWid = wx.FlexGridSizer(3, 2, 1, 1)
		self.sizerboxFiles.Add(
			self.sizerboxFilesWid,   
			border=2, 
			flag=wx.EXPAND|wx.ALIGN_CENTER|wx.ALL
		)
		self.sizerboxFilesWid.Add(
			self.buttonInputFile, 
			border=2, 
			flag=wx.EXPAND|wx.ALIGN_CENTER|wx.ALL
		)
		self.sizerboxFilesWid.Add(
			self.tcInputFile,     
			border=2, 
			flag=wx.EXPAND|wx.ALIGN_CENTER|wx.ALL
		)
		self.sizerboxFilesWid.Add(
			self.buttonOutFile,   
			border=2, 
			flag=wx.EXPAND|wx.ALIGN_CENTER|wx.ALL
		)
		self.sizerboxFilesWid.Add(
			self.tcOutFile,       
			border=2, 
			flag=wx.EXPAND|wx.ALIGN_CENTER|wx.ALL
		)		
	   #--- Values
		self.sizerboxValues = wx.StaticBoxSizer(self.boxValues, wx.VERTICAL)
		self.sizerboxValuesWid = wx.GridBagSizer(1, 1)
		self.sizerboxValues.Add(
			self.sizerboxValuesWid,  
			border=2, 
			flag=wx.EXPAND|wx.ALIGN_CENTER|wx.ALL
		)
		self.sizerboxValuesWid.Add(
			self.stUserValue,
			pos=(0,0), 
			border=2, 
			flag=wx.ALIGN_CENTER|wx.ALL
		)	
		self.sizerboxValuesWid.Add(
			self.tcUserValue, 
			pos=(0,1),
			border=2, 
			flag=wx.EXPAND|wx.ALIGN_CENTER|wx.ALL
		)			
	   #--- Columns
		self.sizerboxColumns = wx.StaticBoxSizer(self.boxColumns, wx.VERTICAL)
		self.sizerboxColumnsWid = wx.FlexGridSizer(2, 2, 1, 1)
		self.sizerboxColumns.Add(
			self.sizerboxColumnsWid, 
			border=2, 
			flag=wx.EXPAND|wx.ALIGN_CENTER|wx.ALL
		)
	  #--- Sizer for buttons
		self.sizerButton = wx.FlexGridSizer(1, 3, 1, 1)
		self.sizerButton.Add(
			self.buttonClear,  
			border=2, 
			flag=wx.EXPAND|wx.ALIGN_CENTER|wx.ALL
		)
		self.sizerButton.Add(
			self.buttonSetDef, 
			border=2, 
			flag=wx.EXPAND|wx.ALIGN_CENTER|wx.ALL
		)
		self.sizerButton.Add(
			self.buttonStart,  
			border=2, 
			flag=wx.EXPAND|wx.ALIGN_CENTER|wx.ALL
		)
	  #--- Main Sizer
		self.sizerTab = wx.GridBagSizer(1, 1)
		self.sizerTab.Add(
			self.sizerboxFiles,   
			pos=(0,0),
			flag=wx.EXPAND|wx.ALIGN_CENTER|wx.ALL, 
			border=2
		)
		self.sizerTab.Add(
			self.sizerboxValues,  
			pos=(1,0),
			flag=wx.EXPAND|wx.ALIGN_CENTER|wx.ALL, 
			border=2
		)
		self.sizerTab.Add(
			self.sizerboxColumns, 
			pos=(2,0), 
			flag=wx.EXPAND|wx.ALIGN_CENTER|wx.ALL, 
			border=2
		)
		self.sizerTab.Add(
			self.sizerButton    , 
			pos=(3,0), 
			flag=wx.ALIGN_CENTER|wx.ALL, 
			border=2
		)
	 #--- Bind
		self.buttonInputFile.Bind(wx.EVT_BUTTON, self.OnInputFile)
		self.buttonOutFile.Bind(wx.EVT_BUTTON, self.OnOutFile)
		self.buttonClear.Bind(wx.EVT_BUTTON, self.OnClear)
		self.buttonSetDef.Bind(wx.EVT_BUTTON, self.OnDef)
		self.buttonStart.Bind(wx.EVT_BUTTON, self.OnStart)
	#---

	#--- Methods of the class
	def OnInputFile(self, event):
		""" Select the input file """
	 
	 #--- Configure
		msg = config.myOpenFile[self.nameTab]['Msg']
		ext = config.myOpenFile[self.nameTab]['ExtLong']
	 #--- Get file
		dlg = MyOpenFile(msg, ext)
		if dlg.ShowModal() == wx.ID_OK:
			self.tcInputFile.SetValue(dlg.GetPaths()[0])
			return True
		else:
			return False	
	#---

	def OnOutFile(self, event):
		""" Select output file """
	 
	 #--- Configure 
		msg = config.myOutFile[self.nameTab]['Msg'] 
		ext = config.myOutFile[self.nameTab]['ExtLong']
	 #--- Get file 
		dlg = MySaveFile(msg, ext)
		if dlg.ShowModal() == wx.ID_OK:
			self.tcOutFile.SetValue(dlg.GetPath())
			return True
		else:
			return False
	#---

	def OnClear(self, event):
		""" Clear all wx.TextCtrl """
		
		for a in [self.sizerboxFilesWid, self.sizerboxValuesWid, self.sizerboxColumnsWid]:	
			children = a.GetChildren()
			for child in children:
				widget = child.GetWindow()
				if isinstance(widget, (wx.TextCtrl, wx.CheckBox)):
					try:
						widget.SetValue("")
					except TypeError:
						widget.SetValue(False)
				else:
					pass
		return True
	#---

	def OnDef(self, event):
		""" Override as needed """
		return True
	#---

	def OnStart(self, event):
		""" Start the analysis """	

		if self.run():
			MySuccessMessage('Analysis completed')
			self.statusbar.SetStatusText('')
			return True
		else:
			self.statusbar.SetStatusText('')
			return False
	#---

	def run(self):
		""" Run the analysis so Start can control de GUI more easily """
	
	 #--- Create dicts
		self.d = {}
		self.do = {}
	 #--- Check, run & save
		self.statusbar.SetStatusText('Checking user input')
		wx.Yield()	
		if self.CheckInput():
			pass
		else:
			return False
		self.statusbar.SetStatusText('Proccesing data')
		wx.Yield()
		if self.DataProcessing():
			pass
		else:
			return False	
		self.statusbar.SetStatusText('Writting output')
		wx.Yield()
		if self.WriteOutput():
			return True
		else:
			return False
	#---

	def CheckInput(self):
		""" Override as needed """
		return True
	#---

	def DataProcessing(self):
		""" Override as needed """
		return True
	#---

	def WriteOutput(self):
		""" Override as needed """
		return True
	#---
#---	