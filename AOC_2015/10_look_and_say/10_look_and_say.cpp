#include <iostream>
using namespace std;

// Write a function that returns a 2 digit array

// Declaring array to a function call
// https://www.digitalocean.com/community/tutorials/return-array-in-c-plus-plus-function
// Instead return a string
string next_look_and_say(int input)
{
    // do nothing
    cout << "I just got executed!" << endl;
    return to_string(input);
}

int main()
{
    cout << next_look_and_say(12) << endl; // call the function
    return 0;
}