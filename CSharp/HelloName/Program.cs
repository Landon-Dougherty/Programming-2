// See https://aka.ms/new-console-template for more information
Console.WriteLine("Enter Your Name : ");
// int, bool, string, char, double instead of float usually
// double --> double precision floating point 
string name = Console.ReadLine();
Console.WriteLine("Hello, " + name);

Console.WriteLine("Enter Your Age :");
// int age = Convert.ToInt32(Console.ReadLine());
int age = int.Parse(Console.ReadLine());
// same as age = int(input())
Console.WriteLine("You Are " + age + " Year Old!");

Console.ReadLine();
