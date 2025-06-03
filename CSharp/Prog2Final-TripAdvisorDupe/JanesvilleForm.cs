using System.ComponentModel;

namespace Prog2Final_TripAdvisorDupe {
    public partial class JanesvilleForm : Form {
        private Form MyParent;
        public JanesvilleForm(Form parent) {
            InitializeComponent();
            MyParent = parent;

        }

        public JanesvilleForm(IContainer components, PictureBox pictureBox3, Label label8, Label label7, Label label6, PictureBox pictureBox2, Label label5, Label label4, PictureBox pictureBox1, Label label3, Label label9, Label label10, Button button2, Label label1) {
            this.components = components;
            this.pictureBox3 = pictureBox3;
            this.label8 = label8;
            this.label7 = label7;
            this.label6 = label6;
            this.pictureBox2 = pictureBox2;
            this.label5 = label5;
            this.label4 = label4;
            this.pictureBox1 = pictureBox1;
            this.label3 = label3;
            this.label9 = label9;
            this.label10 = label10;
            this.button2 = button2;
            this.label1 = label1;
        }

        private void button2_Click(object sender, EventArgs e) {
            MainForm mainForm = new MainForm();
            mainForm.Show();
            this.Close();

        }

        private void button1_Click(object sender, EventArgs e) {
            JanesvilleInfo janInfo = new JanesvilleInfo(this);
            janInfo.Show();
            this.Close();
        }

        private void pictureBox4_Click(object sender, EventArgs e) {
            ShellForm shellForm = new ShellForm();
            shellForm.Show();
            this.Close();
        }
    }
}
