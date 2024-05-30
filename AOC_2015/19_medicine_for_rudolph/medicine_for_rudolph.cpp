// Imports necessary to get file input to work
#include <fstream>
#include <iostream>
#include <vector>
#include <string>
#include <set>
// Import necessary for maps.
#include <map> // Add this line to include the <map> header file

const std::string INPUT = "CRnCaSiRnBSiRnFArTiBPTiTiBFArPBCaSiThSiRnTiBPBPMgArCaSiRnTiMgArCaSiThCaSiRnFArRnSiRnFArTiTiBFArCaCaSiRnSiThCaCaSiRnMgArFYSiRnFYCaFArSiThCaSiThPBPTiMgArCaPRnSiAlArPBCaCaSiRnFYSiThCaRnFArArCaCaSiRnPBSiRnFArMgYCaCaCaCaSiThCaCaSiAlArCaCaSiRnPBSiAlArBCaCaCaCaSiThCaPBSiThPBPBCaSiRnFYFArSiThCaSiRnFArBCaCaSiRnFYFArSiThCaPBSiThCaSiRnPMgArRnFArPTiBCaPRnFArCaCaCaCaSiRnCaCaSiRnFYFArFArBCaSiThFArThSiThSiRnTiRnPMgArFArCaSiThCaPBCaSiRnBFArCaCaPRnCaCaPMgArSiRnFYFArCaSiThRnPBPMgAr";

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

// replacementMap is passed by reference to avoid copying
// Pass the input by const reference, because INPUT is a const
std::set<std::string> generateMolecules(std::map<std::string, std::vector<std::string>> &replacementsMap, const std::string &input)
{
    std::set<std::string> distinctMolecules;
    int currentPos = 0;
    while (currentPos < input.size())
    {
        std::string currentChar = input.substr(currentPos, 1);
        std::string twoCharMatcher = input.substr(currentPos, 2);
        if (replacementsMap.find(currentChar) != replacementsMap.end())
        {
            for (const auto &value : replacementsMap[currentChar])
            {
                std::string newString = input;
                newString.replace(currentPos, 1, value);
                distinctMolecules.insert(newString);
            }
        }
        else if (replacementsMap.find(twoCharMatcher) != replacementsMap.end())
        {
            for (const auto &value : replacementsMap[twoCharMatcher])
            {
                std::string newString = input;
                newString.replace(currentPos, 2, value);
                distinctMolecules.insert(newString);
            }
            // An extra shift right is needed because we are looking at two characters
            currentPos++;
        }
        currentPos++;
    }
    std::cout << "Distinct molecules: " << distinctMolecules.size() << std::endl;
    // This is making a brand new copy in the top scope.
    // For more memory efficiency we could possibly use other techniques
    // like passing a reference to the set and modifying it in place.
    return distinctMolecules;
}

int main()
{
    std::map<std::string, std::vector<std::string>> replacementsMap;
    // Since readFileIntoMap takes a reference, we can pass the map directly
    // and it is modified in place.
    readFileIntoMap(replacementsMap);
    std::set<std::string> part1 = generateMolecules(replacementsMap, INPUT);
    return 0;
}

// Starting from a single molecule e
// we need to try all the possible replacements on it.
// For each distinct molecule
//    we need to try all the possible replacements on it.
//    Delete the original distinct molecule
// Accumulate all the local distinct molecules into a set of global distinct molecules
