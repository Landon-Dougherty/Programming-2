using static System.Console;
Write("Enter Radius : "); double rad = double.Parse(Console.ReadLine());
double pi = 3.14159;
double ar = pi * Math.Pow(rad,2);
double cir = 2 * pi * rad;

Write("\nYour Radius : " + Math.Round(rad,2)); Write("\nYour Area : " + Math.Round(ar,2)); Write("\nYour Circumference : " + Math.Round(cir,2));
