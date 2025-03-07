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
        self.SuspendLayout()
        # 
        # textBox1
        # 
        self._textBox1.BackColor = System.Drawing.Color.Turquoise
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 12.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(142, 324)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(246, 26)
        self._textBox1.TabIndex = 0
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.SystemColors.ButtonHighlight
        self._label1.Location = System.Drawing.Point(142, 236)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(246, 68)
        self._label1.TabIndex = 1
        self._label1.Text = "Enter Word 4 Backwards"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        self._label1.Click += self.Label1Click
        # 
        # button1
        # 
        self._button1.Location = System.Drawing.Point(223, 107)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(75, 68)
        self._button1.TabIndex = 2
        self._button1.Text = "Calc"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        #self._latetoMSOE = True
        # 
        # button2
        # 
        self._button2.Location = System.Drawing.Point(223, 462)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(75, 60)
        self._button2.TabIndex = 3
        self._button2.Text = "Click 4 Clear"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.Chocolate
        self.ClientSize = System.Drawing.Size(559, 568)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._textBox1)
        self.Name = "MainForm"
        self.Text = "StringInterview4"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button2Click(self, sender, e):
        MessageBox.Show("LOLOLOLOLOLOL, I am a teacher and I am an hour and a half late to MSOE")
        self._label1.Text = ""
        self._textBox1.Text = ""

    def Label1Click(self, sender, e):
        pass

    def Button1Click(self, sender, e):
        msg = self._textBox1.Text 
        msg1 = msg[::-1]
        self._label1.Text = str(msg1)