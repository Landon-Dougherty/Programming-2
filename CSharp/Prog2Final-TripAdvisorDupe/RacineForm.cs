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
    public partial class RacineForm : Form {
        private Form MyParent;
        public RacineForm(Form parent) {
            InitializeComponent();
            MyParent = parent;  
        }

        private void button1_Click(object sender, EventArgs e) {
            this.MyParent.Show();
            this.Close();
        }

        private void button2_Click(object sender, EventArgs e) {
            RacineInfo racInfo = new RacineInfo(this);
            racInfo.Show();
            this.Close();
        }
    }
}
