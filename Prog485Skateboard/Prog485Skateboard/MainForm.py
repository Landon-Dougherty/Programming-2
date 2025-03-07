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
        self._panel1 = System.Windows.Forms.Panel()
        self._panel2 = System.Windows.Forms.Panel()
        self._panel3 = System.Windows.Forms.Panel()
        self._panel4 = System.Windows.Forms.Panel()
        self._MTButton = System.Windows.Forms.RadioButton()
        self._DGButton = System.Windows.Forms.RadioButton()
        self._SKButton = System.Windows.Forms.RadioButton()
        self._label3 = System.Windows.Forms.Label()
        self._button25 = System.Windows.Forms.RadioButton()
        self._button32 = System.Windows.Forms.RadioButton()
        self._button27 = System.Windows.Forms.RadioButton()
        self._label4 = System.Windows.Forms.Label()
        self._buttonNatural = System.Windows.Forms.RadioButton()
        self._label5 = System.Windows.Forms.Label()
        self._buttonBlue = System.Windows.Forms.RadioButton()
        self._buttonTeal = System.Windows.Forms.RadioButton()
        self._buttonRed = System.Windows.Forms.RadioButton()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._label2 = System.Windows.Forms.Label()
        self._radioButton1 = System.Windows.Forms.RadioButton()
        self._radioButton2 = System.Windows.Forms.RadioButton()
        self._radioButton3 = System.Windows.Forms.RadioButton()
        self._radioButton4 = System.Windows.Forms.RadioButton()
        self._radioButton5 = System.Windows.Forms.RadioButton()
        self._panel1.SuspendLayout()
        self._panel2.SuspendLayout()
        self._panel3.SuspendLayout()
        self._panel4.SuspendLayout()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.SystemColors.ButtonFace
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 9, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(12, 9)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(288, 23)
        self._label1.TabIndex = 0
        self._label1.Text = "Select The Purchases You Would Like To Make"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # panel1
        # 
        self._panel1.BackColor = System.Drawing.SystemColors.ButtonHighlight
        self._panel1.Controls.Add(self._SKButton)
        self._panel1.Controls.Add(self._DGButton)
        self._panel1.Controls.Add(self._MTButton)
        self._panel1.Location = System.Drawing.Point(12, 91)
        self._panel1.Name = "panel1"
        self._panel1.Size = System.Drawing.Size(288, 178)
        self._panel1.TabIndex = 2
        # 
        # panel2
        # 
        self._panel2.BackColor = System.Drawing.SystemColors.ButtonHighlight
        self._panel2.Controls.Add(self._button32)
        self._panel2.Controls.Add(self._button25)
        self._panel2.Controls.Add(self._button27)
        self._panel2.Location = System.Drawing.Point(352, 91)
        self._panel2.Name = "panel2"
        self._panel2.Size = System.Drawing.Size(288, 178)
        self._panel2.TabIndex = 3
        # 
        # panel3
        # 
        self._panel3.BackColor = System.Drawing.SystemColors.ButtonHighlight
        self._panel3.Controls.Add(self._radioButton5)
        self._panel3.Controls.Add(self._radioButton4)
        self._panel3.Controls.Add(self._radioButton3)
        self._panel3.Controls.Add(self._radioButton2)
        self._panel3.Controls.Add(self._radioButton1)
        self._panel3.Location = System.Drawing.Point(352, 302)
        self._panel3.Name = "panel3"
        self._panel3.Size = System.Drawing.Size(288, 175)
        self._panel3.TabIndex = 5
        # 
        # panel4
        # 
        self._panel4.BackColor = System.Drawing.SystemColors.ButtonHighlight
        self._panel4.Controls.Add(self._buttonRed)
        self._panel4.Controls.Add(self._buttonTeal)
        self._panel4.Controls.Add(self._buttonBlue)
        self._panel4.Controls.Add(self._buttonNatural)
        self._panel4.Location = System.Drawing.Point(12, 302)
        self._panel4.Name = "panel4"
        self._panel4.Size = System.Drawing.Size(288, 175)
        self._panel4.TabIndex = 4
        # 
        # MTButton
        # 
        self._MTButton.Font = System.Drawing.Font("Microsoft Sans Serif", 12.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._MTButton.Location = System.Drawing.Point(10, 12)
        self._MTButton.Name = "MTButton"
        self._MTButton.Size = System.Drawing.Size(262, 49)
        self._MTButton.TabIndex = 0
        self._MTButton.TabStop = True
        self._MTButton.Text = "Master Thrasher --> $60"
        self._MTButton.UseVisualStyleBackColor = True
        # 
        # DGButton
        # 
        self._DGButton.Font = System.Drawing.Font("Microsoft Sans Serif", 12.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._DGButton.Location = System.Drawing.Point(10, 67)
        self._DGButton.Name = "DGButton"
        self._DGButton.Size = System.Drawing.Size(262, 49)
        self._DGButton.TabIndex = 1
        self._DGButton.TabStop = True
        self._DGButton.Text = """Dictator of Grinding--> $45
"""
        self._DGButton.UseVisualStyleBackColor = True
        # 
        # SKButton
        # 
        self._SKButton.Font = System.Drawing.Font("Microsoft Sans Serif", 12.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._SKButton.Location = System.Drawing.Point(10, 122)
        self._SKButton.Name = "SKButton"
        self._SKButton.Size = System.Drawing.Size(262, 49)
        self._SKButton.TabIndex = 2
        self._SKButton.TabStop = True
        self._SKButton.Text = "Street King --> $50"
        self._SKButton.UseVisualStyleBackColor = True
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.SystemColors.ButtonFace
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 9, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(12, 65)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(288, 23)
        self._label3.TabIndex = 6
        self._label3.Text = "Select Deck:"
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # button25
        # 
        self._button25.Font = System.Drawing.Font("Microsoft Sans Serif", 12.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button25.Location = System.Drawing.Point(23, 32)
        self._button25.Name = "button25"
        self._button25.Size = System.Drawing.Size(262, 34)
        self._button25.TabIndex = 3
        self._button25.TabStop = True
        self._button25.Text = "7.75 --> $35"
        self._button25.UseVisualStyleBackColor = True
        # 
        # button32
        # 
        self._button32.Font = System.Drawing.Font("Microsoft Sans Serif", 12.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button32.Location = System.Drawing.Point(23, 112)
        self._button32.Name = "button32"
        self._button32.Size = System.Drawing.Size(262, 34)
        self._button32.TabIndex = 5
        self._button32.TabStop = True
        self._button32.Text = "8.5 --> $45"
        self._button32.UseVisualStyleBackColor = True
        # 
        # button27
        # 
        self._button27.Font = System.Drawing.Font("Microsoft Sans Serif", 12.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button27.Location = System.Drawing.Point(23, 72)
        self._button27.Name = "button27"
        self._button27.Size = System.Drawing.Size(262, 34)
        self._button27.TabIndex = 4
        self._button27.TabStop = True
        self._button27.Text = "8  --> $40"
        self._button27.UseVisualStyleBackColor = True
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.SystemColors.ButtonFace
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 9, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(352, 65)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(288, 23)
        self._label4.TabIndex = 7
        self._label4.Text = "Select Truck Assemblies:"
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # buttonNatural
        # 
        self._buttonNatural.Font = System.Drawing.Font("Microsoft Sans Serif", 12.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._buttonNatural.Location = System.Drawing.Point(10, 28)
        self._buttonNatural.Name = "buttonNatural"
        self._buttonNatural.Size = System.Drawing.Size(262, 23)
        self._buttonNatural.TabIndex = 7
        self._buttonNatural.TabStop = True
        self._buttonNatural.Text = "51 mm --> $20"
        self._buttonNatural.UseVisualStyleBackColor = True
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.SystemColors.ButtonFace
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 9, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(12, 276)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(288, 23)
        self._label5.TabIndex = 8
        self._label5.Text = "Select Wheel Set:"
        self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # buttonBlue
        # 
        self._buttonBlue.Font = System.Drawing.Font("Microsoft Sans Serif", 12.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._buttonBlue.Location = System.Drawing.Point(10, 57)
        self._buttonBlue.Name = "buttonBlue"
        self._buttonBlue.Size = System.Drawing.Size(262, 23)
        self._buttonBlue.TabIndex = 8
        self._buttonBlue.TabStop = True
        self._buttonBlue.Text = "55 mm --> $22"
        self._buttonBlue.UseVisualStyleBackColor = True
        # 
        # buttonTeal
        # 
        self._buttonTeal.Font = System.Drawing.Font("Microsoft Sans Serif", 12.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._buttonTeal.Location = System.Drawing.Point(10, 87)
        self._buttonTeal.Name = "buttonTeal"
        self._buttonTeal.Size = System.Drawing.Size(262, 23)
        self._buttonTeal.TabIndex = 9
        self._buttonTeal.TabStop = True
        self._buttonTeal.Text = "58 mm --> $24"
        self._buttonTeal.UseVisualStyleBackColor = True
        # 
        # buttonRed
        # 
        self._buttonRed.Font = System.Drawing.Font("Microsoft Sans Serif", 12.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._buttonRed.Location = System.Drawing.Point(10, 118)
        self._buttonRed.Name = "buttonRed"
        self._buttonRed.Size = System.Drawing.Size(262, 23)
        self._buttonRed.TabIndex = 10
        self._buttonRed.TabStop = True
        self._buttonRed.Text = "61 mm --> $28"
        self._buttonRed.UseVisualStyleBackColor = True
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.AntiqueWhite
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 12.5, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(426, 483)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(151, 46)
        self._button1.TabIndex = 2
        self._button1.Text = "Click For Total"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.AntiqueWhite
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 17.5, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(36, 483)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(196, 60)
        self._button2.TabIndex = 3
        self._button2.Text = "Exit"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.SystemColors.ButtonFace
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 9, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(352, 276)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(288, 23)
        self._label2.TabIndex = 9
        self._label2.Text = "Select Misc Items:"
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # radioButton1
        # 
        self._radioButton1.Font = System.Drawing.Font("Microsoft Sans Serif", 12.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton1.Location = System.Drawing.Point(3, 12)
        self._radioButton1.Name = "radioButton1"
        self._radioButton1.Size = System.Drawing.Size(262, 23)
        self._radioButton1.TabIndex = 11
        self._radioButton1.TabStop = True
        self._radioButton1.Text = "Grip Tape --> $10"
        self._radioButton1.UseVisualStyleBackColor = True
        # 
        # radioButton2
        # 
        self._radioButton2.Font = System.Drawing.Font("Microsoft Sans Serif", 12.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton2.Location = System.Drawing.Point(3, 41)
        self._radioButton2.Name = "radioButton2"
        self._radioButton2.Size = System.Drawing.Size(262, 23)
        self._radioButton2.TabIndex = 12
        self._radioButton2.TabStop = True
        self._radioButton2.Text = "Bearings --> $30"
        self._radioButton2.UseVisualStyleBackColor = True
        # 
        # radioButton3
        # 
        self._radioButton3.Font = System.Drawing.Font("Microsoft Sans Serif", 12.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton3.Location = System.Drawing.Point(3, 70)
        self._radioButton3.Name = "radioButton3"
        self._radioButton3.Size = System.Drawing.Size(262, 23)
        self._radioButton3.TabIndex = 13
        self._radioButton3.TabStop = True
        self._radioButton3.Text = "Riser Pads --> $2"
        self._radioButton3.UseVisualStyleBackColor = True
        # 
        # radioButton4
        # 
        self._radioButton4.Font = System.Drawing.Font("Microsoft Sans Serif", 12.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton4.Location = System.Drawing.Point(3, 99)
        self._radioButton4.Name = "radioButton4"
        self._radioButton4.Size = System.Drawing.Size(262, 23)
        self._radioButton4.TabIndex = 14
        self._radioButton4.TabStop = True
        self._radioButton4.Text = "Nuts and Bolts Kit --> $3"
        self._radioButton4.UseVisualStyleBackColor = True
        # 
        # radioButton5
        # 
        self._radioButton5.Font = System.Drawing.Font("Microsoft Sans Serif", 12.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton5.Location = System.Drawing.Point(3, 128)
        self._radioButton5.Name = "radioButton5"
        self._radioButton5.Size = System.Drawing.Size(262, 23)
        self._radioButton5.TabIndex = 15
        self._radioButton5.TabStop = True
        self._radioButton5.Text = "Assembly --> $10"
        self._radioButton5.UseVisualStyleBackColor = True
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.SystemColors.ButtonShadow
        self.ClientSize = System.Drawing.Size(661, 541)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._panel3)
        self.Controls.Add(self._panel4)
        self.Controls.Add(self._panel2)
        self.Controls.Add(self._panel1)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "Prog485"
        self._panel1.ResumeLayout(False)
        self._panel2.ResumeLayout(False)
        self._panel3.ResumeLayout(False)
        self._panel4.ResumeLayout(False)
        self.ResumeLayout(False)



    def Button1Click(self, sender, e):
        total = self.total
        if self._MTButton.Checked:
            total += 60
        elif self._DGButton.Checked:
            total += 45
        else:
            total += 50
            
        if self._button25.Checked:
            total += 35
        elif self._button27.Checked:
            total += 40
        else:
            total += 45
          
        if self._buttonNatural.Checked:
            total += 20
        elif self._buttonBlue.Checked:
            total += 22
        elif self._buttonTeal.Checked:
            total += 24
        elif self._buttonRed.Checked:
            total += 26
        
        if self._radioButton1.Checked:
            total += 10
        elif self._radioButton2.Checked:
            total += 30
        elif self._radioButton3.Checked:
            total +=2
        elif self._radioButton4.Checked:
            total +=3
        else:
            total += 30
        self.total = total
        from Form1 import * 
        form1 = Form1(self)
        form1.Show()
        self.Hide()

    def Button2Click(self, sender, e):
        Application.Exit()
