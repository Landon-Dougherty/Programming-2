import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class Saturn(Form):
    def __init__(self, parent):
        self.InitializeComponent()
        self.myparent = parent
    
    def InitializeComponent(self):
        self._button1 = System.Windows.Forms.Button()
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.Location = System.Drawing.Point(140, 320)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(206, 86)
        self._button1.TabIndex = 0
        self._button1.Text = "Go Back"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.SystemColors.ButtonFace
        self._label1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 10, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(141, 24)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(206, 41)
        self._label1.TabIndex = 1
        self._label1.Text = "Type : Jovian"
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.SystemColors.ButtonFace
        self._label2.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 10, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(112, 127)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(253, 41)
        self._label2.TabIndex = 2
        self._label2.Text = """Average Distance From Sun : 9.5388 AU
"""
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.SystemColors.ButtonFace
        self._label3.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 10, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(252, 75)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(206, 41)
        self._label3.TabIndex = 3
        self._label3.Text = "Mass : 5.69 x 10^26"
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.SystemColors.ButtonFace
        self._label4.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 10, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(40, 75)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(206, 41)
        self._label4.TabIndex = 4
        self._label4.Text = "Surface Temp : -180 C"
        # 
        # Saturn
        # 
        self.BackColor = System.Drawing.SystemColors.ButtonShadow
        self.ClientSize = System.Drawing.Size(500, 430)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._button1)
        self.Name = "Saturn"
        self.Text = "Pluto"
        self.ResumeLayout(False)


    def Button1Click(self, sender, e):
        self.Hide()
        self.myparent.Show() 

