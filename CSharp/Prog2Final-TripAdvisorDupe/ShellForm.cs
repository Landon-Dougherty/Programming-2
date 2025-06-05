using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Media;


namespace Prog2Final_TripAdvisorDupe {
    public partial class ShellForm : Form {
        private System.Windows.Forms.Timer moveTimer;
        private int speed = 10;
        private Random random;
        SoundPlayer player;
        public ShellForm() {

            InitializeComponent();

            random = new Random();
            moveTimer = new System.Windows.Forms.Timer();
            moveTimer.Interval = 350; // slower so movement is visible and catchable
            moveTimer.Tick += new EventHandler(MoveTimer_Tick);
            moveTimer.Start();
            player = new SoundPlayer("song.wav");
           
        }

        private void MoveTimer_Tick(object sender, EventArgs e) {
            // Get screen working area (excludes taskbar)
            var workingArea = Screen.PrimaryScreen.WorkingArea;

            // Calculate random X, Y so the whole form fits on screen
            int maxX = workingArea.Width - this.Width;
            int maxY = workingArea.Height - this.Height;

            int randomX = random.Next(0, maxX);
            int randomY = random.Next(0, maxY);

            // Move form to new random location
            this.Location = new System.Drawing.Point(randomX + workingArea.Left, randomY + workingArea.Top);
        }

        private void pictureBox1_Click(object sender, EventArgs e) {
            JanesvilleForm janForm = new JanesvilleForm(this);
            player.Stop(); 
            janForm.Show();
            
            this.Close();

        }

        private void label1_Click(object sender, EventArgs e) {

        }

        private void pictureBox2_Click(object sender, EventArgs e) {

        }

        private void ShellForm_Load(object sender, EventArgs e) {
            try {
                string fullPath = System.IO.Path.Combine(Application.StartupPath, "song.wav");


                player = new SoundPlayer(fullPath);
                player.PlayLooping();  // 🔁 Loop forever
            } catch (Exception ex) {
            }
        }

        
    }
}
