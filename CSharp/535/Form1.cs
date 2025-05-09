
namespace _535 {


    public partial class Form1 : Form {
        private string[] strCaption = {"Click Here.", "Try Again!", "Are You Even Trying?",
        "I'm Over Here!"}; 
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e) {
            MessageBox.Show("You got me!", "", MessageBoxButtons.OK, MessageBoxIcon.Exclamation);
            Application.Exit();        
        }


        private void button1_MouseEnter(object sender, EventArgs e) {
            Random rand = new Random();
            int intIndex = rand.Next(strCaption.Length);
            button1.Text = strCaption[intIndex];
            button1.Left = rand.Next(this.Width - button1.Width);
            button1.Top = rand.Next(this.Height - button1.Height - 30);
        }
    }
}