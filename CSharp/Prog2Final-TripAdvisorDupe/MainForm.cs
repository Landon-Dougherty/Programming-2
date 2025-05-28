using System;
using System.Windows.Forms;
using GMap.NET;
using GMap.NET.MapProviders;
using GMap.NET.WindowsForms;
using GMap.NET.WindowsForms.Markers;

namespace Prog2Final_TripAdvisorDupe {
    public partial class MainForm : Form {
        private GMapControl gMapControl;
        private GMapOverlay markersOverlay;

        List<string> cities = new List<string> {
            "Madison, WI",
            "Milwaukee, WI",
            "Janesville, WI",
            "Green Bay, WI",
            "Kenosha, WI",
            "Racine, WI"
        };
        public MainForm() {
            InitializeComponent();
            
            // Initialize and configure the GMap control
            gMapControl = new GMapControl {
                Dock = DockStyle.Fill,
                MapProvider = GMapProviders.GoogleMap,
                MinZoom = 1,
                MaxZoom = 17,
                Zoom = 8,
                Position = new PointLatLng(43.0731, -89.4012), // Center on Madison
                ShowCenter = false
            };

            // Add map to the form
            this.panel1.Controls.Add(gMapControl);

            // Initialize the marker overlay
            markersOverlay = new GMapOverlay("markers");

            // Add markers

            AddMarker(43.0731, -89.4012, cities[0]);    // Madison
            AddMarker(43.0389, -87.9065, cities[1]);  // Milwaukee
            AddMarker(42.6821, -89.0275, cities[2]); // Janesville
            AddMarker(44.5133, -88.0133, cities[3]); // Green Bay
            AddMarker(42.588079, -87.822877, cities[4]); // Kenosha 
            AddMarker(42.722702, -87.784225, cities[5]); // Racine 


            // Add the overlay to the map
            gMapControl.Overlays.Add(markersOverlay);

            // Subscribe to map mouse click
            gMapControl.MouseClick += GMapControl_MouseClick;
        }

        // Method to add a marker with a tooltip and tag
        private void AddMarker(double lat, double lng, string name) {
            var position = new PointLatLng(lat, lng);
            var marker = new GMarkerGoogle(position, GMarkerGoogleType.red_dot) {
                ToolTipText = name,
                ToolTipMode = MarkerTooltipMode.OnMouseOver,
                Tag = name // You can store any identifier here
            };

            markersOverlay.Markers.Add(marker);
        }

        // MouseClick event handler to detect marker click
        private void GMapControl_MouseClick(object sender, MouseEventArgs e) {
            if (e.Button == MouseButtons.Left) {
                PointLatLng clickPoint = gMapControl.FromLocalToLatLng(e.X, e.Y);

                // Loop through all markers to check if click is near one
                foreach (var marker in markersOverlay.Markers) {
                    double distance = GetDistance(clickPoint, marker.Position);
                    if (distance < 7.50) { // 1km radius threshold
                        // Marker clicked!
                        string name = marker.Tag as string;
                        MessageBox.Show($"You Clicked: {name}");
                         
                        // If Madison is clicked 
                        if (name == cities[0]) {
                            MadisonForm madForm = new MadisonForm(this);
                            madForm.Show();
                            this.Hide();
                        }
                        if (name == cities[1]) { // MWK
                            MwkForm mwkForm = new MwkForm(this);
                            mwkForm.Show();
                            this.Hide();
                        }
                        if (name == cities[2]) { // Janesville
                            JanesvilleForm janForm = new JanesvilleForm(this);
                            janForm.Show();
                            this.Hide();
                        }
                        if (name == cities[3]) { // Green Bay
                            GreenbayForm genForm = new GreenbayForm(this);
                            genForm.Show();
                            this.Hide();
                        }
                        if (name == cities[4]) { // Kenosha
                            KenoshaForm kenForm = new KenoshaForm(this);
                            kenForm.Show();
                            this.Hide();
                        }
                        if (name == cities[5]) { // Racine?
                            RacineForm recForm = new RacineForm(this);
                            recForm.Show();
                            this.Hide();
                        }
                    }
                }
            }
        }

        // Calculates distance between two coordinates in kilometers
        private double GetDistance(PointLatLng point1, PointLatLng point2) {
            var R = 6371; // Earth's radius in km
            var dLat = DegreesToRadians(point2.Lat - point1.Lat);
            var dLon = DegreesToRadians(point2.Lng - point1.Lng);
            var a = Math.Sin(dLat / 2) * Math.Sin(dLat / 2) +
                    Math.Cos(DegreesToRadians(point1.Lat)) * Math.Cos(DegreesToRadians(point2.Lat)) *
                    Math.Sin(dLon / 2) * Math.Sin(dLon / 2);
            var c = 2 * Math.Atan2(Math.Sqrt(a), Math.Sqrt(1 - a));
            return R * c;
        }

        private double DegreesToRadians(double deg) {
            return deg * (Math.PI / 180);
        }

        private void button1_Click(object sender, EventArgs e) {
            Application.Exit();
        }
    }
}