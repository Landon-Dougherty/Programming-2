using static System.Console;

Write("Enter Num 1 : "); int num1 = int.Parse(ReadLine());
Write("Enter Num 2 : "); int num2 = int.Parse(ReadLine());
Write("Enter Num 3 : "); int num3 = int.Parse(ReadLine());
Write("Enter Num 4 : "); int num4 = int.Parse(ReadLine());

int sum = num1 + num2 + num3 + num4;
double average = sum / 4;
Write("Sum : " + sum);
Write("\nAverage : " + Math.Round(average, 2));
Console.ReadKey();