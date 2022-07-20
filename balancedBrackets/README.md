# To run:

- `OUTPUT_PATH` should be in your .env file
- `node balancedBrackets/balancedBracket.js`
- Type in a number of lines you are checking. Enter.
- Type in a string of brackets. Enter.
- Repeat for multiple
- Once finished, `Cltrl + D` to trigger stdin end.
- See output text file and console message whether each is balanced.

# Results

`deeply_nested.txt` (150,000 char)

- isBalancedAppend: 7000ms
- isBalancedPrepend: 30ms
- isBalancedList: 20ms

`deeply_nestedx2.txt` (300,000 char)

- isBalancedAppend: 34000ms (approx. 7000 x 2^2) O(n^2)
- isBalancedPrepend: 50ms O(n)
- isBalancedList: 30ms O(n) with slightly better performance.
