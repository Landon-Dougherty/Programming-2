using Microsoft.VisualBasic;
namespace Prog347
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            int sum = 0;
            int number = int.Parse(Interaction.InputBox("Enter Number :", "Input Needed"));
            for (int i = 0; i <= number; i++)
            {
                sum += i;
            } 
            MessageBox.Show("Sum of Your Number : " + sum);
                
        }
    }
}