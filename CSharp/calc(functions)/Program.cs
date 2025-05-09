using static System.Console;
// <access level> <static or not> <return type> name(<args>) {}
// in console app, we'll mak eall functions "static"
// Not static in Forms appls; always "public" thought

static int add(int x, int y) { return x + y;}
static int subtract(int x , int y) { return x - y;}
static int div(int x, int y) { return x / y;}
static int mul(int x, int y) { return x * y; }

static void wait()
{ // void means 'returns nothing'
    ReadLine();
    // return;
}

Random rand = new Random();
int n1 = rand.Next(1,100) + 1;
int n2 = rand.Next(150,200) + 1;
Write("Choose an option: add, sub, mul, or div\n");
string op = ReadLine().ToLower();
int result = 0;
if (op == "add") result = add(n1, n2);
else if (op == "sub") result = subtract(n1, n2);
else if (op == "mul") result = mul(n1, n2);
else if (op == "dov") result = div(n1, n2);


Write("Result: " + result);
wait();

