# Two Stacks Challenge
## Description
Solved Date: 17 May 2023

https://www.hackerrank.com/challenges/game-of-two-stacks/
Alexa has two stacks of non-negative integers, stack a[n] and stack b[m] where index 0 denotes the top of the stack. Alexa challenges Nick to play the following game:

In each move, Nick can remove one integer from the top of either stack a or stack b.
Nick keeps a running sum of the integers he removes from the two stacks.
Nick is disqualified from the game if, at any point, his running sum becomes greater than some integer maxSum given at the beginning of the game.
Nick's final score is the total number of integers he has removed from the two stacks.
Given a, b, and maxSum for g games, find the maximum possible score Nick can achieve.
## Current Status
8/15 tests passing

Passes 8 out of 15 tests, timeouts for remainder most likely due to popping from front of list in python being O(n)

I do short circuit once I get over the maxSum. I’m doing it in Python lists and since it asks for index 0 to be the top of the stack, I wonder where all that popping the first item off the list is causing the issue. In fact that’s very likely https://medium.com/@shuangzizuobh2/how-well-do-you-code-python-9bec36bbc322#:~:text=pop(k)%20has%20a%20time,Use%20deque%20instead.


