# ------------------------------------------------------------------------------
# 	Copyright (C) 2019-2020 Kenny Bravo Rodriguez

# 	This program is distributed for free in the hope that it will be useful,
# 	but WITHOUT ANY WARRANTY; without even the implied warranty of
# 	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

# 	See the accompaning licence for more details.
# ------------------------------------------------------------------------------

""" This module creates the window to show the License Agreement """

#--- Imports
## Standard modules
import wx
## My modules
import config.config as config
import menu.menu as menu
from gui.win.win_base_help import HelpWinBase
#---

class LicAgreementWin(HelpWinBase):
	""" Creates the window to show the Lic. Agreement """

	def __init__(self, parent=None):
		"""  """

	 #--- Initial Setup
		self.nameWin = config.winName['licagr']
		super().__init__(None)
	 #--- Add Lic Agreement Text
		self.MyText.AppendText(LicAgreementText)
		self.MyText.SetInsertionPoint(0)
	 #--- Show 		
		self.Show()
	#---
#---

LicAgreementText = """## Copyright ##

Copyright © 2019-2020 Kenny Bravo Rodriguez. All rights reserved.

## License ##

Peptide Search Tools and its source code are governed by the following license:
Upon execution of this Agreement by the party identified below (”Licensee”), 
Kenny Bravo Rodriguez (KBR) will provide the Peptide Search Tools software in 
Executable Code and/or Source Code form (”Software”) to Licensee, subject to 
the following terms and conditions. 

For purposes of this Agreement, Executable Code is the compiled code, which is 
ready to run on Licensee’s computer. Source code consists of a set of files, 
which contain the actual program commands that are compiled to form the 
Executable Code.

1. The Software is intellectual property owned by KBR, and all rights, title 
and interest, including copyright, remain with KBR. KBR grants, and Licensee 
hereby accepts, a restricted, non-exclusive, non-transferable license to use 
the Software for academic, research and internal business purposes only, e.g. 
not for commercial use (see Clause 7 below), without a fee.

2. Licensee may, at its own expense, create and freely distribute complimentary
works that inter-operate with the Software, directing others to license and 
obtain the Software itself. Licensee may, at its own expense, modify the 
Software to make derivative works. Except as explicitly provided below, this 
License shall apply to any derivative work as it does to the original Software 
distributed by KBR. Any derivative work should be clearly marked and renamed to
notify users that it is a modified version and not the original Software 
distributed by KBR. Licensee agrees to reproduce the copyright notice and other
proprietary markings on any derivative work and to include in the documentation
of such work the acknowledgment: ”This software includes code developed by 
Kenny Bravo Rodriguez for the Peptide Search Tools software”. 

Licensee may not sell any derivative work based on the Software under any 
circumstance. For commercial distribution of the Software or any derivative work
based on the Software a separate license is required. Licensee may contact KBR 
to negotiate an appropriate license for such distribution.

3. Except as expressly set forth in this Agreement, 

THIS SOFTWARE IS PROVIDED "AS IS” AND KBR MAKES NO REPRESENTATIONS AND EXTENDS 
NO WARRANTIES OF ANY KIND, EITHER EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED
TO WARRANTIES OR MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE, OR THAT 
THE USE OF THE SOFTWARE WILL NOT INFRINGE ANY PATENT, TRADEMARK, OR OTHER 
RIGHTS. LICENSEE ASSUMES THE ENTIRE RISK AS TO THE RESULTS AND PERFORMANCE OF 
THE SOFTWARE AND/OR ASSOCIATED MATERIALS. LICENSEE AGREES THAT KBR SHALL NOT BE
HELD LIABLE FOR ANY DIRECT, INDIRECT, CONSE- QUENTIAL, OR INCIDENTAL DAMAGES 
WITH RESPECT TO ANY CLAIM BY LICENSEE OR ANY THIRD PARTY ON ACCOUNT OF OR 
ARISING FROM THIS AGREEMENT OR USE OF THE SOFTWARE AND/OR ASSOCIATED MATERIALS.

4. Licensee understands the Software is proprietary to KBR. Licensee agrees to 
take all reasonable steps to insure that the Software is protected and secured 
from unauthorized disclosure, use, or release and will treat it with at least 
the same level of care as Licensee would use to protect and secure its own 
proprietary computer programs and/or information, but using no less than a 
reasonable standard of care. Licensee agrees to provide the Software only to 
any other person or entity who has registered with KBR. If Licensee is not 
registering as an individual but as an institution or corporation each member 
of the institution or corporation who has access to or uses Software must agree 
to and abide by the terms of this license. If Licensee becomes aware of any 
unauthorized licensing, copying or use of the Software, Licensee shall promptly 
notify KBR in writing. Licensee expressly agrees to use the Software only in the
manner and for the specific uses authorized in this Agreement.

5. KBR shall have the right to terminate this license immediately by written 
notice upon Licensee’s breach of, or non-compliance with, any terms of the 
license. Licensee may be held legally responsible for any copyright infringement
that is caused or encouraged by its failure to abide by the terms of this 
license. Upon termination, Licensee agrees to destroy all copies of the 
Software in its possession and to verify such destruction in writing.

6. Licensee agrees that any reports or published results obtained with the 
Software will acknowledge its use by the appropriate citation as follows:
”Peptide Search Tools was developed by Kenny Bravo Rodriguez.”
Any published work, which utilizes Peptide Search Tools, shall include the following 
reference:
GITHUB ADDRESS
Electronic documents will include a direct link to the GitHub repository page:
GITHUB ADDRESS

7. Commercial use of the Software, or derivative works based thereon, REQUIRES 
A COMMERCIAL LICENSE. Should Licensee wish to make commercial use of the 
Software, Licensee will contact KBR to negotiate an appropriate license for such
use. Commercial use includes: (1) integration of all or part of the Software 
into a product for sale, lease or license by or on behalf of Licensee to third 
parties, or (2) distribution of the Software to third parties that need it to 
commercialize product sold or licensed by or on behalf of Licensee.

8. Peptide Search Tools is being distributed as a research tool and as such, KBR 
encourages contributions from users of the code that might, at KBR’s sole 
discretion, be used or incorporated to make the basic operating framework of the
Software a more stable, flexible, and/or useful product. Licensees who 
contribute their code to become an internal portion of the Software agree that 
such code may be distributed by KBR under the terms of this License and may be 
required to sign an ”Agreement Regarding Contributory Code for Peptide Search Tools 
Software” before KBR can accept it.

9. The use of the Software implies that Licensee read and accepted this License
Agreement."""
