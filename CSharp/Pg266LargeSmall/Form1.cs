namespace Pg266LargeSmall
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            int a = int.Parse(textBox1.Text);
            int b = int.Parse(textBox2.Text);
            int test = Math.Max(a, b);
            label4.Text = $"Output : {test}";


        }
    }
}