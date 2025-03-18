from MainForm import *
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
        self._button1 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.CadetBlue
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 17.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(42, 39)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(240, 90)
        self._label1.TabIndex = 0
        self._label1.Text = "Total : "
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # button1
        # 
        self._button1.Location = System.Drawing.Point(123, 195)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(75, 23)
        self._button1.TabIndex = 1
        self._button1.Text = "Leave"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # Form1
        # 
        self.BackColor = System.Drawing.SystemColors.ButtonShadow
        self.ClientSize = System.Drawing.Size(324, 297)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label1)
        self.Name = "Form1"
        self.Text = "Form1"
        self.Load += self.Form1Load
        self.ResumeLayout(False)


    def Form1Load(self, sender, e):
        self._label1.Text = "Total : $" + str(self.myparent.total) + " / Sem"

    def Button1Click(self, sender, e):
        Application.Exit()