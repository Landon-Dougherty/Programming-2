import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.FromArgb(224, 224, 224)
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 12.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(39, 73)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(111, 31)
        self._label1.TabIndex = 0
        self._label1.Text = "Length :"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.FromArgb(224, 224, 224)
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 12.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(39, 132)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(111, 31)
        self._label2.TabIndex = 1
        self._label2.Text = "Width :"
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.FromArgb(224, 224, 224)
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 12.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(39, 287)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(413, 31)
        self._label3.TabIndex = 3
        self._label3.Text = "Perimeter :"
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.FromArgb(224, 224, 224)
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 12.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(39, 228)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(413, 31)
        self._label4.TabIndex = 2
        self._label4.Text = "Area :"
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 12.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(156, 75)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(133, 26)
        self._textBox1.TabIndex = 4
        # 
        # textBox2
        # 
        self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 12.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.Location = System.Drawing.Point(156, 134)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(133, 26)
        self._textBox2.TabIndex = 5
        # 
        # button1
        # 
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 17.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(329, 12)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(123, 92)
        self._button1.TabIndex = 6
        self._button1.Text = "Calc"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 17.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(467, 12)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(123, 92)
        self._button2.TabIndex = 7
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 17.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(403, 110)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(123, 92)
        self._button3.TabIndex = 8
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = True
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.FromArgb(192, 255, 192)
        self.ClientSize = System.Drawing.Size(619, 410)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "Prog52a"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        length = int(self._textBox1.Text)
        width = int(self._textBox2.Text)
        # area = length * width
        # perim = 2 * length + 2 * width
        self._label3.Text = "Perimeter : "  + str((length * 2) + (width * 2))
        # self._label3.Text = "Perimeter : " + str(perim)
        self._label4.Text = "Area : " + str(length * width)
        # self._label4.Text = "Area : " + str(area)
    
    def Button2Click(self, sender, e):
        self._label1.Text = "Length : " 
        self._label2.Text = "Width : "  
        self._label3.Text = "Perimeter : "
        self._label4.Text = "Area : "
 
    def Button3Click(self, sender, e):
        Application.Exit()