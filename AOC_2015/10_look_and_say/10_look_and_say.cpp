#include <iostream>
#include <format>

using namespace std;

string next_look_and_say(int input)
{
    string inputString = to_string(input);
    string result = "";

    // Process the first element from the input
    int count = 1;
    char previousChar = inputString[0];
    inputString.erase(0, 1);

    while (!inputString.empty())
    {
        char currentChar = inputString[0];
        if (inputString.length() == 1)
        {
            if (currentChar != previousChar)
            {
                // if its different and then we need to return
                // both the previous result and the the orphaned one.
                result.append(format("{}{}", count, previousChar));
                result.append(format("{}{}", 1, currentChar));
            }
            else
            {
                // if its the same as the previous one, then we need to increment the count
                count += 1;
                result.append(format("{}{}", count, previousChar));
            }
        }
        else if (currentChar != previousChar)
        {
            cout << previousChar << endl;
            result.append(format("{}{}", count, previousChar));
            count = 1;                  // start counter again
            previousChar = currentChar; // Reset the previous character
        }
        else
        {
            count += 1;
            cout << inputString << endl;
        }
        inputString.erase(0, 1);
    }
    return result;
}

int main()
{
    cout << next_look_and_say(115554442) << endl; // call the function
    return 0;
}
