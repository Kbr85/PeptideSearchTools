# ------------------------------------------------------------------------------
# 	Copyright (C) 2019-2020 Kenny Bravo Rodriguez

# 	This program is distributed for free in the hope that it will be useful,
# 	but WITHOUT ANY WARRANTY; without even the implied warranty of
# 	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

# 	See the accompaning licence for more details.
# ------------------------------------------------------------------------------

""" This module contains the main configuration parameters of the app """

#--- Imports
## Standard modules
import platform
## My modules

#---

# ------------------------------------------------------------------------------
# NON-CONFIGURABLE PARAMETERS
# ------------------------------------------------------------------------------

version = '1.0'
name    = 'Peptide Search Tools'
cOS     =  platform.system()

winName = { # Name of the main windows, keys are id, values are usable names
	'main'      : name,
	'licagr'    : "License Agreement",
	'help'      : "Quick Help",
	'confSearch': 'Consensus Search Configuration',
}

tabName = { # Names of the tabs in the app, keys are id, values are usable names
	'pept'  : 'Peptide.txt',
	'gene'  : 'Gene.fasta',
	'seqset': 'Consensus',
}

tabOrder = { # Order of the tab in the notebook
	tabName['pept']  : 0,
	tabName['gene']  : 1,
	tabName['seqset']: 2,
}

win = { # To track the existence and number of certain windows. 
		# None values change to a reference to the open window.
	'Open'  : [], # List of all open windows in the program
 #--> Main like windows
	winName['main']      : None,
	'copyShow'           : True, # This is to show the copyright only when the app starts
	winName['licagr']    : None,
	winName['help']      : None,
	winName['confSearch']: None,
}

title = { # Title of the main windows
	winName['main']      : name + ' v' + version,
	winName['licagr']    : "License Agreement",
	winName['help']      : 'Quick Help',
	winName['confSearch']: 'Consensus Search Configuration',
	'app' 				 : name,
}

extLong = { # string for the dlg windows representing the extension of the files
	'Data': 'txt files (*.txt)|*.txt',
	'Seq' : 'txt fasta files (*.txt; *.fasta)|*.txt;*.fasta',
}

size = { # Size related options
	'window' : {
		winName['main']      : (650, 380),
		winName['licagr']    : (650, 670),
		winName['help']      : (650, 670),
		winName['confSearch']: (650, 420),
	},
	'TextCtrl' : {
		'File' : {
			tabName['pept']  : (495, 22),
			tabName['gene']  : (495, 22),
			tabName['seqset']: (495, 22),
		},
		'Value' : {
			tabName['pept']  : (475, 22),
			tabName['gene']  : (458, 22),
			tabName['seqset']: (390, 22),
		},
		'Column' : {
			tabName['pept']  : (460, 22),
			tabName['gene']  : (460, 22),
			tabName['seqset']: (460, 22),
		},
		winName['licagr']    : (640, 600),
		winName['help']      : (640, 600),
		winName['confSearch']: {
			'NRes' : (50,22),
			'Pos'  : (150, 22),
			'AA'   : (390, 22),
		},
	},
	'ScrolledW' : {
		winName['confSearch'] : (640, 300),
	},
}

msg = { # Messages in the App
	'Open' : {
		'DataFile'   : 'Select the data file',
		'FastaFile'  : 'Select the fasta file',
		'GeneFile'   : 'Select the gene file',
	},
	'Save' : {
		'Output' : 'Select the output file',
	},
	'Errors' : {
		'DataFileTxt' : ("Please choose a Data File.\nOnly .txt files can be "
			"selected."),
		'FastaFile' : ("Please choose a Fasta File.\nOnly .txt or .fasta files"
			" can be selected."),
		'GeneFile' : ("Please choose a Gene File.\nOnly .txt files can be "
			"selected."),
		'OutFileTxt' : ("Please choose an Output File.\nOnly .txt files can be"
			" selected."),
		'Field_FirstResidue' : ("In the field First Residue <=\nonly a single "
			"integer greater than zero can be accepted."),
		'Field_FirstCol' : ("In the field Start Residue\nonly a single "
			"integer equal or greater than zero can be accepted."),
		'Field_ColExtract' : ("In the field Columns to Extract\nonly integers"
			" equal or greater than zero can be accepted."),
		'Field_Res2Extract' : ("In the field Residues to extract\nonly integers"
			" greater than zero can be accepted"),
		'NoPeptide' : ("There were no N-terminal peptides found in the "
			"Data File."),
		'NoGene' : ("There were no genes found in the given Gene File"),
		'NoProt' : ("There were no proteins from the specified genes in the"
			" given fasta formatted file."),
		'NRes' : ("Please define the number of residues in the consensus "
			"sequence"),
		'PosAAs' : ("Please use the Configure button in the User defined values"
			" section to provide a valid value for Positions & AAs."),
		'NoSeq' : ("The consensus sequences were not found in the fasta file."),
	},	
}

tabLabel = { # Labels in the tabs
	tabName['pept'] : {
		'input'         : 'Data File',
		'output'        : 'Output File',
		'firstUserValue': 'First Residue <=',
	},
	tabName['gene'] : {
		'input'         : 'Fasta File',
		'output'        : 'Output File',
		'firstUserValue': 'Residues to extract',
		'gene'          : 'Gene File',
	},	
	tabName['seqset'] : {
		'input'         : 'Fasta File',
		'output'        : 'Output File',
		'firstUserValue': "Positions && AAs",
		'cbCompProt'    : "Only complete proteins",
	}	
}

myOpenFile = { # Msg and extensions for the open input file dialogue
	tabName['pept'] : {
		'Msg'    : msg['Open']['DataFile'],
		'ExtLong': extLong['Data'],
	},
	tabName['gene'] : {
		'Msg'    : msg['Open']['FastaFile'],
		'ExtLong': extLong['Seq'],
	},
	tabName['seqset'] : {
		'Msg' : msg['Open']['FastaFile'],
		'ExtLong' : extLong['Seq'],
	},
}

myGeneFile = { # Msg and extensions for the open gene file dialogue
	tabName['gene'] : {
		'Msg'    : msg['Open']['GeneFile'],
		'ExtLong': extLong['Data'],
	},
}

myOutFile = { # Msg and extensions for the select output file dialogue
	tabName['pept'] : {
		'Msg'    : msg['Save']['Output'],
		'ExtLong': extLong['Data'],
	},
	tabName['gene'] : {
		'Msg'    : msg['Save']['Output'],
		'ExtLong': extLong['Data'],
	},
	tabName['seqset'] : {
		'Msg'    : msg['Save']['Output'],
		'ExtLong': extLong['Data'],
	},	
}

fatalErrorsMsg = { # Fatal error msgs
	tabName['pept'] : {
		'iFile'    : msg['Errors']['DataFileTxt'],
		'oFile'    : msg['Errors']['OutFileTxt'],
		'fRes'     : msg['Errors']['Field_FirstResidue'],
		'fResCol'  : msg['Errors']['Field_FirstCol'],
		'col2Ext'  : msg['Errors']['Field_ColExtract'],
		'NoPeptide': msg['Errors']['NoPeptide'],
	},
	tabName['gene'] : {
		'iFile'    : msg['Errors']['FastaFile'],
		'gFile'    : msg['Errors']['GeneFile'],
		'oFile'    : msg['Errors']['OutFileTxt'],
		'r2extract': msg['Errors']['Field_Res2Extract'],
		'noGene'   : msg['Errors']['NoGene'],
		'noProt'   : msg['Errors']['NoProt'],
	},
	tabName['seqset'] : {
		'iFile': msg['Errors']['FastaFile'],
		'oFile': msg['Errors']['OutFileTxt'],
		'PosAA': msg['Errors']['PosAAs'],
		'NoSeq': msg['Errors']['NoSeq'],
	},
	winName['confSearch'] : {
		'NRes' : msg['Errors']['NRes'],
	},
}

dictKey = { # Label for widgets in the windows
	winName['confSearch'] : {
		'PosKey' : 'Pos',
	},
}

dataFrame = {
	'Header' : {
		tabName['seqset'] : [
			'Sequence', 
			'Appearance', 
			'%_AP',
			'%_TP',
			'Prot_IDs',
		],
	},
}

helperDict = { # Helper dicts to pretty print Input Data in the output file
	tabName['pept'] : {
		'iFile'  : 'Data File',
		'oFile'  : 'Output File',
		'fRes'   : 'First Residue <=',
		'fResCol': 'Start Residue',
		'Col2Ext': 'Columns to Extract',
	},
	tabName['gene'] : {
		'iFile': 'Fasta File',
		'gFile': 'Gene File',
		'oFile': 'Output File',
		'r2ext': 'Residues to extract',
	},
	tabName['seqset'] : {
		'iFile'   : 'Fasta File',
		'oFile'   : 'Output File',
		'PosAA'   : 'Positions & AAs',
		'CompProt': 'Complete proteins',
	},
}

pointer = { # Pointer to methods in different classes to avoid repeating if 
			 # statements. This dict is filled in 
			 # PeptideSearch.PeptideSearchApp.AppInit
	'gmethods' : { # points to methods in gui.gui_methods module
		'WinCreate' : {}, # Methods to create a window
	},			 
}

naVals = [ # Possible NA values
	'N', 'n', 'No', 'NO', 'NA', ''
]

oneLetterAA = [ # AA one letter codes
	'A', 'I', 'L', 'V', 'M', 'F', 'W', 'Y', 'R', 'K', 'D', 'E', 'C', 'Q',
	'H', 'S', 'T', 'N', 'G', 'P'
]
