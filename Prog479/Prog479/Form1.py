
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class Form1(Form):
    def __init__(self, parent):
        self.InitializeComponent()
        self.myparent = parent
    
    def InitializeComponent(self):
        self._panel1 = System.Windows.Forms.Panel()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._checkBox1 = System.Windows.Forms.CheckBox()
        self._checkBox2 = System.Windows.Forms.CheckBox()
        self._panel2 = System.Windows.Forms.Panel()
        self._radioButton1 = System.Windows.Forms.RadioButton()
        self._radioButton2 = System.Windows.Forms.RadioButton()
        self._radioButton3 = System.Windows.Forms.RadioButton()
        self._radioButton4 = System.Windows.Forms.RadioButton()
        self._panel1.SuspendLayout()
        self._panel2.SuspendLayout()
        self.SuspendLayout()
        # 
        # panel1
        # 
        self._panel1.BackColor = System.Drawing.Color.BlanchedAlmond
        self._panel1.Controls.Add(self._panel2)
        self._panel1.Controls.Add(self._checkBox2)
        self._panel1.Controls.Add(self._checkBox1)
        self._panel1.Location = System.Drawing.Point(39, 24)
        self._panel1.Name = "panel1"
        self._panel1.Size = System.Drawing.Size(549, 314)
        self._panel1.TabIndex = 0
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.BlanchedAlmond
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 17.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(324, 344)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(129, 63)
        self._button1.TabIndex = 2
        self._button1.Text = "Reset"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.BlanchedAlmond
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 17.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(459, 344)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(129, 63)
        self._button2.TabIndex = 3
        self._button2.Text = "Close"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # checkBox1
        # 
        self._checkBox1.BackColor = System.Drawing.Color.BurlyWood
        self._checkBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 12.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._checkBox1.Location = System.Drawing.Point(22, 71)
        self._checkBox1.Name = "checkBox1"
        self._checkBox1.Size = System.Drawing.Size(253, 49)
        self._checkBox1.TabIndex = 0
        self._checkBox1.Text = "Conference Registration : $835"
        self._checkBox1.UseVisualStyleBackColor = False
        self._checkBox1.Click += self.CheckBox1Click
        # 
        # checkBox2
        # 
        self._checkBox2.BackColor = System.Drawing.Color.BurlyWood
        self._checkBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 12.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._checkBox2.Location = System.Drawing.Point(22, 167)
        self._checkBox2.Name = "checkBox2"
        self._checkBox2.Size = System.Drawing.Size(253, 49)
        self._checkBox2.TabIndex = 1
        self._checkBox2.Text = "Opening Night Dinner & Keynote: $30"
        self._checkBox2.UseVisualStyleBackColor = False
        # 
        # panel2
        # 
        self._panel2.BackColor = System.Drawing.Color.BurlyWood
        self._panel2.Controls.Add(self._radioButton4)
        self._panel2.Controls.Add(self._radioButton3)
        self._panel2.Controls.Add(self._radioButton2)
        self._panel2.Controls.Add(self._radioButton1)
        self._panel2.Location = System.Drawing.Point(285, 20)
        self._panel2.Name = "panel2"
        self._panel2.Size = System.Drawing.Size(242, 263)
        self._panel2.TabIndex = 2
        # 
        # radioButton1
        # 
        self._radioButton1.BackColor = System.Drawing.SystemColors.Window
        self._radioButton1.Font = System.Drawing.Font("Microsoft Sans Serif", 13.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton1.Location = System.Drawing.Point(15, 28)
        self._radioButton1.Name = "radioButton1"
        self._radioButton1.Size = System.Drawing.Size(210, 47)
        self._radioButton1.TabIndex = 0
        self._radioButton1.TabStop = True
        self._radioButton1.Text = "Intro To E-Commerce"
        self._radioButton1.UseVisualStyleBackColor = False
        # 
        # radioButton2
        # 
        self._radioButton2.BackColor = System.Drawing.SystemColors.Window
        self._radioButton2.Font = System.Drawing.Font("Microsoft Sans Serif", 11.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton2.Location = System.Drawing.Point(15, 81)
        self._radioButton2.Name = "radioButton2"
        self._radioButton2.Size = System.Drawing.Size(210, 47)
        self._radioButton2.TabIndex = 1
        self._radioButton2.TabStop = True
        self._radioButton2.Text = "The Future At The Web"
        self._radioButton2.UseVisualStyleBackColor = False
        # 
        # radioButton3
        # 
        self._radioButton3.BackColor = System.Drawing.SystemColors.Window
        self._radioButton3.Font = System.Drawing.Font("Microsoft Sans Serif", 12.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton3.Location = System.Drawing.Point(15, 134)
        self._radioButton3.Name = "radioButton3"
        self._radioButton3.Size = System.Drawing.Size(210, 47)
        self._radioButton3.TabIndex = 2
        self._radioButton3.TabStop = True
        self._radioButton3.Text = "Advanced Visual Basic"
        self._radioButton3.UseVisualStyleBackColor = False
        # 
        # radioButton4
        # 
        self._radioButton4.BackColor = System.Drawing.SystemColors.Window
        self._radioButton4.Font = System.Drawing.Font("Microsoft Sans Serif", 13.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton4.Location = System.Drawing.Point(15, 187)
        self._radioButton4.Name = "radioButton4"
        self._radioButton4.Size = System.Drawing.Size(210, 47)
        self._radioButton4.TabIndex = 3
        self._radioButton4.TabStop = True
        self._radioButton4.Text = "Network Security"
        self._radioButton4.UseVisualStyleBackColor = False
        # 
        # Form1
        # 
        self.BackColor = System.Drawing.Color.BurlyWood
        self.ClientSize = System.Drawing.Size(635, 438)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._panel1)
        self.Name = "Form1"
        self.Text = "Form1"
        self._panel1.ResumeLayout(False)
        self._panel2.ResumeLayout(False)
        self.ResumeLayout(False)

    def Button1Click(self, sender, e):
        self._checkBox1.Checked = False
        self._checkBox2.Checked = False
        

    def Button2Click(self, sender, e):
        if self._checkBox1.Checked == False:
            if self._radioButton1.Checked:
                MessageBox.Show("You Must Register Before Signing Up For A Program.")
                self._radioButton1.Checked = False
                
            if self._radioButton2.Checked:
                MessageBox.Show("You Must Register Before Signing Up For A Program.")
                self._radioButton2.Checked = False
                
            if self._radioButton3.Checked:
                MessageBox.Show("You Must Register Before Signing Up For A Program.")
                self._radioButton3.Checked = False
                
            if self._radioButton4.Checked:
                MessageBox.Show("You Must Register Before Signing Up For A Program.")
                self._radioButton4.Checked = False
        else:
            if self._checkBox1.Checked:
                self.myparent.total += 895
                if self._checkBox2.Checked:
                    self.myparent.total += 30
                    self.Hide()
                    self.myparent.Show()
                self.Hide()
                self.myparent.Show()

            

    def CheckBox1Click(self, sender, e):
        pass