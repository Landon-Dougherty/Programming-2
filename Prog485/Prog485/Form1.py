import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class Form1(Form):
    def __init__(self, parent):
        self.InitializeComponent()
        self.myparent = parent

        
    
    def InitializeComponent(self):
        self._label1 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 12.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(93, 114)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(246, 92)
        self._label1.TabIndex = 0
        self._label1.Text = "Your Total : $"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # Form1
        # 
        self.BackColor = System.Drawing.SystemColors.ButtonHighlight
        self.ClientSize = System.Drawing.Size(459, 342)
        self.Controls.Add(self._label1)
        self.Name = "Form1"
        self.Text = "Form1"
        self.Load += self.Form1Load
        self.ResumeLayout(False)
        
        


    def Form1Load(self, sender, e):
        total = self.myparent.total
        self._label1.Text = str(total)