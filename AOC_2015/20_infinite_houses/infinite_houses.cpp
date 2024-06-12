#include <iostream>
#include <vector>

namespace infinite_houses
{
    int get_presents(int number)
    {
        // Create a list of prime numbers and their current factor's cumulative total
        // while we haven't found house with 29000000 presents
        std::vector<int> primes;
        // Special case number 1 to 2
        // If odd number
        if (number % 2 != 0)
        {
            //    Check if number is prime
            bool isPrime = true;
            for (int i = 3; i <= number / 2; i += 2)
            {
                if (number % i == 0)
                {
                    // not a prime, do not keep looping
                    isPrime = false;
                    break;
                }
            }

            if (isPrime)
            {
                primes.push_back(number);
            }
        }

        // Print contents of primes vector
        for (int prime : primes)
        {
            std::cout << prime << " ";
        }
        //    If prime
        //        Add to prime map
        //        Initialize total with number
        return 0;
    }

}

int main()
{
    std::cout << infinite_houses::get_presents(4) << std::endl;
    return 0;
}