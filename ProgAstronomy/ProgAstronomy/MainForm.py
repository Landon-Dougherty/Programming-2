import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._label1 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.SystemColors.ButtonHighlight
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 12.5, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(137, 26)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(347, 51)
        self._label1.TabIndex = 0
        self._label1.Text = "Select A Planet With Buttons Because I Forgot How To Use A Combo Box!"
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.SystemColors.ButtonShadow
        self.ClientSize = System.Drawing.Size(651, 504)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "ProgAstronomy"
        self.ResumeLayout(False)

