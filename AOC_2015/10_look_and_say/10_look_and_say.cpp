#include <iostream>
using namespace std;

char pop(string& myString)
{
    // Checking if the string is not empty before removing the last character
    if (!myString.empty())
    {
        char lastValue = myString.back();
        cout << myString << endl;
        myString.pop_back();
        cout << myString << endl;
        return lastValue;
    }
    return '0';
}

// Declaring array to a function call
// https://www.digitalocean.com/community/tutorials/return-array-in-c-plus-plus-function
// Instead return a string
string next_look_and_say(int input)
{
    cout << "I just got executed!" << endl;
    // 1. Convert the input to a string
    string inputString = to_string(input);
    // 2. Loop through the string
    while (!inputString.empty())
    {
        pop(inputString);
    }
    return to_string(input);
}

int main()
{
    cout << next_look_and_say(12) << endl; // call the function
    return 0;
}