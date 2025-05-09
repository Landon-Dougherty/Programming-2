using static System.Console;
Write("Enter Mass : "); double mass = double.Parse(ReadLine());
double weight = mass * 9.8;
if (weight >= 1000) { Write("Too Heavy"); }
else if (weight <= 10) { Write("Too Light"); }
else
{
    Write("Weight : " + weight);
}
ReadLine();