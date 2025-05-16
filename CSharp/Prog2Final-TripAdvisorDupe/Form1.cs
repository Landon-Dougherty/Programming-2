// using Mapsui;
using System;
using System.Windows.Forms;
using GMap.NET;
using GMap.NET.MapProviders; 
using GMap.NET.WindowsForms;
using GMap.NET.WindowsForms.Markers;


namespace Prog2Final_TripAdvisorDupe {
    public partial class Form1 : Form { 
        private Button buttonOnMap;
        public Form1() {
            InitializeComponent();            
            // var mapControl = new MapControl();
            // Controls.Add(mapControl);
            // mapControl.Map.Layers.Add(Mapsui.Tiling.OpenStreetMap.CreateTileLayer());
            
        }
        GMapControl gMapControl;
        private void Form1_Load(object sender, EventArgs e) {
            gMapControl = new GMapControl();
            gMapControl.Dock = DockStyle.Fill;
            this.panel1.Controls.Add(gMapControl);  // panel1 is your Panel where map will be placed
            gMapControl.MapProvider = GMapProviders.GoogleMap;  // You can use other map providers
            GMaps.Instance.Mode = AccessMode.ServerOnly;

            buttonOnMap = new Button();
            buttonOnMap.Text = "Click me";
            buttonOnMap.Size = new System.Drawing.Size(100,50);


            PlaceButtonOnMap(new PointLatLng(43.0389, -87.9065));  // Milwaukee, WI coordinates


            gMapControl.Position = new PointLatLng(43.038902, -87.906471); // Set the default map location (New York)
            gMapControl.MinZoom = 2;
            gMapControl.MaxZoom = 17;
            gMapControl.Zoom = 10;
            gMapControl.DragButton = MouseButtons.Left;
        }

        private void button1_Click(object sender, EventArgs e) {
            // Example: Add a marker at the current map center
            PointLatLng point = new PointLatLng(); 

            GMapMarker marker = new GMarkerGoogle(point, GMarkerGoogleType.green);
            GMapOverlay markersOverlay = new GMapOverlay("markers");

            markersOverlay.Markers.Add(marker);
            gMapControl.Overlays.Add(markersOverlay);
        }
    }
}