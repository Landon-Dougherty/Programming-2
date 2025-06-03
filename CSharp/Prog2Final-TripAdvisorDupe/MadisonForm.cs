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
    public partial class MadisonForm : Form {

        private Form MyParent;
        public MadisonForm(Form parent) {
            InitializeComponent();

            this.MyParent = parent;
        }

        private void button1_Click(object sender, EventArgs e) {
            this.MyParent.Show();
            this.Close();
        }
        private void button2_Click(object sender, EventArgs e) {
            MadisonInfo madInfo = new MadisonInfo(this);
            madInfo.Show();
            this.Hide();
        }
        private void label2_Click(object sender, EventArgs e) {

        }

        private void MadisonForm_Load(object sender, EventArgs e) {

        }
    }
}
