using GMap.NET.MapProviders;
using GMap.NET.WindowsPresentation;
using System;
using System.Windows;
using System.Windows.Controls;
using GMap.NET;

namespace YourNamespace
{
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();

            // Initialize the GMap Control
            gMapControl.MapProvider = GMapProviders.GoogleMap;
            gMapControl.SetPositionByKeywords("Madison, Wisconsin, USA");
            gMapControl.MinZoom = 1;
            gMapControl.MaxZoom = 17;
            gMapControl.Zoom = 10;

            // Additional GMap settings
            gMapControl.ShowTileGridLines = false;
            gMapControl.Manager.Mode = GMap.NET.AccessMode.ServerOnly;

            // Place button over the specific location (Madison, WI)
            PlaceButtonOverMap();
        }

        // Function to calculate map position for a button (Madison, WI)
        private void PlaceButtonOverMap()
        {
            // Coordinates for Madison, WI (Latitude, Longitude)
            double lat = 43.0731;
            double lon = -89.4012;

            // Convert map coordinates to screen coordinates
            var point = gMapControl.FromLatLngToLocal(new PointLatLng(lat, lon));

            // Position the button on the canvas based on screen coordinates
            Canvas.SetLeft(mwkButton, point.X - mwkButton.Width / 2);
            Canvas.SetTop(mwkButton, point.Y - mwkButton.Height / 2);
        }

     