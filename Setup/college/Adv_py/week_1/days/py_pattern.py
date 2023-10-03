"""
This script prints a pattern in descending order, where each row contains the repeating number in descending order.

Example:
For input '5', the output will be:
5 5 5 5 5
4 4 4 4
3 3 3
2 2
1

Instructions:
- Enter an upper limit 'num' to determine the number of rows in the pattern.
- The script will then print 'num' rows of numbers in descending order, where each row contains the repeating number 'i'.
- The pattern is displayed with each number 'i' printed 'i' times in each row.
"""

num = int(input("Enter upper limit: "))
for i in range(num, 0, -1):
    for j in range(0, i):
        print(i, end='')
    print()
