using static System.Console;

Write("Enter Base :  "); double bas = int.Parse(ReadLine());
Write("Enter Height : "); double height = int.Parse(ReadLine());
double bas1 = Math.Pow(bas, 2);
double height1 = Math.Pow(height, 2);
double area = (bas * height) / 2;
double hyp = Math.Sqrt((bas1 + height1));

Console.WriteLine("\nYour Hypotenuse : " + Math.Round(hyp, 1));
Write("Your Area : " + Math.Round(area, 2));
Console.WriteLine("\nThe Perimeter : " + Math.Round(hyp + bas + height,2));






