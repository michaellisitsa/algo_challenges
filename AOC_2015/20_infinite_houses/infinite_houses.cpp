#include <iostream>
#include <vector>
#include <set>
#include <algorithm>
#include <utility>

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

    std::pair<int, int> get_presents(int number, std::vector<int> primes)
    {
        std::set<int> visited_elves_gt_50_multiple;
        std::set<int> visited_elves_lte_50_multiple;
        // Special case for end elves
        visited_elves_gt_50_multiple.insert(1); // we know the 1st elf will be way over the 50th multiple
        visited_elves_lte_50_multiple.insert(number);
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
                        if (number / multiple <= 50)
                        {
                            visited_elves_lte_50_multiple.insert(multiple);
                        }
                        else
                        {
                            visited_elves_gt_50_multiple.insert(multiple);
                        }
                    }
                }
            }
        }

        std::pair<int, int> sum = std::make_pair(0, 0);
        for (int elf : visited_elves_gt_50_multiple)
        {
            sum.first += 10 * elf;
        }
        for (int elf : visited_elves_lte_50_multiple)
        {
            sum.first += 10 * elf;
            sum.second += 11 * elf;
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
        bool firstSolved = false;
        bool secondSolved = false;

        std::pair<int, int> presents = infinite_houses::get_presents(trial, primes);
        if (trial % 100 == 0)
        {
            std::cout << "Num: " << trial << " Presents Pt1: " << presents.first << " Pt2: " << presents.second << std::endl;
        }
        if (presents.first >= number && !firstSolved)
        {
            std::cout << "RESULTS PART 1: " << std::endl;
            std::cout << "House Number: " << trial << ", Presents: " << presents.first << std::endl;
            std::cout << trial << std::endl;
            firstSolved = true;
        }
        if (presents.second >= number)
        {
            std::cout << "RESULTS PART 2: " << std::endl;
            std::cout << "House Number: " << trial << ", Presents: " << presents.second << std::endl;
            std::cout << trial << std::endl;
            secondSolved = true;
        }
        if (firstSolved && secondSolved)
        {
            break;
        }
    }
    return 0;
}