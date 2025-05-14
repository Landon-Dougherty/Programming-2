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
    public partial class StudentForm : Form
    {
        public StudentForm()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            int tktCost = 7;
            int tktCount = int.Parse(textBox1.Text);
            double fnlCost = 0.0;
            double tax = 1.07;

            fnlCost = tktCount * tktCost;
            label5.Text = fnlCost.ToString();
            label6.Text = "7%";
            fnlCost = fnlCost * tax;
            label7.Text = fnlCost.ToString();

        }
    }
}
