// Imports necessary to get file input to work
#include <fstream>
#include <iostream>
#include <vector>
#include <string>
// Import necessary for maps.
#include <map> // Add this line to include the <map> header file

void readFileIntoMap(std::map<std::string, std::vector<std::string>> &map)
{
    std::ifstream file("test_data.txt");
    if (file.is_open())
    {
        std::string line;
        // Default termination is \n, otherwise pass 3rd parameter.
        while (std::getline(file, line))
        {
            // size_t used because it stores any size of object in bytes.
            // If the string is very long, the delimiter position could overflow an int.
            size_t delimiterPos = line.find(" => ");
            // npos is a constant static member value with the greatest possible value for an element of type size_t.
            // so reaching it would signify no match
            if (delimiterPos != std::string::npos)
            {
                std::string key = line.substr(0, delimiterPos);
                std::string value = line.substr(delimiterPos + 4);
                // Check if the key already exists in the map
                if (map.find(key) != map.end())
                {
                    // If the key exists, add the new value to the existing vector
                    map[key].push_back(value);
                }
                else
                {
                    // If the key doesn't exist, create a new vector, add the value to it,
                    // and then add the vector to the map
                    std::vector<std::string> values;
                    values.push_back(value);
                    map[key] = values;
                }
            }
            else
            {
                // Handle invalid input
            }
        }
        file.close();
    }
    else
    {
        std::cout << "Unable to open file\n";
    }
}

int main()
{
    std::map<std::string, std::vector<std::string>> map;
    readFileIntoMap(map);
    // We are getting a reference to every key-value pair in the map
    // and marking it const so that we can't modify it
    for (const auto &pair : map)
    {
        std::cout << pair.first << " => ";
        // We are getting a reference to each item in the vector
        // and marking it const so that we can't modify it
        for (const auto &value : pair.second)
        {
            std::cout << value << ", ";
        }
        std::cout << std::endl;
    }
    return 0;
}
// Parse the keys to objects mapping
// and store it in a map

// while the remainingChars is not empty
//    If the next character is a one-character matcher
//        copy the string and replace the character
//    elseif the next character is a two-character matcher
//        copy the string and replace the two characters
//    else
//        pop the currentChar from the remainingChars
//    push the string onto a Set
