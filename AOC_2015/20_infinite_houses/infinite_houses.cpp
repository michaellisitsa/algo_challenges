#include <iostream>
#include <vector>
#include <set>

namespace infinite_houses
{
    bool is_prime(int number)
    {
        if (number < 4)
        {
            return true;
        }
        if (number % 2 != 0)
        {
            std::cout << "Checking if " << number << " is prime." << std::endl;
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
            std::cout << number << " is prime: " << isPrime << std::endl;
            return isPrime;
        }
        else
        {
            return false;
        }
    }

    int get_presents(int number)
    {
        // Create a list of prime numbers and their current factor's cumulative total
        // while we haven't found house with 29000000 presents
        std::vector<int> primes;

        bool isPrime = is_prime(number);
        if (isPrime)
        {
            primes.push_back(number);
        }

        // Print contents of primes vector
        for (int prime : primes)
        {
            std::cout << prime << " ";
        }
        return 0;
    }

}
int main()
{
    std::cout << infinite_houses::get_presents(3) << std::endl;
    return 0;
}