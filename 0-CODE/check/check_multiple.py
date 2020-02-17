# ------------------------------------------------------------------------------
# 	Copyright (C) 2019-2020 Kenny Bravo Rodriguez

# 	This program is distributed for free in the hope that it will be useful,
# 	but WITHOUT ANY WARRANTY; without even the implied warranty of
# 	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

# 	See the accompaning licence for more details.
# ------------------------------------------------------------------------------

""" This module contain methods to check user input """

#--- Imports
## Standard modules

## My modules
import check.check_single as checkS
#---


def CheckMNumber(num, t="float", comp="egt", val=0, val2=None):
	""" Check if a number is of type t and compare the number to val
		---
		num : variable holding the number (float or string)
		t   : possible values; float, int, etc (string)
		comp: possible values; egt, e, gt, elt, lt (string) 
		val : value to compare against (float)
		val2: value to define a range in wich num must be (float)
	"""
 #--- Check num type
	out, numT = checkS.CheckNumType(num, t)
	if out:
		pass
	else:
		return [False, None]
 #--- Compare & Return
	if val2 == None:
		if checkS.CheckNumComp(numT, comp, val):
			return [True, numT]
		else:
			return [False, None]
	else:
		if checkS.CheckaWithincd(numT, val, val2):
			return [True, numT]
		else:
			return [False, None]
#---

def CheckMListNumber(listV, t="float", comp="egt", val=0, Range=False,
	Order=False, Unique=True, DelRepeat=False, NA=False):
	""" Check if a list contains only number of type t and compare to val.
		Check also for range of numbers, unique elements and order. 
		---
		listV : list with the values (string)
		t     : possible values; float, int, etc (string)
		comp  : possible values; egt, e, gt, elt, lt (string)
		val   : value to compare against (float)
		Range : range allows in values
		Order : number must be in ascending order or not
		Unique: numbers must be unique or not
		DelRepeat : delete repeated elements or not
		NA    : NA values could be present or not
		----
		Returned list has proper type and expanded ranges. 
	"""
	# This is meant for user-built lists so multiple iteration over the list
	# will not have a big impact over execution time. So split for easier
	# mantienance and expansion
 #--- Split string into a list
	lin  = listV.strip().split(" ")
	lout = []
 #--- NA values
	if 'NA' in lin:
		if NA:
			if len(lin) == 1:
				lout.append(None)
				return [True, lout]
			else:
				return [False, None]
		else:
			return [False, None]
	else:
		pass
 #--- Fix each element
	for i in lin:
		#--- Empty element comming from split &| user input
		if i == "" or i == " ":
			pass
		#--- Number
		elif "-" not in i:
			out, num = CheckMNumber(i, t, comp, val)
			if out:
				lout.append(num)
			else:
				return [False, None]
		#--- Range or negative number
		else:
			ii = i.split("-")
			lii = len(ii)
			#--- Extra - character in range/number
			if lii > 2:
				return [False, None]
			#--- Negative number
			elif lii == 2 and ii[0] == "":
				out, num = CheckMNumber(i, t, comp, val)
				if out:
					lout.append(num)
				else:
					return [False, None]
			#--- Actual range
			elif lii == 2 and ii[0] != "":
				if Range:
					iie = []
					#--- Check range limit values against t, comp & val input
					for x in ii:
						out, num = CheckMNumber(x, t, comp, val)
						if out:
							iie.append(num)
						else:
							return [False, None]
					#--- Check a < b in range a-b
					if iie[0] >= iie[1]:
						return [False, None]
					else:
						#--- Expand range
						lout += range(iie[0], iie[1] + 1)
				else:
					return [False, None]
			else:
				# DlgBugMsg
				pass
 #--- Unique elements. Must be here to catch repeated elements after range
 #	 expansion
	if Unique:
		if checkS.CheckListUniqueElements(lout):
			pass
		else:
			#--- Remove duplicates
			if DelRepeat:
				lout = list(dict.fromkeys(lout))
			else:
				return [False, None]
	else:
		pass		
 #--> Order the list
	if Order:
		lout.sort()
	else:
		pass
 #--> Return
	return [True, lout]
#---