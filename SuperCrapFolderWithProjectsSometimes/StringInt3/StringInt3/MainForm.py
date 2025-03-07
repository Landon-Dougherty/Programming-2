import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._label4 = System.Windows.Forms.Label()
        self._button3 = System.Windows.Forms.Button()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._label3 = System.Windows.Forms.Label()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._label1 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.White
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(39, 179)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(258, 46)
        self._label4.TabIndex = 23
        self._label4.Text = "First Unq. Letter :"
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.Wheat
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 17.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(244, 339)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(288, 164)
        self._button3.TabIndex = 22
        self._button3.Text = "Clear"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.Wheat
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 17.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(459, 266)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(288, 164)
        self._button1.TabIndex = 21
        self._button1.Text = "Calc"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.Wheat
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 17.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(26, 266)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(288, 164)
        self._button2.TabIndex = 20
        self._button2.Text = "Exit"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.SystemColors.ActiveBorder
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(303, 179)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(343, 46)
        self._label3.TabIndex = 19
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 17, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(303, 47)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(343, 33)
        self._textBox1.TabIndex = 17
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.White
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(39, 39)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(258, 46)
        self._label1.TabIndex = 16
        self._label1.Text = "Enter Word  :"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.Chocolate
        self.ClientSize = System.Drawing.Size(768, 513)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "StringInt3"
        self.Load += self.MainFormLoad
        self.ResumeLayout(False)
        self.PerformLayout()


    def MainFormLoad(self, sender, e):
        pass

    def Button1Click(self, sender, e): #Calc
        self._label3.Text = ""
        str = self._textBox1.Text.lower() 
        for i in range(0,len(str)):
            str.find(str[i])
            y = str.rfind(str[i])
            if str[i] == str[y] :
                self._label3.Text = str[i]
                return
            
    def Button2Click(self, sender, e): 
        Application.Exit()
        pass

    def Button3Click(self, sender, e):
        self._textBox1.Text = ""
        pass