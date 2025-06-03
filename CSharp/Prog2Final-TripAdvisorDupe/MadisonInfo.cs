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
    public partial class MadisonInfo : Form {
        private Form MyParent;
        public MadisonInfo(Form parent) {
            InitializeComponent();
            MyParent = parent;
        }

        private void button2_Click(object sender, EventArgs e) {
            MyParent.Show();
            this.Close();
        }

        private void label16_Click(object sender, EventArgs e) {

        }
    }
}
