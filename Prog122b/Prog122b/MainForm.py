﻿import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._listBox1 = System.Windows.Forms.ListBox()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # listBox1
        # 
        self._listBox1.BackColor = System.Drawing.SystemColors.HotTrack
        self._listBox1.FormattingEnabled = True
        self._listBox1.ItemHeight = 29
        self._listBox1.Location = System.Drawing.Point(12, 12)
        self._listBox1.Name = "listBox1"
        self._listBox1.Size = System.Drawing.Size(462, 265)
        self._listBox1.TabIndex = 0
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.FromArgb(255, 128, 255)
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 17.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(12, 310)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(114, 104)
        self._button1.TabIndex = 1
        self._button1.Text = "Display"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.FromArgb(255, 128, 255)
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 17.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(192, 310)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(114, 104)
        self._button2.TabIndex = 2
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.FromArgb(255, 128, 255)
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 17.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(360, 310)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(114, 104)
        self._button3.TabIndex = 3
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.FromArgb(64, 64, 0)
        self.ClientSize = System.Drawing.Size(486, 426)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._listBox1)
        self.Font = System.Drawing.Font("Microsoft Sans Serif", 17.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self.Name = "MainForm"
        self.Text = "Prog122b"
        self.Load += self.MainFormLoad
        self.ResumeLayout(False)


    def MainFormLoad(self, sender, e):
        pass

    def Button3Click(self, sender, e):
        Application.Exit()

    def Button2Click(self, sender, e):
        self._listBox1.Items.Clear()
        

    def Button1Click(self, sender, e):
        header = "Hours \t Pay" 
        self._listBox1.Items.Add(header)
        for i in range(1,41):
            hours = i 
            pay = hours * 4 
            list = str(hours) + " \t " + str(pay)
            self._listBox1.Items.Add(list)