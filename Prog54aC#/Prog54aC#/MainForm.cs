/*
 * Created by SharpDevelop.
 * User: dougherty.l
 * Date: 4/14/2025
 * Time: 2:46 PM
 * 
 * To change this template use Tools | Options | Coding | Edit Standard Headers.
 */
using System;
using System.Collections.Generic;
using System.Drawing;
using System.Windows.Forms;

namespace Prog54aC_
{
    /// <summary>
    /// Description of MainForm.
    /// </summary>
    public partial class MainForm : Form
    {
        public MainForm()
        {
            //
            // The InitializeComponent() call is required for Windows Forms designer support.
            //
            InitializeComponent();
            
            //
            // TODO: Add constructor code after the InitializeComponent() call.
            //
        }
        
        void Button1Click(object sender, EventArgs e)
        {
            int miles = 0;
            int gallons = 0;
            double mpg = 0; 
            string car = comboBox1.Text;
            
            if (car == "1970 VW Bug") {
                miles = 286;
                gallons = 9;
            } else if (car == "1979 Firebird") {
                miles = 412;
                gallons = 40;
            } else if (car == "1980 Subaru") { 
                miles = 361;
                gallons = 18;
            } else if (car == "1975 Cutlass") { 
                miles = 161;
                gallons = 11;
            } else { 
                MessageBox.Show("Invalid Selection!");
                return;
            }
            
            mpg = (double)miles / gallons;
            mpg = Math.Round(mpg, 1);
            lblmile.Text = miles.ToString();
            lblgallon.Text = gallons.ToString();
            lblmpg.Text = mpg.ToString();
            
        }
        
        void Button2Click(object sender, EventArgs e)
        {
            lblmile.Text = "";
            lblmpg.Text = "";
            lblgallon.Text = "";
            comboBox1.Text = "";
        }
    }
}
