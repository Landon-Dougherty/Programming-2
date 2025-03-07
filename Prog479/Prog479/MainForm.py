import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
        self.total = 0 
        self.test = True
    
    def InitializeComponent(self):
        self._panel1 = System.Windows.Forms.Panel()
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self._label7 = System.Windows.Forms.Label()
        self._label8 = System.Windows.Forms.Label()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._textBox3 = System.Windows.Forms.TextBox()
        self._textBox4 = System.Windows.Forms.TextBox()
        self._textBox5 = System.Windows.Forms.TextBox()
        self._textBox6 = System.Windows.Forms.TextBox()
        self._textBox7 = System.Windows.Forms.TextBox()
        self._textBox8 = System.Windows.Forms.TextBox()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._label9 = System.Windows.Forms.Label()
        self._button4 = System.Windows.Forms.Button()
        self._panel1.SuspendLayout()
        self.SuspendLayout()
        # 
        # panel1
        # 
        self._panel1.BackColor = System.Drawing.SystemColors.ButtonFace
        self._panel1.Controls.Add(self._button4)
        self._panel1.Controls.Add(self._label9)
        self._panel1.Controls.Add(self._textBox8)
        self._panel1.Controls.Add(self._textBox7)
        self._panel1.Controls.Add(self._textBox6)
        self._panel1.Controls.Add(self._textBox5)
        self._panel1.Controls.Add(self._textBox4)
        self._panel1.Controls.Add(self._textBox3)
        self._panel1.Controls.Add(self._textBox2)
        self._panel1.Controls.Add(self._textBox1)
        self._panel1.Controls.Add(self._label8)
        self._panel1.Controls.Add(self._label7)
        self._panel1.Controls.Add(self._label6)
        self._panel1.Controls.Add(self._label5)
        self._panel1.Controls.Add(self._label4)
        self._panel1.Controls.Add(self._label3)
        self._panel1.Controls.Add(self._label2)
        self._panel1.Controls.Add(self._label1)
        self._panel1.Location = System.Drawing.Point(34, 34)
        self._panel1.Name = "panel1"
        self._panel1.Size = System.Drawing.Size(493, 296)
        self._panel1.TabIndex = 0
        self._panel1.Paint += self.Panel1Paint
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.SystemColors.ButtonShadow
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 12.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(29, 24)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(100, 23)
        self._label1.TabIndex = 0
        self._label1.Text = "Name :"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.SystemColors.ButtonShadow
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 12.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(29, 83)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(100, 23)
        self._label2.TabIndex = 1
        self._label2.Text = "Company :"
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.SystemColors.ButtonShadow
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 12.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(29, 143)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(100, 23)
        self._label3.TabIndex = 2
        self._label3.Text = "Address :"
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.SystemColors.ButtonShadow
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 12.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(29, 209)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(100, 23)
        self._label4.TabIndex = 3
        self._label4.Text = "City :"
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.SystemColors.ButtonShadow
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 12.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(135, 109)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(100, 23)
        self._label5.TabIndex = 4
        self._label5.Text = "Email :"
        self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.SystemColors.ButtonShadow
        self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 12.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.Location = System.Drawing.Point(135, 47)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(100, 23)
        self._label6.TabIndex = 5
        self._label6.Text = "Phone :"
        self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label7
        # 
        self._label7.BackColor = System.Drawing.SystemColors.ButtonShadow
        self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 12.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label7.Location = System.Drawing.Point(135, 180)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(100, 23)
        self._label7.TabIndex = 6
        self._label7.Text = "State :"
        self._label7.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label8
        # 
        self._label8.BackColor = System.Drawing.SystemColors.ButtonShadow
        self._label8.Font = System.Drawing.Font("Microsoft Sans Serif", 12.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label8.Location = System.Drawing.Point(135, 229)
        self._label8.Name = "label8"
        self._label8.Size = System.Drawing.Size(100, 23)
        self._label8.TabIndex = 7
        self._label8.Text = "Zip : "
        self._label8.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # textBox1
        # 
        self._textBox1.BackColor = System.Drawing.Color.FromArgb(192, 255, 255)
        self._textBox1.Location = System.Drawing.Point(135, 24)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(299, 20)
        self._textBox1.TabIndex = 8
        # 
        # textBox2
        # 
        self._textBox2.BackColor = System.Drawing.Color.FromArgb(192, 255, 255)
        self._textBox2.Location = System.Drawing.Point(135, 86)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(299, 20)
        self._textBox2.TabIndex = 9
        # 
        # textBox3
        # 
        self._textBox3.BackColor = System.Drawing.Color.FromArgb(192, 255, 255)
        self._textBox3.Location = System.Drawing.Point(135, 146)
        self._textBox3.Name = "textBox3"
        self._textBox3.Size = System.Drawing.Size(299, 20)
        self._textBox3.TabIndex = 10
        # 
        # textBox4
        # 
        self._textBox4.BackColor = System.Drawing.Color.FromArgb(192, 255, 255)
        self._textBox4.Location = System.Drawing.Point(135, 206)
        self._textBox4.Name = "textBox4"
        self._textBox4.Size = System.Drawing.Size(299, 20)
        self._textBox4.TabIndex = 11
        # 
        # textBox5
        # 
        self._textBox5.BackColor = System.Drawing.Color.Wheat
        self._textBox5.Location = System.Drawing.Point(241, 50)
        self._textBox5.Name = "textBox5"
        self._textBox5.Size = System.Drawing.Size(221, 20)
        self._textBox5.TabIndex = 12
        # 
        # textBox6
        # 
        self._textBox6.BackColor = System.Drawing.Color.Wheat
        self._textBox6.Location = System.Drawing.Point(241, 109)
        self._textBox6.Name = "textBox6"
        self._textBox6.Size = System.Drawing.Size(221, 20)
        self._textBox6.TabIndex = 13
        # 
        # textBox7
        # 
        self._textBox7.BackColor = System.Drawing.Color.Wheat
        self._textBox7.Location = System.Drawing.Point(241, 183)
        self._textBox7.Name = "textBox7"
        self._textBox7.Size = System.Drawing.Size(221, 20)
        self._textBox7.TabIndex = 14
        # 
        # textBox8
        # 
        self._textBox8.BackColor = System.Drawing.Color.Wheat
        self._textBox8.Location = System.Drawing.Point(241, 229)
        self._textBox8.Name = "textBox8"
        self._textBox8.Size = System.Drawing.Size(221, 20)
        self._textBox8.TabIndex = 15
        # 
        # button1
        # 
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 17.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(34, 349)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(148, 63)
        self._button1.TabIndex = 1
        self._button1.Text = "Reset"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 17.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(188, 349)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(179, 63)
        self._button2.TabIndex = 2
        self._button2.Text = "Exit"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 10, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(373, 349)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(154, 63)
        self._button3.TabIndex = 3
        self._button3.Text = "Select Conference Options"
        self._button3.UseVisualStyleBackColor = True
        self._button3.Click += self.Button3Click
        # 
        # label9
        # 
        self._label9.BackColor = System.Drawing.Color.Purple
        self._label9.Font = System.Drawing.Font("Microsoft Sans Serif", 12.5, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label9.ForeColor = System.Drawing.Color.White
        self._label9.Location = System.Drawing.Point(219, 257)
        self._label9.Name = "label9"
        self._label9.Size = System.Drawing.Size(179, 36)
        self._label9.TabIndex = 16
        self._label9.Text = "Total : $"
        self._label9.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # button4
        # 
        self._button4.Font = System.Drawing.Font("Microsoft Sans Serif", 17.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button4.Location = System.Drawing.Point(29, 257)
        self._button4.Name = "button4"
        self._button4.Size = System.Drawing.Size(153, 36)
        self._button4.TabIndex = 4
        self._button4.Text = "Get Total:"
        self._button4.UseVisualStyleBackColor = True
        self._button4.Click += self.Button4Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.SystemColors.ButtonShadow
        self.ClientSize = System.Drawing.Size(560, 424)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._panel1)
        self.Name = "MainForm"
        self.Text = "Prog479"
        self.Load += self.MainFormLoad
        self._panel1.ResumeLayout(False)
        self._panel1.PerformLayout()
        self.ResumeLayout(False)


    def Button2Click(self, sender, e):
        Application.Exit()
        

    def Button1Click(self, sender, e):
        self._textBox1.Text = ""
        self._textBox2.Text = ""
        self._textBox3.Text = ""
        self._textBox4.Text = ""
        self._textBox5.Text = ""
        self._textBox6.Text = ""
        self._textBox7.Text = ""
        self._textBox8.Text = ""
        

    def Button3Click(self, sender, e):
        
        from Form1 import *
        form1 = Form1(self)
        form1.Show()
        self.Hide()

    def Panel1Paint(self, sender, e):
        pass

    def MainFormLoad(self, sender, e):
        pass

    def Button4Click(self, sender, e):
        self._label9.Text = "Your Total : $" + str(self.total)