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
            bool isPrime = true;
            for (int i = 3; i * i <= number; i += 2)
            {
                if (number % i == 0)
                {
                    isPrime = false;
                    break;
                }
            }
            return isPrime;
        }
        else
        {
            return false;
        }
    }

    int get_presents(int number, std::vector<int> primes)
    {
        std::set<int> visited_elves;
        // Special case for end elves
        visited_elves.insert(1);
        visited_elves.insert(number);
        for (int prime : primes)
        {
            if (prime > number / 2)
            {
                break;
            }
            if (number % prime == 0)
            {
                for (int multiple = prime; multiple <= number / 2; multiple += prime)
                {
                    if (number % multiple == 0)
                    {
                        visited_elves.insert(multiple);
                    }
                }
            }
        }

        int sum = 0;
        for (int elf : visited_elves)
        {
            sum += 10 * elf;
        }
        return sum;
    }
}
int main()
{
    std::vector<int> primes;
    unsigned long long number = 29000000;
    ;
    std::cout << "Started calculating primes" << std::endl;
    for (int i = 2; i <= number / 2; i++)
    {
        if (i % 100000 == 0)
        {
            std::cout << "Calculating prime: " << i << std::endl;
        }
        if (infinite_houses::is_prime(i))
        {
            primes.push_back(i);
        }
    }
    std::cout << "Finished calculating primes" << std::endl;

    // Modify trial value to get reasonable time to completion
    for (unsigned long long trial = 1; trial < number; trial++)
    {
        if (trial % 50 == 0)
        {
            std::cout << "Calculating presents for: " << trial << std::endl;
        }
        if (infinite_houses::get_presents(trial, primes) >= number)
        {
            std::cout << "RESULTS: " << std::endl;
            std::cout << "House Number: " << trial << ", Presents: " << infinite_houses::get_presents(trial, primes) << std::endl;
            std::cout << trial << std::endl;
            break;
        }
    }
    return 0;
}