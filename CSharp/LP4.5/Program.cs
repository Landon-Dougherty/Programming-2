Console.Write("Enter the grade percentage : ");
double perc = double.Parse(Console.ReadLine());
char letgrade = ' ';
if (perc >= 90)
{
    letgrade = 'A';
}
else if (perc >= 80)
{
    letgrade = 'B';
}
else if (perc >= 70)
{
    letgrade = 'C';
} else if (perc >= 60)
{
    letgrade = 'D';
} else
{
    letgrade = 'F';
}
Console.WriteLine("The letter grade is: " + letgrade);
Console.ReadLine();