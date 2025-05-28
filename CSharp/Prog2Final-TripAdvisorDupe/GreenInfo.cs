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
    public partial class GreenInfo : Form {
        private Form MyParent;
        public GreenInfo(Form parent) {
            InitializeComponent();
            MyParent = parent;
        }

        private void button2_Click(object sender, EventArgs e) {
            GreenbayForm greenInfo = new GreenbayForm(this);
            greenInfo.Show();
            this.Close();
        }
    }
}
