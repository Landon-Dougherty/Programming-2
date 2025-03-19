import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
        self.total = 0
    
    def InitializeComponent(self):
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._panel1 = System.Windows.Forms.Panel()
        self._panel2 = System.Windows.Forms.Panel()
        self._radioButton1 = System.Windows.Forms.RadioButton()
        self._radioButton2 = System.Windows.Forms.RadioButton()
        self._radioButton3 = System.Windows.Forms.RadioButton()
        self._radioButton4 = System.Windows.Forms.RadioButton()
        self._radioButton5 = System.Windows.Forms.RadioButton()
        self._radioButton6 = System.Windows.Forms.RadioButton()
        self._radioButton7 = System.Windows.Forms.RadioButton()
        self._button1 = System.Windows.Forms.Button()
        self._panel1.SuspendLayout()
        self._panel2.SuspendLayout()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.SystemColors.ButtonHighlight
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 13, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(95, 46)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(176, 23)
        self._label1.TabIndex = 0
        self._label1.Text = "Select School :"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.SystemColors.ButtonHighlight
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 13, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(340, 46)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(176, 23)
        self._label2.TabIndex = 1
        self._label2.Text = "Select Meal Plan : "
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # panel1
        # 
        self._panel1.BackColor = System.Drawing.SystemColors.ButtonFace
        self._panel1.Controls.Add(self._radioButton3)
        self._panel1.Controls.Add(self._radioButton4)
        self._panel1.Controls.Add(self._radioButton2)
        self._panel1.Controls.Add(self._radioButton1)
        self._panel1.Location = System.Drawing.Point(87, 96)
        self._panel1.Name = "panel1"
        self._panel1.Size = System.Drawing.Size(214, 337)
        self._panel1.TabIndex = 2
        # 
        # panel2
        # 
        self._panel2.BackColor = System.Drawing.SystemColors.ButtonFace
        self._panel2.Controls.Add(self._radioButton7)
        self._panel2.Controls.Add(self._radioButton6)
        self._panel2.Controls.Add(self._radioButton5)
        self._panel2.Location = System.Drawing.Point(307, 96)
        self._panel2.Name = "panel2"
        self._panel2.Size = System.Drawing.Size(214, 337)
        self._panel2.TabIndex = 3
        # 
        # radioButton1
        # 
        self._radioButton1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton1.Location = System.Drawing.Point(2, 50)
        self._radioButton1.Name = "radioButton1"
        self._radioButton1.Size = System.Drawing.Size(203, 24)
        self._radioButton1.TabIndex = 0
        self._radioButton1.TabStop = True
        self._radioButton1.Text = """Allen Hall - $1,500 / Sem
"""
        self._radioButton1.UseVisualStyleBackColor = True
        self._radioButton1.CheckedChanged += self.RadioButton1CheckedChanged
        # 
        # radioButton2
        # 
        self._radioButton2.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton2.Location = System.Drawing.Point(3, 107)
        self._radioButton2.Name = "radioButton2"
        self._radioButton2.Size = System.Drawing.Size(203, 24)
        self._radioButton2.TabIndex = 1
        self._radioButton2.TabStop = True
        self._radioButton2.Text = "Pike Hall - $1,600 / Sem"
        self._radioButton2.UseVisualStyleBackColor = True
#        self._radioButton2.CheckedChanged += self.RadioButton2CheckedChanged
        # 
        # radioButton3
        # 
        self._radioButton3.Font = System.Drawing.Font("Microsoft Sans Serif", 9, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton3.Location = System.Drawing.Point(4, 234)
        self._radioButton3.Name = "radioButton3"
        self._radioButton3.Size = System.Drawing.Size(203, 24)
        self._radioButton3.TabIndex = 3
        self._radioButton3.TabStop = True
        self._radioButton3.Text = """University Suites - $1,800 / Sem
"""
        self._radioButton3.UseVisualStyleBackColor = True
        # 
        # radioButton4
        # 
        self._radioButton4.Font = System.Drawing.Font("Microsoft Sans Serif", 9, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton4.Location = System.Drawing.Point(3, 177)
        self._radioButton4.Name = "radioButton4"
        self._radioButton4.Size = System.Drawing.Size(203, 24)
        self._radioButton4.TabIndex = 2
        self._radioButton4.TabStop = True
        self._radioButton4.Text = """Farthing Hall - $1,200 / Sem
"""
        self._radioButton4.UseVisualStyleBackColor = True
        # 
        # radioButton5
        # 
        self._radioButton5.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton5.Location = System.Drawing.Point(6, 77)
        self._radioButton5.Name = "radioButton5"
        self._radioButton5.Size = System.Drawing.Size(203, 24)
        self._radioButton5.TabIndex = 4
        self._radioButton5.TabStop = True
        self._radioButton5.Text = "7 / Week - $560 / Sem"
        self._radioButton5.UseVisualStyleBackColor = True
        # 
        # radioButton6
        # 
        self._radioButton6.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton6.Location = System.Drawing.Point(6, 147)
        self._radioButton6.Name = "radioButton6"
        self._radioButton6.Size = System.Drawing.Size(203, 24)
        self._radioButton6.TabIndex = 5
        self._radioButton6.TabStop = True
        self._radioButton6.Text = "14 / Week - 1095$ / Sem"
        self._radioButton6.UseVisualStyleBackColor = True
        # 
        # radioButton7
        # 
        self._radioButton7.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton7.Location = System.Drawing.Point(6, 214)
        self._radioButton7.Name = "radioButton7"
        self._radioButton7.Size = System.Drawing.Size(203, 24)
        self._radioButton7.TabIndex = 6
        self._radioButton7.TabStop = True
        self._radioButton7.Text = "Unlimited - $1,500 / Sem"
        self._radioButton7.UseVisualStyleBackColor = True
        # 
        # button1
        # 
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(233, 439)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(138, 48)
        self._button1.TabIndex = 4
        self._button1.Text = "Total "
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.SystemColors.ButtonShadow
        self.ClientSize = System.Drawing.Size(631, 499)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._panel2)
        self.Controls.Add(self._panel1)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "Prog484"
        self._panel1.ResumeLayout(False)
        self._panel2.ResumeLayout(False)
        self.ResumeLayout(False)


    def RadioButton1CheckedChanged(self, sender, e):
        pass

    def Button1Click(self, sender, e):
        total = self.total 
        if self._radioButton1.Checked:
            total += 1500
        elif self._radioButton2.Checked:
            total += 1600
        elif self._radioButton3.Checked:
            total += 1200
        elif self._radioButton4.Checked:
            total += 1800
        else:
            pass
        
        if self._radioButton5.Checked:
            total += 560
            self.Hide()  
        elif self._radioButton6.Checked:
            total += 1095
            self.Hide()  
        elif self._radioButton7.Checked:
            total += 1500
        else:
            pass
        self.total = total
        from Form1 import * 
        form1 = Form1(self)
        form1.Show()
        self.Hide()
            
