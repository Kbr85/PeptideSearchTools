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


""" This module contains the main configuration parameters of the app """


#region -------------------------------------------------------------> Imports
import os
import platform
from pathlib import Path
#endregion ----------------------------------------------------------> Imports

#region ------------------------------------------ NON-CONFIGURABLE PARAMETERS

#region --------------------------------------------------> General parameters
development = True # To control variables with different values in dev or prod
version     = '1.0.1' # String to write in the output files
cOS         = platform.system() # Current operating system
cwd = Path(os.path.abspath(os.path.dirname(__file__))) # Current directory
#endregion -----------------------------------------------> General parameters

#region ---------------------------------------- PLATFORM DEPENDENT PARAMETERS
if cOS == 'Darwin':
	#--> Fix cwd and set the location of the Resources folder
	cwd = cwd.parent
	cwd = cwd.parent
	if development:
		res = cwd / 'BORRAR-PeptideSearchTools/RESOURCES'
	else:
		res = cwd / 'Resources'

elif cOS == 'Windows':
	#--> Fix cwd and set the location of the Resources folder
	cwd = cwd.parent
	res = cwd / 'RESOURCES'

elif cOS == 'Linux':
	#--> Fix cwd and set the location of the Resources folder
	res = cwd / 'RESOURCES'
else:
	pass
#endregion ------------------------------------- PLATFORM DEPENDENT PARAMETERS

#region ----------------------------------------------------> Names and titles
name = { # Unique names to identify windows/objects through the config file
	'Window': { #--> Main windows
		'MainW' : 'MainW',
	},
	'Tab' : { #--> Tab for notebook windows
		'PeptS' : 'PeptS',
		'Gene'  : 'Gene',
		'SeqSet': 'SeqSet',
		'LicAgr': 'LicAgr',
		'Help'  : 'Help',
	},
	'Panes' : {#--> Panes
		'UserInput' : 'UserInput',
		'ListCtrl'  : 'ListCtrl',
	},
}

title = { # Title of windows, tabs and panes
	#--> Window
	'MainW' : f'Peptide Search Tools {version}',
	#--> Tab
	'PeptS' : 'Peptide.txt',
	'Gene'  : 'Gene.fasta',
	'SeqSet': 'Consensus',
	'LicAgr': 'License Agreement',
	'Help'  : 'Quick help',
	#--> Pane
	'UserInput' : 'User input',
	'ListCtrl'  : 'Columns in the main input file',
}
#endregion -------------------------------------------------> Names and titles

#region ------------------------------------------------------> Path and Files
path = { # Relevant paths
	'CWD'      : cwd,
	'Resources': res,
}
file = { # Location of important files
	'LicAgr': res / 'TXT/license.txt',
	'Help'  : res / 'TXT/example.txt',
}
#endregion ---------------------------------------------------> Path and Files

#region ---------------------------------------------------------------> Sizes
size = { # Base size for widgets
	'MainW' : (900, 480),
	'ListCtrl' : {
		'Peptide' : (50, 150),
	},
}
#endregion ------------------------------------------------------------> Sizes

#region ----------------------------------------------------------> Extensions
extLong = { # string for the dlg windows representing the extension of the files
	'Data': 'txt files (*.txt)|*.txt',
	'Seq' : 'txt fasta files (*.txt; *.fasta)|*.txt;*.fasta',
}
#endregion -------------------------------------------------------> Extensions

#region --------------------------------------------------------------> Labels
label = { # Label for wx.Buttons, wx.StaticText, etc
	'ButtonGroup' : { # For gui.widgets.ButtonGroup
		'Clear': 'Clear All',
		'Run'  : 'Search',
	},
	'BaseTab' : { # For gui.tab.BaseTab
		'File'  : 'Files',
		'Value' : 'User-defined values',
		'Column': 'Columns in the input files',
	},
	'Peptide' : { # For gui.tab.Peptide
		'FirstResidue': 'First Residue <=',
		'StartResidue': 'Start Residue',
		'ColExtract'  : 'Columns to Extract',
		'DataFile'    : 'Data File',
		'OutFile'     : 'Output File',
		'Column'      : ("#", "Column's name"),
	},
}
#endregion -----------------------------------------------------------> Labels

#region ---------------------------------------------------------------> Hints
hint = { # Hint for wx.TextCtrl
	'Peptide' : { # For gui.tab.Peptide
		'DataFile' : f"Path to the {label['Peptide']['DataFile']}.",
		'OutFile' : f"Path to the {label['Peptide']['OutFile']}.",
		'FirstResidue' : (
			f"Non-negative Integer, e.g. 2. First residue number must be less "
			f"equal than the number given here."),
		'StartResidue' : (
			f"Non-negative Integer, e.g. 36. Column number containing the "
			f"Start residue numbers."),
		'ColExtract' : (
			f"NA or Space-separated list of non-negative integers, e.g. 0 38 36"
			f" 37. Columns to extract from the {label['Peptide']['DataFile']}."),
	},
}
#endregion ------------------------------------------------------------> Hints

#region ---------------------------------------------------------------> Msg
msg = { # Messages for the user
	'Step' : { # Statusbar msg for steps in Run
		'Check' : 'Checking user input',
	},
	'Error' : { # Error msgs
		'Peptide' : { # For gui.tab.Peptide
			'DataFile' : (
				f"Select the path to the {label['Peptide']['DataFile']}."),
			'OutFile' : (
				f"Select the path to the {label['Peptide']['OutFile']}."),
			'FirstResidue' : (
				f"Only an integer number greater or equal than 1 "
				f"can be accepted in {label['Peptide']['FirstResidue']}."),
			'StartResidue' : (
				f"Only an integer number greater or equal than 0 "
				f"can be accepted in {label['Peptide']['StartResidue']}.\n"
				f"In addition, the number must be lower/equal than the total "
				f"number of columns in the {label['Peptide']['DataFile']}."),
			'ColExtract' : (
				f"Only a list of space-separated non-negative integer numbers "
				f"or the value NA can be accepted in "
				f"{label['Peptide']['ColExtract']}.\n"
				f"In addition, numbers must be lower/equal than the total "
				f"number of columns in the {label['Peptide']['DataFile']}."),
		},
	},
}
#endregion ------------------------------------------------------------> Msg


# win = { # To track the existence and number of certain windows. 
# 		# None values change to a reference to the open window.
# 	'Open'  : [], # List of all open windows in the program
#  #--> Main like windows
# 	winName['main']      : None,
# 	winName['licagr']    : None,
# 	winName['help']      : None,
# 	winName['confSearch']: None,
# 	'copyShow'           : True, # This is to show the copyright only when the app starts
# }

# title = { # Title of the main windows
# 	winName['main']      : name + ' ' + version,
# 	winName['licagr']    : "License Agreement",
# 	winName['help']      : 'Quick Help',
# 	winName['confSearch']: 'Consensus Search Configuration',
# 	'app' 				 : name,
# }



# size = { # Size related options
# 	'window' : {
# 		winName['main']      : (650, 380),
# 		winName['licagr']    : (650, 670),
# 		winName['help']      : (650, 670),
# 		winName['confSearch']: (650, 420),
# 	},
# 	'TextCtrl' : {
# 		'File' : {
# 			tabName['pept']  : (495, 22),
# 			tabName['gene']  : (495, 22),
# 			tabName['seqset']: (495, 22),
# 		},
# 		'Value' : {
# 			tabName['pept']  : (475, 22),
# 			tabName['gene']  : (458, 22),
# 			tabName['seqset']: (390, 22),
# 		},
# 		'Column' : {
# 			tabName['pept']  : (460, 22),
# 			tabName['gene']  : (460, 22),
# 			tabName['seqset']: (460, 22),
# 		},
# 		winName['licagr']    : (640, 600),
# 		winName['help']      : (640, 600),
# 		winName['confSearch']: {
# 			'NRes' : (50,22),
# 			'Pos'  : (150, 22),
# 			'AA'   : (390, 22),
# 		},
# 	},
# 	'ScrolledW' : {
# 		winName['confSearch'] : (640, 300),
# 	},
# }

# msg = { # Messages in the App
# 	'Copyright' :("Copyright (c) 2019 Max Planck Institute of Molecular "
# 		"Physiology"),
# 	'Open' : {
# 		'DataFile'   : 'Select the data file',
# 		'FastaFile'  : 'Select the fasta file',
# 		'GeneFile'   : 'Select the gene file',
# 	},
# 	'Save' : {
# 		'Output' : 'Select the output file',
# 	},
# 	'Errors' : {
# 		'DataFileTxt' : ("Please choose a Data File.\nOnly .txt files can be "
# 			"selected."),
# 		'FastaFile' : ("Please choose a Fasta File.\nOnly .txt or .fasta files"
# 			" can be selected."),
# 		'GeneFile' : ("Please choose a Gene File.\nOnly .txt files can be "
# 			"selected."),
# 		'OutFileTxt' : ("Please choose an Output File.\nOnly .txt files can be"
# 			" selected."),
# 		'Field_FirstResidue' : ("In the field First Residue <=\nonly a single "
# 			"integer greater than zero can be accepted."),
# 		'Field_FirstCol' : ("In the field Start Residue\nonly a single "
# 			"integer equal or greater than zero can be accepted."),
# 		'Field_ColExtract' : ("In the field Columns to Extract\nonly integers"
# 			" equal or greater than zero can be accepted."),
# 		'Field_Res2Extract' : ("In the field Residues to extract\nonly integers"
# 			" greater than zero can be accepted"),
# 		'NoPeptide' : ("There were no N-terminal peptides found in the "
# 			"Data File."),
# 		'NoGene' : ("There were no genes found in the given Gene File"),
# 		'NoProt' : ("There were no proteins from the specified genes in the"
# 			" given fasta formatted file."),
# 		'NRes' : ("Please define the number of residues in the consensus "
# 			"sequence"),
# 		'PosAAs' : ("Please use the Configure button in the User defined values"
# 			" section to provide a valid value for Positions & AAs."),
# 		'NoSeq' : ("The consensus sequences were not found in the fasta file."),
# 	},	
# }

# tabLabel = { # Labels in the tabs
# 	tabName['pept'] : {
# 		'input'         : 'Data File',
# 		'output'        : 'Output File',
# 		'firstUserValue': 'First Residue <=',
# 	},
# 	tabName['gene'] : {
# 		'input'         : 'Fasta File',
# 		'output'        : 'Output File',
# 		'firstUserValue': 'Residues to extract',
# 		'gene'          : 'Gene File',
# 	},	
# 	tabName['seqset'] : {
# 		'input'         : 'Fasta File',
# 		'output'        : 'Output File',
# 		'firstUserValue': "Positions && AAs",
# 		'cbCompProt'    : "Only complete proteins",
# 	}	
# }

# myOpenFile = { # Msg and extensions for the open input file dialogue
# 	tabName['pept'] : {
# 		'Msg'    : msg['Open']['DataFile'],
# 		'ExtLong': extLong['Data'],
# 	},
# 	tabName['gene'] : {
# 		'Msg'    : msg['Open']['FastaFile'],
# 		'ExtLong': extLong['Seq'],
# 	},
# 	tabName['seqset'] : {
# 		'Msg' : msg['Open']['FastaFile'],
# 		'ExtLong' : extLong['Seq'],
# 	},
# }

# myGeneFile = { # Msg and extensions for the open gene file dialogue
# 	tabName['gene'] : {
# 		'Msg'    : msg['Open']['GeneFile'],
# 		'ExtLong': extLong['Data'],
# 	},
# }

# myOutFile = { # Msg and extensions for the select output file dialogue
# 	tabName['pept'] : {
# 		'Msg'    : msg['Save']['Output'],
# 		'ExtLong': extLong['Data'],
# 	},
# 	tabName['gene'] : {
# 		'Msg'    : msg['Save']['Output'],
# 		'ExtLong': extLong['Data'],
# 	},
# 	tabName['seqset'] : {
# 		'Msg'    : msg['Save']['Output'],
# 		'ExtLong': extLong['Data'],
# 	},	
# }

# fatalErrorsMsg = { # Fatal error msgs
# 	tabName['pept'] : {
# 		'iFile'    : msg['Errors']['DataFileTxt'],
# 		'oFile'    : msg['Errors']['OutFileTxt'],
# 		'fRes'     : msg['Errors']['Field_FirstResidue'],
# 		'fResCol'  : msg['Errors']['Field_FirstCol'],
# 		'col2Ext'  : msg['Errors']['Field_ColExtract'],
# 		'NoPeptide': msg['Errors']['NoPeptide'],
# 	},
# 	tabName['gene'] : {
# 		'iFile'    : msg['Errors']['FastaFile'],
# 		'gFile'    : msg['Errors']['GeneFile'],
# 		'oFile'    : msg['Errors']['OutFileTxt'],
# 		'r2extract': msg['Errors']['Field_Res2Extract'],
# 		'noGene'   : msg['Errors']['NoGene'],
# 		'noProt'   : msg['Errors']['NoProt'],
# 	},
# 	tabName['seqset'] : {
# 		'iFile': msg['Errors']['FastaFile'],
# 		'oFile': msg['Errors']['OutFileTxt'],
# 		'PosAA': msg['Errors']['PosAAs'],
# 		'NoSeq': msg['Errors']['NoSeq'],
# 	},
# 	winName['confSearch'] : {
# 		'NRes' : msg['Errors']['NRes'],
# 	},
# }

# dictKey = { # Label for widgets in the windows
# 	winName['confSearch'] : {
# 		'PosKey' : 'Pos',
# 	},
# }

# dataFrame = { # Data frames info
# 	'Header' : {
# 		tabName['seqset'] : [
# 			'Sequence', 
# 			'Appearance', 
# 			'%_AP',
# 			'%_TP',
# 			'Prot_IDs',
# 		],
# 	},
# }

# helperDict = { # Helper dicts to pretty print Input Data in the output file
# 	tabName['pept'] : {
# 		'iFile'  : 'Data File',
# 		'oFile'  : 'Output File',
# 		'fRes'   : 'First Residue <=',
# 		'fResCol': 'Start Residue',
# 		'Col2Ext': 'Columns to Extract',
# 	},
# 	tabName['gene'] : {
# 		'iFile': 'Fasta File',
# 		'gFile': 'Gene File',
# 		'oFile': 'Output File',
# 		'r2ext': 'Residues to extract',
# 	},
# 	tabName['seqset'] : {
# 		'iFile'   : 'Fasta File',
# 		'oFile'   : 'Output File',
# 		'PosAA'   : 'Positions & AAs',
# 		'CompProt': 'Complete proteins',
# 	},
# }

# pointer = { # Pointer to methods in different classes to avoid repeating if 
# 			 # statements. This dict is filled in 
# 			 # PeptideSearch.PeptideSearchApp.AppInit
# 	'gmethods' : { # points to methods in gui.gui_methods module
# 		'WinCreate' : {}, # Methods to create a window
# 	},			 
# }

# naVals = [ # Possible NA values
# 	'N', 'n', 'No', 'NO', 'NA', '',
# ]

# oneLetterAA = [ # AA one letter codes
# 	'A', 'I', 'L', 'V', 'M', 'F', 'W', 'Y', 'R', 'K', 'D', 'E', 'C', 'Q',
# 	'H', 'S', 'T', 'N', 'G', 'P',
# ]
# #endregion --------------------------------------- NON-CONFIGURABLE PARAMETERS
