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
            this.Parent.Show();
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
    }
}
