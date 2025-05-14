using static System.Console;
Write("Enter a string: ");
string word = ReadLine().ToLower();

int v = 0;
int c = 0;

for (int i = 0; i < word.Length; i++) {
    char let = word[i];
        if (let == 'a' || let == 'e' || let == 'i' || let == 'o' || let == 'u') 
        v++;
        else if (let >= 'a' && let <= 'z') c++; // Check ASCII range of lowercase letters  
}

Write("{0} contains {1} vowels and {2} consonants",
    word, v, c);
ReadLine();

// Why can't we just do cool things like make a practically used program in a given instance.
