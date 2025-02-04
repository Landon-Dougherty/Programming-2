import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._listBox1 = System.Windows.Forms.ListBox()
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.LightSeaGreen
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 22.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(28, 351)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(131, 84)
        self._button1.TabIndex = 0
        self._button1.Text = "Display"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.LightSeaGreen
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 22.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(213, 351)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(131, 84)
        self._button2.TabIndex = 1
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.LightSeaGreen
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 22.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(399, 351)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(131, 84)
        self._button3.TabIndex = 2
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # listBox1
        # 
        self._listBox1.BackColor = System.Drawing.Color.LightSeaGreen
        self._listBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 17.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._listBox1.FormattingEnabled = True
        self._listBox1.ItemHeight = 29
        self._listBox1.Location = System.Drawing.Point(28, 21)
        self._listBox1.Name = "listBox1"
        self._listBox1.Size = System.Drawing.Size(502, 294)
        self._listBox1.TabIndex = 3
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.CadetBlue
        self.ClientSize = System.Drawing.Size(563, 470)
        self.Controls.Add(self._listBox1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Name = "MainForm"
        self.Text = "Prog115a"
        self.Load += self.MainFormLoad
        self.ResumeLayout(False)


    def MainFormLoad(self, sender, e):
        pass

    def Button3Click(self, sender, e):
        Application.Exit()
        

    def Button2Click(self, sender, e): #Clear
        self._listBox1.Items.Clear()

    def Button1Click(self, sender, e):
        self._listBox1.Items.Clear()
        lcv = 2 # Loop Control Variable
        while lcv <= 36:
            self._listBox1.Items.Add(str(lcv))
            lcv += 2 
        pass
    
        