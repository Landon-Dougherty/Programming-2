using static System.Console;
Write("Enter Weight in Kg : "); int weight = int.Parse(ReadLine());
Write("Enter Length In cm : "); double length = double.Parse(ReadLine());
Write("Enter Width In cm : "); double width = double.Parse(ReadLine());
Write("Enter Height In cm : "); double height = double.Parse(ReadLine());
double size = Math.Round(length * width * height, 2);
if (weight > 27 && size < 100000) 
{
    Write("Your Package Is Too Heavy! ");
    ReadLine();
} else if (weight > 27 && size > 100000){
    Write("Your Package Is Too Heavy And Too Large!");
    ReadLine();
} else if (weight <= 27 && size > 100000)
{
    Write("Your Package Is Too Large!");
    ReadLine();
} else
{
    Write("Your Package Is Acceptable!");
    ReadLine();
}
