using static System.Math;
using static System.Console;
Write("Enter numbers of copies to print : ");
int copies = int.Parse(ReadLine());
double price = 0;
double cost = 0;
// && AND, || OR, ! NOT
if (copies > 0 && copies <= 99) price = 0.30;
else if (copies > 99 && copies <= 499) price = 0.28;
else if (copies > 499 && copies <= 749) price = 0.27;
else if (copies > 749 && copies <= 1000) price = 0.26;
else price = 0.25;
cost = price * copies;

Write("Price Per Copy : $" + price);
Write("\nTotal : $" + Math.Round(cost,2));
ReadLine();
