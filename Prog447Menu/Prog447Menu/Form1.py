
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class Form1(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._lblMessage = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # lblMessage
        # 
        self._lblMessage.Font = System.Drawing.Font("Microsoft Sans Serif", 25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._lblMessage.Location = System.Drawing.Point(54, 364)
        self._lblMessage.Name = "lblMessage"
        self._lblMessage.Size = System.Drawing.Size(443, 57)
        self._lblMessage.TabIndex = 0
        self._lblMessage.Text = "Hello, world!"
        self._lblMessage.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # Form1
        # 
        self.BackColor = System.Drawing.Color.BurlyWood
        self.ClientSize = System.Drawing.Size(543, 489)
        self.Controls.Add(self._lblMessage)
        self.Name = "Form1"
        self.Text = "Form1"
        self.ResumeLayout(False)

