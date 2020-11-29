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

from dat4s_core.config.config import optAA as dtsOptAA
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
		'MainW'        : 'MainW',
		'ConsensusConf': 'ConsensusConf',
	},
	'Tab' : { #--> Tab for notebook windows
		'Peptide'  : 'Peptide',
		'Gene'     : 'Gene',
		'Consensus': 'Consensus',
		'LicAgr'   : 'LicAgr',
		'Help'     : 'Help',
	},
	'Panes' : {#--> Panes
		'UserInput' : 'UserInput',
		'ListCtrl'  : 'ListCtrl',
	},
}

title = { # Title of windows, tabs and panes
	#--> Window
	'MainW'   : f'Peptide Search Tools {version}',
	'ConsConf': 'Consensus sequence configuration',
	#--> Tab
	'Peptide'  : 'Peptide.txt',
	'Gene'     : 'Gene.fasta',
	'Consensus': 'Consensus',
	'LicAgr'   : 'License Agreement',
	'Help'     : 'Quick help',
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
	'ListCtrl' : { # wx.ListCtrl
		'Peptide' : (50, 150),
	},
	'ScrolledW' : { # wx.ScrolledWindow
		'ConsensusConf' : (520, 200),
	},
	'TextCtrl' : { # wx.TextCtrl
		'ConsensusConf' : { # gui.window.ConsensusConf
			'Position': (180,22),
			'AA'      : (220, 22),
		},
	},
}
#endregion ------------------------------------------------------------> Sizes

#region ----------------------------------------------------------> Extensions
extLong = { # string for the dlg windows representing the extension of the files
	'Data': 'txt files (*.txt)|*.txt',
	'Seq' : 'txt fasta files (*.txt; *.fasta)|*.txt;*.fasta',
}
#endregion -------------------------------------------------------> Extensions

#region -----------------------------------------------------------> Dict Keys
dictKey = { # Import dict keys
	'ConsensusConf' : { # gui.window.ConsensusConf
		'PosKey' : 'Pos',
	},
}
#endregion --------------------------------------------------------> Dict Keys

#region --------------------------------------------------------------> Labels
label = { # Label for wx.Buttons, wx.StaticText, etc
	'ButtonGroup' : { # gui.widgets.ButtonGroup
		'Clear': 'Clear All',
		'Run'  : 'Search',
	},
	'BaseTab' : { # gui.tab.BaseTab
		'File'  : 'Files',
		'Value' : 'User-defined values',
		'Column': 'Columns in the input files',
	},
	'Peptide' : { # gui.tab.PeptideTab
		'DataFile'    : 'Data File',
		'OutFile'     : 'Output File',
		'FirstResidue': 'First Residue <=',
		'StartResidue': 'Start Residue',
		'ColExtract'  : 'Columns to Extract',
		'Column'      : ("#", "Column's name"),
	},
	'Gene' : { # gui.tab.GeneTab
		'FastaFile'     : 'Fasta File',
		'GeneFile'      : 'Gene File',
		'OutFile'       : 'Output File',
		'ResidueExtract': 'Residues to Extract',
	},
	'Consensus' : { # gui.tab.ConsensusTab
		'FastaFile': 'Fasta File',
		'OutFile'  : 'Output File',
		'PosAA'    : "Positions && AAs",       # && Needed for wxPython
		'CompProt' : 'Only complete proteins',
	},
	'ConsensusConf' : { # gui.window.ConsensusConf
		'Number'  : 'Number of positions',
		'Create'  : 'Create fields',
		'Position': 'Residue Numbers',
		'AA'      : 'Amino Acids',
	},
}
#endregion -----------------------------------------------------------> Labels

#region ---------------------------------------------------------------> Hints
hint = { # Hint for wx.TextCtrl
	'Peptide' : { # gui.tab.PeptideTab
		'DataFile' : f"Path to the {label['Peptide']['DataFile']}.",
		'OutFile' : f"Path to the {label['Peptide']['OutFile']}.",
		'FirstResidue' : (
			f"Non-negative Integer, e.g. 2. First residue number must be less "
			f"equal than the number given here."),
		'StartResidue' : (
			f"Non-negative Integer, e.g. 36. Column number containing the "
			f"Start residue numbers."),
		'ColExtract' : (
			f"Space-separated list of non-negative integers, e.g. 0 38 36 37. "
			f"Columns to extract from the {label['Peptide']['DataFile']}."),
	},
	'Gene' : { # gui.tab.GeneTab
		'FastaFile': f"Path to the {label['Gene']['FastaFile']}.",
		'GeneFile' : f"Path to the {label['Gene']['GeneFile']}.",
		'OutFile'  : f"Path to the {label['Gene']['OutFile']}.",
		'ResidueExtract' : (
			f"Space-separated list of positive integers, e.g. 5 10 20 50. "
			f"Lengths of the N-terminal peptides to extract from the "
			f"{label['Gene']['FastaFile']}."),
	},
	'Consensus' : { # gui.tab.ConsensusTab
		'FastaFile': f"Path to the {label['Consensus']['FastaFile']}.",
		'OutFile'  : f"Path to the {label['Consensus']['OutFile']}.",
		'PosAA'    : (
			f"Dictionary e.g. {{2: 'A W', 3: 'S T', 4: 'I A', 'Pos': True}} "
			f"with the positions to analyse and the AAs to search for."),
	},
	'ConsensusConf' : { # gui.window.ConsensusConf
		'Position' : ("Integer (> 0) or NA, e.g. 3."),
		'AA' : ("Space-separated list of AAs, e.g. A H K."),
	},
}
#endregion ------------------------------------------------------------> Hints

#region -----------------------------------------------------------------> Msg
msg = { # Messages for the user
	'Success' : "The analysis finished correctly.",
	'Step' : { # Statusbar msg for steps in Run
		'Check'  : 'Checking user input',
		'Prepare': f"Preparing the {label['ButtonGroup']['Run']}",
		'Run'    : "Running the analysis",
		'Output' : "Writing output",
	},
	'Error' : { # Error msgs
		'Peptide' : { # gui.tab.PeptideTab
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
				f"can be accepted in {label['Peptide']['ColExtract']}.\n"
				f"In addition, numbers must be lower/equal than the total "
				f"number of columns in the {label['Peptide']['DataFile']}."),
			'NoPeptide' : (
				f"There were no N-terminal peptides found in the "
				f"{label['Peptide']['DataFile']}."),
		},
		'Gene' : { # gui.tab.GeneTab
			'FastaFile' : (
				f"Select the path to the {label['Gene']['FastaFile']}."),
			'GeneFile' : (
				f"Select the path to the {label['Gene']['GeneFile']}."),
			'OutFile' : (
				f"Select the path to the {label['Gene']['OutFile']}."),
			'ResidueExtract' : (
				f"Only a list of space-separated positive integer numbers "
				f"can be accepted in {label['Gene']['ResidueExtract']}."),
			'NoGene' : (
				f"There were no Gene names in the given "
				f"{label['Gene']['GeneFile']}"),
			'NoProtFound' : (
				f"There were no proteins in the {label['Gene']['FastaFile']} "
				f"associated with the gene names read from the "
				f"{label['Gene']['GeneFile']}."),
		},
		'Consensus' : { # gui.tab.GeneTab
			'FastaFile' : (
				f"Select the path to the {label['Consensus']['FastaFile']}."),
			'OutFile' : (
				f"Select the path to the {label['Consensus']['OutFile']}."),
			'PosAA' : f"Define the {label['Consensus']['PosAA']} to analyse.",
		},
		'ConsensusConf' : {
			'Number' : (
				f"Only a positive integer can be accepted in "
				f"{label['ConsensusConf']['Number']}."),
			'Position' : (
				f"The values for {label['ConsensusConf']['Position']} must be "
				f"all NA or all positive integers."),
			'PosUnique' : (
				f"The values for {label['ConsensusConf']['Position']} must be "
				f"unique, if not NA."),
			'PosIncrease' : (
				f"The values for {label['ConsensusConf']['Position']} must be "
				f"monotonically increasing, if not NA."),
			'AA' : (
				f"Only a space-separated list of AAs (one letter code) can be "
				f"accepted in {label['ConsensusConf']['AA']}."
			),
		},
	},
}
#endregion --------------------------------------------------------------> Msg

#endregion --------------------------------------> NON-CONFIGURABLE PARAMETERS

#region ---------------------------------------------> CONFIGURABLE PARAMETERS
optAA = dtsOptAA

#endregion ------------------------------------------> CONFIGURABLE PARAMETERS

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
