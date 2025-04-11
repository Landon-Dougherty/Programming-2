// See https://aka.ms/new-console-template for more information
Console.WriteLine("Enter Length : ");
int len = int.Parse(Console.ReadLine());
Console.WriteLine("Enter Width : ");
int wid = int.Parse(Console.ReadLine());
int area = len * wid;
int perim = 2 * len + 2 * wid;
Console.WriteLine("Your Area : " + area);
Console.WriteLine("Your Perimeter :" + perim);
