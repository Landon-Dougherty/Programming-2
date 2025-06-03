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
    public partial class MwkForm : Form {
        private Form MyParent;
        public MwkForm(Form parent) {
            InitializeComponent();

            MyParent = parent;
        }

        private void button1_Click(object sender, EventArgs e) {
            this.MyParent.Show();
            this.Close();
        }

        private void MwkForm_Load(object sender, EventArgs e) {

        }

        private void button2_Click(object sender, EventArgs e) {
            MyParent.Show();
            this.Close();
        }

        private void button1_Click_1(object sender, EventArgs e) {
            MwkInfo mwkInfo = new MwkInfo(this);
            mwkInfo.Show();
            this.Hide();
        }
    }
}
