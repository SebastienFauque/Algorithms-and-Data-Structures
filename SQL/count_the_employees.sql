The data for the number employed at serveral
famout IT companies is the Company table.
Write a query to print the IDs of the companies
that have more than 10000 employees, in
ascending order of ID.

Sample Input:

Company table
--------------------
Id |    Name  |   Employees
1   Adobe       28085
2   FlipKart      35543
3   Amazon      1089
4   Paytm       9982
5   BookMyShow 5589
6   Oracle       4003
7   NIIT         57782
8   Samsung     2000
9   TCS         10046
10  Wipro       3500



My query:

SELECT id
FROM company
WHERE employees > 10000
ORDER BY id ASC;