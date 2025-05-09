using Microsoft.VisualBasic;
namespace Pg498Payroll
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        const int intMAX_EMPLOYEES = 5;
        const decimal decHOURLY_PAY_RATE = 6.0m;
        private void button1_Click(object sender, EventArgs e)
        {
            // Calc and display gross pay earned by employees
            int[] intHours = new int[intMAX_EMPLOYEES]; // An array of [0,0,0,0,0]
            // <type>[] varname = new <type>[capacity];
            int Count = 0; 
            int EmpHours = 0;
            decimal EmpPay = 0.0m;

            for (Count = 0; Count <= intMAX_EMPLOYEES; Count++) 
            {
                while (int.TryParse(Interaction.InputBox("Enter # of Hours Worked by Employee # " + (Count + 1).ToString(), 
                    "Need Hours Worked"), out EmpHours) == false) {
                    MessageBox.Show("Please enter an integer for hours worked: ");
                }
                
            }

        }
    }
}

