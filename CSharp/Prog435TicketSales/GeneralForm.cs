using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Prog435TicketSales
{

    public partial class GeneralForm : Form
    {
        private Form myParent;

        public GeneralForm(Form myParent) // Constructor (__init__)
        {
            InitializeComponent();
            this.myParent = myParent;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            this.myParent.Show();
            this.Close();
        }

        private void GeneralForm_FormClosed(object sender, FormClosedEventArgs e)
        {
            this.Parent.Show();
        }

        private void GeneralForm_Load(object sender, EventArgs e)
        {

        }

        private void GeneralForm_Load_1(object sender, EventArgs e)
        {

        }

        private void label1_Click(object sender, EventArgs e) {

        }

        private void button2_Click(object sender, EventArgs e) {
            double tktCost = 0.0;
            int tktCount = int.Parse(textBox1.Text);
            double fnlCost = 0.0;
            
            if (radioButton1.Checked) 
                tktCost = 20.0;
            else if (radioButton2.Checked) 
                tktCost = 15.0;
            else 
                tktCost = 10.0;
            
            fnlCost = tktCount * tktCost;
            label6.Text = fnlCost.ToString();
            label7.Text = "Tax = 7%";
            
            fnlCost = fnlCost * 1.07;
            
            label8.Text = fnlCost.ToString();


        }
    }
}
