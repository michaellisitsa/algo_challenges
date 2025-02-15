# Super Digit
Solved Date: 8 September 2022
https://www.hackerrank.com/challenges/recursive-digit-sum

We define super digit of an integer x  using the following rules:

Given an integer, we need to find the super digit of the integer.

If x has only 1 digit, then its super digit is x.
Otherwise, the super digit of x is equal to the super digit of the sum of the digits of x.

Complete the function superDigit in the editor below. It must return the calculated super digit as an integer.

superDigit has the following parameter(s):

string n: a string representation of an integer
int k: the times to concatenate n to make p
