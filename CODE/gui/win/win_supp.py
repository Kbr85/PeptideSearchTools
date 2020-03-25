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


""" This module contain classes for supporting windows e.g. select files """


#--- Imports
import wx
import ast
from pathlib import Path

import config.config as config
import data.data_methods as dmethods
import check.check_single as checkS
import check.check_multiple as checkM
#---


class GuiCheck():
	""" This class contains only methods to check user input """

	def GuiCheckInputFile(self, n, tc, msg, NA=False):
		""" Check if the user selected a file that can be read. 
			Since the user cannot type the path to the file, only read
			permission need to be check
			---
			n : key for self.d & self.do (str)
			tc : wx.TextCtrl with the input
			msg : error message (str)
			NA: is allowed or not (boolean)
		"""

	 #--> Set Initial values and check for NA values 
		if self.SetInitVal(tc, n, msg, NA):
			pass
		else:
			return False
	 #---
	 #--> Check file can be read & create Path instance for self.do[n]
		if checkS.CheckFileRead(self.d[n]):
			self.do[n] = Path(self.d[n])
			return True
		else:
			MyFatalErrorMessage(msg)
			return False
	 #---
	#---

	def GuiCheckOutFile(self, n, tc, msg, NA=False):
		""" Check if the user selected a file that can be used for save. 
			Since the user cannot type the path to the file, only write
			permission need to be check
			---
			n : key for self.d & self.do (str)
			tc : wx.TextCtrl with the input
			msg : error message (str)
			NA: is allowed or not (boolean)
		"""

	 #--> Set Initial values and check for NA values 
		if self.SetInitVal(tc, n, msg, NA):
			pass
		else:
			return False
	 #---
	 #--> Check file can be read & create Path instance for self.do[n]
		if checkS.CheckFileWrite(self.d[n]):
			self.do[n] = Path(self.d[n])
			return True
		else:
			MyFatalErrorMessage(msg)
			return False
	 #---
	#---

	def GuiCheckInteger(self, n, tc, msg, t='int', comp='gt', NA=False):
		""" Check that only and integer is given 
			---
			n : key for self.d & self.do (str)
			tc : wx.TextCtrl with the input
			msg : error message (str)
			t : number type (float or int) (str)
			comp : zero comparison (str)
			NA: is allowed or not (boolean)			
		"""

	 #--> Set Initial values and check for NA values 
		if self.SetInitVal(tc, n, msg, NA):
			pass
		else:
			return False
	 #---
	 #-->
		out, self.do[n] = checkM.CheckMNumber(self.d[n], t=t, comp=comp)
		if out:
			return True
		else:
			MyFatalErrorMessage(msg)
			return False 
	 #---
	#---		

	def GuiCheckListNumber(self, n, tc, msg, t='int', comp='egt', val=0, 
		NA=False, Range=False, Order=False, Unique=True, DelRepeat=False):
		""" Check that tc has a list of numbers 
			---
			n: dicts key to hold output (string)
			tc: wx.TextCtrl instance
			msg: error msg (string)
			t: float, int (string)
			comp: egt >= val, e == val, gt > val, elt <= val, lt < val (string)
			val: value to compare against (number)
			NA: NA allowed (boolean)
			Rage: Range allowed (boolean)
			Order: list must be ordered low -> high (boolean)
			Unique: elements must be unique (boolean)
			DelRepeat: delete repeating elements (boolean)								
		"""

	 #--> Set Initial values and check NA
		if self.SetInitVal(tc, n, msg, NA):
			pass
		else:
			return False
	 #---
	 #--> Check list elements
		out, self.do[n] = checkM.CheckMListNumber(self.d[n], 
			t=t, 
			comp=comp, 
			val=val, 
			Range=Range, 
			Order=Order, 
			Unique=Unique, 
			DelRepeat=DelRepeat,
		)
		if out:
			return True
		else:
			MyFatalErrorMessage(msg)
			return False					
	 #---
	#---

	def GuiCheckPosAADict(self, n, n2, tc, msg, t='int', comp='gt', val=0, 
		NA=False):
		""" Check that tc holds a dict with integer gt 0 as keys and AA residues
			as values.There must be a boolean key with name as in 
			config.dictKey
			e.g. {2: 'Q W', 3: 'R T', 4: 'S A', 'Pos': True}
			---
			n: dicts key to hold output (string)
			n2: dicts key to hold the positions of the AA in 0 based numbers
			tc: wx.TextCtrl instance
			msg: error msg (string)
			t: float, int (string)
			comp: egt >= val, e == val, gt > val, elt <= val, lt < val (string)
			val: value to compare against (number)			
		"""

	 #--> Set Initial values and check NA
		if self.SetInitVal(tc, n, msg, NA):
			pass
		else:
			return False
	 #---
	 #--> k Variable
		k = True
	 #---
	 #--> Needed to keep the same order in the dict when changing keys from str to int
		self.do[n] = {}
		self.do[n2] = []
	 #---
	 #-->  Convert to dict and check class
		try:
			myDict = ast.literal_eval(self.d[n])
		except Exception:
			k = False
		if k:
			if isinstance(myDict, dict):
				pass
			else:
				k = False
		else:
			pass
	 #---
	 #--> Check key (integers), values (only AA in one letter code and unique for each k-v pair)
		if k:
		 #--- To control that PosKey is present in the dict keys
			PosKey = False
			for i, v in myDict.items():
				if i != config.dictKey[config.winName['confSearch']]['PosKey']:
				 #--- Keys are integers
					try:
						kInt = int(i)
					except Exception:
						k = False
						break
				 #--- Unique AA in each k-v pair
					lv = dmethods.str2l(v, ' ')[1]
					if len(lv) == len(set(lv)):
						pass
					else:
						k = False
						break
				 #--- Only AA in the value
					if checkS.CheckListAinListB(lv, config.oneLetterAA):
						self.do[n][kInt] = lv
						self.do[n2].append(kInt-1)
					else:
						k = False
						break
				else:
					self.do[n][i] = v 
					PosKey = True
			if PosKey:
				pass
			else:
				k = False
		else:
			pass
	 #---
	 #--> Return
		return self.CheckK(k, msg)
	 #---
	#---

	def SetInitVal(self, tc, n, msg, NA):
		""" Set the initial value for self.d[n] and self.do[n] 
			---
			tc: wx.TextCtrl with the user given value
			n: key for self.d & self.do
		"""

	 #--> Get string in tc
		val = tc.GetValue()
	 #---
	 #--> Set self.d[n] & self.do[n]
		if val in config.naVals:
			self.d[n] = val
			self.do[n] = None
			if self.CheckNA(NA):
				return True
			else:
				MyFatalErrorMessage(msg)
				return False			
		else:
			self.d[n] = self.do[n] = val
	 #---
	 #--> Return	
		return True
	 #---
	#---

	def CheckNA(self, NA):
		""" Check if NA values are allowed
			Return: True (nothing else need to be check, Return True)
				    False (NA value found but not allowed, Return False)
			---
			NA: NA values are allowed or not (boolean) 
		"""

		if NA:
			return True
		else:
			return False
	#---

	def CheckK(self, k, msg):
		""" For a multicheck function k holds a boolean stating whether the 
			check was succesfull or not
			---
			k: boolean
			msg: error msg (string)
		"""

		if k:
			return True
		else:
			MyFatalErrorMessage(msg)
			return False
	#---
#---


class MyOpenFile(wx.FileDialog):
	""" Defines my custom open file dialog window """

	def __init__(self, message, wildcard):
		""""""

		super().__init__(
			None, 
			message=message, 
			wildcard=wildcard, 
			style=wx.FD_OPEN|wx.FD_CHANGE_DIR|wx.FD_FILE_MUST_EXIST|wx.FD_PREVIEW
		)
	#---
#---


class MySaveFile(wx.FileDialog):
	""" My save file windows """

	def __init__(self, message, wildcard):
		""""""

		super().__init__(
			None, 
			message=message, 
			wildcard=wildcard, 
			style=wx.FD_SAVE|wx.FD_OVERWRITE_PROMPT
		)
	#---
#---


class MySuccessMessage(wx.MessageDialog):
	""" Defines a custom message box with title All done!!! and style """
	
	def __init__(self, message):
		""""""

		super().__init__(
			None, 
			message=message, 
			caption='All done!!!', 
			style=wx.OK|wx.ICON_INFORMATION
		)
		self.Center()
		self.ShowModal()
		self.Destroy()
	#---
#---


class MyFatalErrorMessage(wx.MessageDialog):
	""" Defines a custom message box with title Fatal Error Detected and style 
	"""

	def __init__(self, message):
		""""""

		super().__init__(
			None, 
			message=message, 
			caption='Fatal Error Detected', 
			style=wx.OK|wx.ICON_ERROR
		)
		self.Center()
		self.ShowModal()
		self.Destroy()
	#---
#---


class MyWarningMessageOK(wx.MessageDialog):
	""" Defines a custom warning message """

	def __init__(self, message):
		""""""

		super().__init__(
			None, 
			message=message, 
			caption='Warning', 
			style=wx.OK|wx.ICON_EXCLAMATION
		)
		self.Center()
		self.ShowModal()
		self.Destroy()
	#---
#---
