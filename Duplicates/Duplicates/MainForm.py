import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._label1 = System.Windows.Forms.Label()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._button2 = System.Windows.Forms.Button()
        self._button1 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.SystemColors.ActiveCaption
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(34, 67)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(258, 46)
        self._label1.TabIndex = 0
        self._label1.Text = "Enter Text:"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 17, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(298, 75)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(343, 33)
        self._textBox1.TabIndex = 1
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.SystemColors.ActiveCaption
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(34, 199)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(258, 46)
        self._label2.TabIndex = 2
        self._label2.Text = "Duplicates :"
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.SystemColors.ActiveBorder
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(298, 199)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(343, 46)
        self._label3.TabIndex = 3
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.Wheat
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 17.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(21, 294)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(288, 164)
        self._button2.TabIndex = 4
        self._button2.Text = "Exit"
        self._button2.UseVisualStyleBackColor = False
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.Wheat
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 17.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(454, 294)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(288, 164)
        self._button1.TabIndex = 5
        self._button1.Text = "Calc"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.Wheat
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 17.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(239, 367)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(288, 164)
        self._button3.TabIndex = 6
        self._button3.Text = "Clear"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.Orange
        self.ClientSize = System.Drawing.Size(767, 543)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "Duplicates"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button3Click(self, sender, e):
        self._label3.Text = ""
        self._textBox1.Text = ""

    def Button1Click(self, sender, e):
        self._label3.Text = ""
        myStr = self._textBox1.Text.lower()
        for lcv in range(len(myStr)):
            for lcv2 in range(lcv+1, len(myStr)):
                ltr1 = myStr[lcv]
                ltr2 = myStr[lcv2]
                if ltr1 == ltr2:
                    self._label3.Text += ltr2 + " " 
        pass