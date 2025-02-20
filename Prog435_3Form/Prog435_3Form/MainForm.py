
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.SystemColors.ButtonFace
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(69, 58)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(286, 139)
        self._label1.TabIndex = 0
        self._label1.Text = """Select General Sales for all ticket sales to the general public.
"""
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.SystemColors.ButtonFace
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(69, 226)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(286, 139)
        self._label2.TabIndex = 1
        self._label2.Text = "Select Student Sales for all student ticket sales."
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # button1
        # 
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 12.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(385, 58)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(164, 139)
        self._button1.TabIndex = 2
        self._button1.Text = "General Sales"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 12.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(385, 226)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(164, 139)
        self._button2.TabIndex = 3
        self._button2.Text = "Student Sales"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.SystemColors.ButtonShadow
        self.ClientSize = System.Drawing.Size(622, 445)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "Prog435_3Form"
        self.ResumeLayout(False)


    def Button1Click(self, sender, e):
        from Form1 import *     
        form1 = Form1(self)
        form1.Show()
        self.Hide()

    def Button2Click(self, sender, e):
        from Form2 import * 
        form2 = Form2(self)
        form2.Show()
        self.Hide()