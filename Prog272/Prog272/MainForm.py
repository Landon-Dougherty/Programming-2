import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._button1 = System.Windows.Forms.Button()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._textBox3 = System.Windows.Forms.TextBox()
        self._button2 = System.Windows.Forms.Button()
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.Location = System.Drawing.Point(575, 12)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(64, 109)
        self._button1.TabIndex = 0
        self._button1.Text = "balkan master button (Clear)"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(233, 12)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(251, 30)
        self._textBox1.TabIndex = 1
        # 
        # textBox2
        # 
        self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.Location = System.Drawing.Point(233, 77)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(251, 30)
        self._textBox2.TabIndex = 2
        # 
        # textBox3
        # 
        self._textBox3.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox3.Location = System.Drawing.Point(233, 147)
        self._textBox3.Name = "textBox3"
        self._textBox3.Size = System.Drawing.Size(251, 30)
        self._textBox3.TabIndex = 3
        # 
        # button2
        # 
        self._button2.Location = System.Drawing.Point(73, 277)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(479, 109)
        self._button2.TabIndex = 4
        self._button2.Text = "balkan master button (Calc)"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.SystemColors.ButtonShadow
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 16.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(12, 12)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(202, 35)
        self._label1.TabIndex = 5
        self._label1.Text = " Daytime Rate"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.SystemColors.ButtonShadow
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 16.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(12, 77)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(202, 35)
        self._label2.TabIndex = 6
        self._label2.Text = "Evening Rate"
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.SystemColors.ButtonShadow
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 16.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(12, 142)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(202, 35)
        self._label3.TabIndex = 7
        self._label3.Text = " Off-Peak"
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.SystemColors.ButtonShadow
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 16.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(258, 200)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(202, 35)
        self._label4.TabIndex = 8
        self._label4.Text = "Enter # Of Mins"
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.SystemColors.ButtonShadow
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 16.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(73, 424)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(479, 35)
        self._label5.TabIndex = 9
        self._label5.Text = "Final Cost :"
        self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.Chartreuse
        self.ClientSize = System.Drawing.Size(651, 488)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._textBox3)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._button1)
        self.Name = "MainForm"
        self.Text = "Prog272"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button2Click(self, sender, e):
        daytime = int(self._textBox1.Text) 
        eventime = int(self._textBox2.Text)
        offtime  = int(self._textBox3.Text)
        daycost = round(float(daytime * 0.07),3)
        evencost = round(float(eventime * 0.12),3)
        offcost =  round(float(offtime * 0.05),3)
        final = float(daycost + evencost + offcost)
        self._label5.Text = "Your Final Cost Is :  $" + str(final)

    def Button1Click(self, sender, e):
        self._textBox1.Text = ""
        self._textBox2.Text = ""
        self._textBox3.Text = ""
        self._label5.Text = "Final Cost :" 