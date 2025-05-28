using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Prog2Final_TripAdvisorDupe {
    public partial class RacineInfo : Form {
        private Form MyParent;
        public RacineInfo(Form parent) {
            InitializeComponent();
            MyParent = parent;
        }

        private void label4_Click(object sender, EventArgs e) {

        }

        private void label11_Click(object sender, EventArgs e) {

        }

        private void button1_Click(object sender, EventArgs e) {
            
        }

        private void button2_Click(object sender, EventArgs e) {
            RacineForm racForm = new RacineForm(this);
            racForm.Show();
            this.Close();
        }

        private void label15_Click(object sender, EventArgs e) {

        }
    }
}
