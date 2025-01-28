import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._textBox1 = System.Windows.Forms.TextBox()
        self._label1 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 12.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(242, 54)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(100, 26)
        self._textBox1.TabIndex = 0
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.SystemColors.ActiveBorder
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 21.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(137, 9)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(317, 42)
        self._label1.TabIndex = 1
        self._label1.Text = "Enter Radius"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.DarkGray
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 17.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(12, 102)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(140, 83)
        self._button1.TabIndex = 2
        self._button1.Text = "Calc"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.DarkGray
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 17.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(218, 102)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(140, 83)
        self._button2.TabIndex = 3
        self._button2.Text = "leave."
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.DarkGray
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 17.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(414, 102)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(140, 83)
        self._button3.TabIndex = 4
        self._button3.Text = "Clear"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.SystemColors.ActiveBorder
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 21.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(12, 248)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(542, 42)
        self._label2.TabIndex = 5
        self._label2.Text = "Area = "
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.SystemColors.ActiveBorder
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 21.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(12, 306)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(542, 42)
        self._label3.TabIndex = 6
        self._label3.Text = "Circumference ="
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.SystemColors.ActiveBorder
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 21.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(12, 369)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(542, 42)
        self._label4.TabIndex = 7
        self._label4.Text = "Radius ="
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.SystemColors.ControlDarkDark
        self.ClientSize = System.Drawing.Size(591, 466)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._textBox1)
        self.Name = "MainForm"
        self.Text = "Prog54c"
        self.Load += self.MainFormLoad
        self.ResumeLayout(False)
        self.PerformLayout()


    def MainFormLoad(self, sender, e):
        pass


    def Button2Click(self, sender, e):
        Application.Exit()
        

    def Button3Click(self, sender, e): #Clear Button
        self._textBox1.Text = ""
        self._label2.Text = "Area = "
        self._label3.Text = "Circumference = "
        self._label4.Text = "Radius = "
        

    def Button1Click(self, sender, e):
        radius = int(self._textBox1.Text)
        pi = 3.14159
        circ = round(2 * pi * radius,3)
        area = round(pi * (radius ** 2),3)
        self._label2.Text = "Area = " + str(area)
        self._label3.Text = "Circumference = " + str(circ)
        self._label4.Text = "Radius = " + str(radius)