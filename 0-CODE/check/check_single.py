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
from pathlib import Path
## My modules
#---

#--------------------------------------------------- Files (Down) 
def CheckFileRead(var):
	""" Check if var points to a file that can be read in.
		---
		var : path the file (string or path)
	"""
 #--- Variables
	mfile = Path(var)
 #--- Check & Return
	try:
		fo = open(mfile, 'r')
		fo.close()
		return True
	except Exception:
		return False
#---

def CheckFileWrite(var):
	""" Check if var points to a file that can be used for write.
		---
		var : path the file (string or path)
	"""
 #--- Create path object
	varP = Path(var)
 #--- Test write
	try:
		varP.touch()
		varP.unlink()
		return True
	except Exception:
		return False
#---
#--------------------------------------------------- Files (Up)



#--------------------------------------------------- Numbers (Down)
def CheckNumType(var, t='float'):
	""" Check that var holds a number of type t. 
		---
		var : variable to check
		t   : possible values: float, int
		---
		Returns the number with the correct type. 
	"""
 #--- Variables
	k = True
 #--- Set the correct type
	if t == 'float':
		try:
			varT = float(var)
		except Exception:
			k = False
	elif t == 'int':
		try:
			varT = int(var)
		except Exception:
			k = False
	else:
		### DlgBugMsg
		pass
 #--- Return
	if k:
		return [True, varT]
	else:
		return [False, None]
#---

def CheckNumComp(num, comp='egt', val=0):
	""" Compare num to val using comp
		---
		num : number to use in the comparison (int, float, etc)
		comp: egt >= val, e == val, gt > val, elt <= val, lt < val (string)
		val : value to compare against (int, float, etc) 
	"""
 #--- Variables
	k = True
 #--- Compare
	if comp == 'gt':
		if num > val:
			return True
		else:
			k = False
	elif comp == 'egt':
		if num >= val:
			return True
		else:
			k = False
	elif comp == 'e':
		if num == val:
			return True
		else:
			k = False
	elif comp == 'elt':
		if num <= val:
			return True
		else:
			k = False
	elif comp == 'lt':
		if num < val:
			return True
		else:
			k = False
	else:
		### DlgBugMsg
		pass
 #--- Return
	if k:
		return True
	else:
		return False
#---

def CheckaWithincd(a, c, d):
	""" Check that a >= c & a <= d
		---
		a : number to check (int, float, etc)
		b, c : limits of the interval (int, float, etc)
	"""
 #--- Check & Return
	if c <= a and a <= d:
		return True
	else:
		return False
#---
#--------------------------------------------------- Numbers (Up)



#--------------------------------------------------- List (Down)
def CheckListUniqueElements(l, NA=False):
	""" Check that a list does not contains repeated elements
		---
		l : flat list
		NA: allow NA elements in the list or not (boolean)
	"""
 #--- Remove multiple NA elements if they are allowed
	if NA == False:
		lo = list(set(l))
	else:
		l = [x for x in l if x != None]
		lo = list(set(l))
 #--- Compare length of l & lo and Return
	if len(lo) == len(l):
		return True
	else:
		return False
#---

def CheckListAinListB(listA, listB):
	""" Check that all elements in listA are present in listB """
	for i in listA:
		if i in listB:
			pass
		else:
			return False
	return True
#---
#--------------------------------------------------- List (Up)