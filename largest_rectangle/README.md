# Largest Rectangle

Solved Date: 24 May 2023
https://www.hackerrank.com/challenges/largest-rectangle

## Description

Skyline Real Estate Developers is planning to demolish a number of old, unoccupied buildings and construct a shopping mall in their place. Your task is to find the largest solid area in which the mall can be constructed.

There are a number of buildings in a certain two-dimensional landscape. Each building has a height, given by `h[i]` where `i subset [1,n]`. If you join k adjacent buildings, they will form a solid rectangle of area `k x min(h[i], h[i+1], ..., h[i] + k - 1])`.
