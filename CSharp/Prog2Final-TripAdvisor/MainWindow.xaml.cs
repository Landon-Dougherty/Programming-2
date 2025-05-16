using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace Prog2Final_TripAdvisor {
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window {
        //Mapsui.UI.Wpf.MapControl mapControl;

        public MainWindow() {
            InitializeComponent();
            mapControl.Map = new Mapsui.Map();
            mapControl.Map?.Layers.Add(Mapsui.Tiling.OpenStreetMap.CreateTileLayer());
            //mapControl = new Mapsui.UI.Wpf.MapControl();
            //mapControl.Map?.Layers.Add(Mapsui.Tiling.OpenStreetMap.CreateTileLayer());
            //Content = mapControl;
            this.Content = mapControl;

            double WILong = -89.5;
            double WILat = -44.5;

            var center = Mercar

        }
        // button stuff can go here if you eventually find out how to do it.


    }
}
