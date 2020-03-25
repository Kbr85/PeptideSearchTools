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


""" This module creates the window to show the Help """


#--- Imports
import wx

import config.config as config
import menu.menu as menu
from gui.win.win_base_help import HelpWinBase
#---

class HelpWin(HelpWinBase):
	""" Creates the window to show the Help """

	def __init__(self, parent=None):
		"""  """

	 #--> Initial Setup
		self.nameWin = config.winName['help']
		super().__init__(None)
	 #---
	 #--> Add Lic Agreement Text
		self.MyText.AppendText(HelpText)
		self.MyText.SetInsertionPoint(0)
	 #---
	 #--> Show 		
		self.Show()
	 #---
	#---
#---


HelpText = """#### Brief Description of Peptide Search Tools 1.0 ####

Peptide Search Tools v1.0 is designed as a Notebook in which each page gives 
access to a specific functionality. The main objective is to search for peptide
sequences in different files with various search criteria.

## The Peptide.txt Page ##

This page allows to extract all N-terminal peptides found in a Maxquant 
peptide.txt file. In general, any file with tab separated columns and column 
names in the first row can be correctly searched. 

All fields in the page must be filled before starting the search. Initial guess 
values are given for the last three fields.

--------------------------------------------------------------------------------
	When giving the number of a column in the Data File, users must remember 
	that column’s numbers start in 0 not in 1. Thus, a column showing the 
	number 18 in Excel will be column 17 in Peptide Search Tools v1.0.                                                                                 
--------------------------------------------------------------------------------

- The Data File button allows to browse the file system to select the input 
	file. Only files with txt extension can be selected.
- The Output File button allows to browse the file system to select the output 
	file. Only files with txt extension can be selected.
- The field First Residue <= allows to specify a residue number. Peptides for 
	which the residue number of the first residue is lower or equal to the 
	specified number will be extracted from the Data File and saved in the 
	Output File. Only an integer greater than zero can be accepted here.
- The field Start Residue allows to specify the column in the Data File with
	the residue number of the first residue of the detected sequences. Only an 
	integer greater or equal than zero can be accepted here.
- The field Columns to Extract allows to specify the columns in the Data File 
	that will be extracted. Only a list of unique integers greater or equal than
	zero can be accepted here, e.g. 0 1 2 6 34 50.

The Output file will be a plain text file with a format similar to the given 
Data file. Only the specified Columns to Extract will be included in the 
Output file and columns will be tab separated. The file will have two section.
The first section (Input Data) will list the given search options. The second 
section contains the output data.

The first row in the Output Data section will have the name of the extracted 
columns. The other rows will contain sequences from the Data file for which the 
residue number of the first residue is equal or lower than the specified First 
Residue <= value. 

## The Genes.fasta Page ##

This page allows to extract the N-terminal sequences, up to a user defined 
length, of all proteins present in a multisequence fasta formated file that 
belong to a list of user defined genes. 

All fields in the page must be filled before starting the analysis.
Initial guess values are given for the last field.

- The Fasta File button allows to browse the file system to select a fasta 
	formated file containing multiple protein sequences. Only files with txt or 
	fasta extension can be selected.
- The Genes File button allows to browse the file system to select a plain text 
	file containing a list of genes. Only files with txt extension ca be 
	selected. This file must contain a gene per line, for example:

	NME6
	TRIM17
	KLC2
	PRKN
	POTEJ
	P3H3

- The Output File button allows to browse the file system to select the Output 
	file. Only files with txt extension can be selected.
- The Residue to Extract field allows to a specify the length of the N-terminal 
	peptides that will be extracted. Only a list of unique integers greater than
	zero can be accepted here, e.g. 5 10 25 50 100.

The Output file will be a plain text file with two sections. The first section 
(Input Data) will list the given search options. The second section contains the
output data.

The first row of the second section will have the name of the columns and the 
rest of the rows will be the identified proteins belonging to the given genes
with the peptide sequences.

## The Consensus Page ##

This page allows to search a multifasta file for a given set of consensus
sequences. The set of consensus sequences can be search for in a given set of
residue numbers or in the whole sequence of the proteins. Read below for more 
details. 

--------------------------------------------------------------------------------
	The Page assumes that the multifasta file follow the format of Uniprot 
	for fasta files
--------------------------------------------------------------------------------

All fields in the page must be filled before starting the analysis. Initial 
guess values are given for the last two fields.

- The Fasta File button allows to browse the file system to select a fasta 
	formated file containing multiple protein sequences. Only files with txt or 
	fasta extension can be selected.
- The Output File button allows to browse the file system to select the Output 
	file. Only files with txt extension can be selected.
- The Positions & AAs field allows to specify the positions and the amino acids
	in the consensus sequence. This field is not meant to be filled by hand.
	To input the values use the Configure button at the right side of the field.
- The Only complete proteins checkbox allows to select whether to consider all
	sequences in the multifasta file (unchecked state) or only the sequences of
	complete proteins (checked state).

The Configure button at the right side of the Poistions & AAs field opens a new 
window where the amino acids in the consensus sequence and the residue numbers 
can be specified. The use of the window is straightforward. Type the total 
number of residues in the consensus sequence and then press the button Create
matrix. The appropiate number of fields for the Residue number and AA in the 
consensus sequence will appear. 

The expected input in the fields Residue number is the residue number of the 
corresponding amino acid in the consensus sequence. Thus, only an integer 
greater than zero will be accepted here. The expected input in the fields 
Amino acids is a space separated list of amino acids (one letter code).
The amino acid fields cannot be empty but the Residue numbers can be left empty.

If the Residue numbers are left empty, then the consensus sequences formed by 
the combination of the Amino acids lists will be searched for in the entire 
sequence of the proteins in the multifasta file. If the Residue numbers are 
given, then the search is restricted to amino acids in these positions for the 
sequence of the proteins in the multifasta file.

The Residue numbers are not expected to be continuous, meaning that the 
consensus sequences can be searched for in residues 3, 4, 10, 11 and 20. 
However, when the Residue numbers are left empty the resulting consensus
sequences will be assumed to be continuous. 

Special care must be taken with incomplete sequences when dealing with a 
multifasta file automatically generated. The UniProt convention is to mark these
sequences with the word Fragment in the header section and the presence or 
absence of this word is what it is used to exclude incomplete sequences from the
analysis. If all proteins are to be included in the analysis it is important to 
be aware that for incomplete sequences:
- there is no way to know the actual residue numbers
- there is no way to know if there are gaps between adjacent residues in the 
	sequence 
Therefore, including incomplete sequences in the analysis should be done only in
very specific situations, e.g. manually curated multifasta file.  

The Output file will be a plain text file with two sections. The first section 
(Input Data) will list the given search options. The second section contains the
Output data.	

The information in the Output data section includes the total number of proteins
in the multifasta file, the total number of complete proteins, the total number
of times that the consensus sequences were found in absolute number and as 
percent of the total proteins and total complete proteins.

The last part of the section shows a detailed information about each sequence
in the consensus set including the number of times the sequence appears in the 
protein sequences, percents and the protein IDs where the sequences were found."""
