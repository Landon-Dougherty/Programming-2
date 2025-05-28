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
    public partial class MwkInfo : Form {
        private Form MyParent;
        public MwkInfo(Form parent ) {
            InitializeComponent();
            MyParent = parent;
        }

        private void button2_Click(object sender, EventArgs e) {
            MwkForm mwkForm = new MwkForm(this);
            mwkForm.Show();
            this.Close();
        }
    }
}
