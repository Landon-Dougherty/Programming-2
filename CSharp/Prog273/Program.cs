using static System.Console;
Write("Enter Amount of Books Scanned : ");
int scan = int.Parse(ReadLine());
int point = 0;
if (scan >= 4)
{
    point = 60;
} else if (scan == 3)
{
    point = 30;
} else if (scan == 2)
{
    point = 15;
} else if (scan == 1)
{
    point = 5;
} else
{
    point = 0;
}
Write("Your Total Points : " + point.ToString());
ReadLine();