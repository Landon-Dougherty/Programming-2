using static System.Math;
using static System.Console;

Write("Enter Your Number : ");
double before = double.Parse(ReadLine());
before = before - 165;
double after = before / 100;
double month = Math.Floor(after / 1);
double minus = Math.Round(after - month,2);
minus = Math.Round(minus * 100);
Write("Your Birthday : " + month + " Month and " + minus + " Day.");
ReadLine();




