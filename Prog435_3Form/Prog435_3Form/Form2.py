import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class Form2(Form):
    def __init__(self, parent):
        self.InitializeComponent()
        self.myparent = parent
    
    def InitializeComponent(self):
        self._panel1 = System.Windows.Forms.Panel()
        self._label1 = System.Windows.Forms.Label()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._panel2 = System.Windows.Forms.Panel()
        self._label4 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._button2 = System.Windows.Forms.Button()
        self._button1 = System.Windows.Forms.Button()
        self._label5 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self._panel1.SuspendLayout()
        self._panel2.SuspendLayout()
        self.SuspendLayout()
        # 
        # panel1
        # 
        self._panel1.BackColor = System.Drawing.SystemColors.ButtonHighlight
        self._panel1.Controls.Add(self._label6)
        self._panel1.Controls.Add(self._label5)
        self._panel1.Controls.Add(self._button2)
        self._panel1.Controls.Add(self._button1)
        self._panel1.Controls.Add(self._panel2)
        self._panel1.Controls.Add(self._textBox1)
        self._panel1.Controls.Add(self._label1)
        self._panel1.Location = System.Drawing.Point(45, 25)
        self._panel1.Name = "panel1"
        self._panel1.Size = System.Drawing.Size(524, 383)
        self._panel1.TabIndex = 0
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.BlanchedAlmond
        self._label1.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 12.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(3, 33)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(158, 23)
        self._label1.TabIndex = 0
        self._label1.Text = "How Many Tickets?"
        # 
        # textBox1
        # 
        self._textBox1.BackColor = System.Drawing.Color.Wheat
        self._textBox1.Location = System.Drawing.Point(167, 33)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(331, 20)
        self._textBox1.TabIndex = 3
        # 
        # panel2
        # 
        self._panel2.BackColor = System.Drawing.Color.BurlyWood
        self._panel2.Controls.Add(self._label4)
        self._panel2.Controls.Add(self._label3)
        self._panel2.Controls.Add(self._label2)
        self._panel2.Location = System.Drawing.Point(167, 116)
        self._panel2.Name = "panel2"
        self._panel2.Size = System.Drawing.Size(213, 230)
        self._panel2.TabIndex = 4
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.BlanchedAlmond
        self._label4.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 12.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(18, 154)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(177, 38)
        self._label4.TabIndex = 9
        self._label4.Text = "Total : "
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.BlanchedAlmond
        self._label3.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 12.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(36, 91)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(137, 23)
        self._label3.TabIndex = 8
        self._label3.Text = "Tax % :"
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.BlanchedAlmond
        self._label2.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 12.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(36, 38)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(137, 23)
        self._label2.TabIndex = 5
        self._label2.Text = "Ticket Cost :"
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.BurlyWood
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 12.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(335, 70)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(119, 40)
        self._button2.TabIndex = 6
        self._button2.Text = "EXIT"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.BurlyWood
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 12.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(82, 70)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(119, 40)
        self._button1.TabIndex = 5
        self._button1.Text = "Calc"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.BlanchedAlmond
        self._label5.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 12.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(12, 185)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(137, 85)
        self._label5.TabIndex = 10
        self._label5.Text = "Student tickets is for seating in the student section only."
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.Color.BlanchedAlmond
        self._label6.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 12.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.Location = System.Drawing.Point(384, 185)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(137, 85)
        self._label6.TabIndex = 11
        self._label6.Text = "Student tickets is for seating in the student section only."
        # 
        # Form1
        # 
        self.BackColor = System.Drawing.SystemColors.ButtonShadow
        self.ClientSize = System.Drawing.Size(622, 445)
        self.Controls.Add(self._panel1)
        self.Name = "Form1"
        self.Text = "Prog435_3Form"
        self._panel1.ResumeLayout(False)
        self._panel1.PerformLayout()
        self._panel2.ResumeLayout(False)
        self.ResumeLayout(False)




       

    def Button1Click(self, sender, e):
        TC = 7 
        self._label2.Text = "Ticket Cost : " + str(TC)
        self._label3.Text = "Tax % : 0.06"
        self._label4.Text = "Total : " + str(int(TC * int(self._textBox1.Text)))

    def Button2Click(self, sender, e):
        Application.Exit()