using static System.Console;
int pay = 0;
int hour = 0;
Write("Hours\tPay");
for (int i = 0; i < 41; i++)
{
    hour = i; 
    pay = hour * 4; 
    Write("\n" + hour + "\t" + pay);
}
ReadLine();

