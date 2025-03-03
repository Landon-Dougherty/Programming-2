import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self, parent):
        self.InitializeComponent()
        self.myparent = parent
    
    def InitializeComponent(self):
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
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
        self._button40 = System.Windows.Forms.RadioButton()
        self._label4 = System.Windows.Forms.Label()
        self._buttonNatural = System.Windows.Forms.RadioButton()
        self._label5 = System.Windows.Forms.Label()
        self._buttonBlue = System.Windows.Forms.RadioButton()
        self._buttonTeal = System.Windows.Forms.RadioButton()
        self._buttonRed = System.Windows.Forms.RadioButton()
        self._buttonGreen = System.Windows.Forms.RadioButton()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
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
        # label2
        # 
        self._label2.BackColor = System.Drawing.SystemColors.ButtonFace
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 9, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(27, 14)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(235, 23)
        self._label2.TabIndex = 1
        self._label2.Text = "Total : "
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
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
        self._panel2.Controls.Add(self._button40)
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
        self._panel3.Controls.Add(self._button1)
        self._panel3.Controls.Add(self._label2)
        self._panel3.Location = System.Drawing.Point(352, 302)
        self._panel3.Name = "panel3"
        self._panel3.Size = System.Drawing.Size(288, 175)
        self._panel3.TabIndex = 5
        # 
        # panel4
        # 
        self._panel4.BackColor = System.Drawing.SystemColors.ButtonHighlight
        self._panel4.Controls.Add(self._buttonGreen)
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
        self._MTButton.Text = "Regular Shades --> $0"
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
        self._DGButton.Text = "Folding Shades --> $10"
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
        self._SKButton.Text = "Shaded Shades --> $15"
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
        self._label3.Text = "Select Shades:"
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # button25
        # 
        self._button25.Font = System.Drawing.Font("Microsoft Sans Serif", 12.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button25.Location = System.Drawing.Point(17, 11)
        self._button25.Name = "button25"
        self._button25.Size = System.Drawing.Size(262, 34)
        self._button25.TabIndex = 3
        self._button25.TabStop = True
        self._button25.Text = "25in. Wide --> $0"
        self._button25.UseVisualStyleBackColor = True
        # 
        # button32
        # 
        self._button32.Font = System.Drawing.Font("Microsoft Sans Serif", 12.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button32.Location = System.Drawing.Point(17, 91)
        self._button32.Name = "button32"
        self._button32.Size = System.Drawing.Size(262, 34)
        self._button32.TabIndex = 5
        self._button32.TabStop = True
        self._button32.Text = "32in. Wide --> $4"
        self._button32.UseVisualStyleBackColor = True
        # 
        # button27
        # 
        self._button27.Font = System.Drawing.Font("Microsoft Sans Serif", 12.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button27.Location = System.Drawing.Point(17, 51)
        self._button27.Name = "button27"
        self._button27.Size = System.Drawing.Size(262, 34)
        self._button27.TabIndex = 4
        self._button27.TabStop = True
        self._button27.Text = "27in. Wide --> $2"
        self._button27.UseVisualStyleBackColor = True
        # 
        # button40
        # 
        self._button40.Font = System.Drawing.Font("Microsoft Sans Serif", 12.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button40.Location = System.Drawing.Point(16, 126)
        self._button40.Name = "button40"
        self._button40.Size = System.Drawing.Size(262, 34)
        self._button40.TabIndex = 6
        self._button40.TabStop = True
        self._button40.Text = "40in. Wide --> $6"
        self._button40.UseVisualStyleBackColor = True
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.SystemColors.ButtonFace
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 9, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(352, 65)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(288, 23)
        self._label4.TabIndex = 7
        self._label4.Text = "Select Deck : "
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # buttonNatural
        # 
        self._buttonNatural.Font = System.Drawing.Font("Microsoft Sans Serif", 12.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._buttonNatural.Location = System.Drawing.Point(10, 14)
        self._buttonNatural.Name = "buttonNatural"
        self._buttonNatural.Size = System.Drawing.Size(262, 23)
        self._buttonNatural.TabIndex = 7
        self._buttonNatural.TabStop = True
        self._buttonNatural.Text = "Natural --> $5"
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
        self._label5.Text = "Select Color:"
        self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # buttonBlue
        # 
        self._buttonBlue.Font = System.Drawing.Font("Microsoft Sans Serif", 12.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._buttonBlue.Location = System.Drawing.Point(10, 43)
        self._buttonBlue.Name = "buttonBlue"
        self._buttonBlue.Size = System.Drawing.Size(262, 23)
        self._buttonBlue.TabIndex = 8
        self._buttonBlue.TabStop = True
        self._buttonBlue.Text = "Blue --> $0"
        self._buttonBlue.UseVisualStyleBackColor = True
        # 
        # buttonTeal
        # 
        self._buttonTeal.Font = System.Drawing.Font("Microsoft Sans Serif", 12.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._buttonTeal.Location = System.Drawing.Point(10, 72)
        self._buttonTeal.Name = "buttonTeal"
        self._buttonTeal.Size = System.Drawing.Size(262, 23)
        self._buttonTeal.TabIndex = 9
        self._buttonTeal.TabStop = True
        self._buttonTeal.Text = "Teal --> $0"
        self._buttonTeal.UseVisualStyleBackColor = True
        # 
        # buttonRed
        # 
        self._buttonRed.Font = System.Drawing.Font("Microsoft Sans Serif", 12.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._buttonRed.Location = System.Drawing.Point(10, 101)
        self._buttonRed.Name = "buttonRed"
        self._buttonRed.Size = System.Drawing.Size(262, 23)
        self._buttonRed.TabIndex = 10
        self._buttonRed.TabStop = True
        self._buttonRed.Text = "Red --> $0"
        self._buttonRed.UseVisualStyleBackColor = True
        # 
        # buttonGreen
        # 
        self._buttonGreen.Font = System.Drawing.Font("Microsoft Sans Serif", 12.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._buttonGreen.Location = System.Drawing.Point(10, 130)
        self._buttonGreen.Name = "buttonGreen"
        self._buttonGreen.Size = System.Drawing.Size(262, 23)
        self._buttonGreen.TabIndex = 11
        self._buttonGreen.TabStop = True
        self._buttonGreen.Text = "Green --> $0"
        self._buttonGreen.UseVisualStyleBackColor = True
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.AntiqueWhite
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 17.5, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(27, 56)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(235, 82)
        self._button1.TabIndex = 2
        self._button1.Text = "Click For Total"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.AntiqueWhite
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 17.5, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(229, 481)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(196, 60)
        self._button2.TabIndex = 3
        self._button2.Text = "Exit"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.SystemColors.ButtonShadow
        self.ClientSize = System.Drawing.Size(661, 541)
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
        shadetype = 0.0
        shadelength = 0.0
        shadecolor = 0.0
        
        if self._MTButton.Checked == True:
            shadetype = 0.0
        elif self._DGButton.Checked == True:
            shadetype = 10.0
        else:
            shadetype = 15.0
            
        if self._button25.Checked == True:
            shadelength = 0.0
        elif self._button27.Checked == True:
            shadelength = 2.0
        elif self._button32.Checked == True:
            shadelength = 4.0
        else:
            shadelength = 6.0
          
        if self._buttonNatural.Checked == True:
            shadecolor = 5.0
        
        total = float(shadetype+shadelength+shadecolor)
        
        from Form1 import * 
        form1 = Form1(self)
        form1.Show()
        self.Hide()

    def Button2Click(self, sender, e):
        Application.Exit()