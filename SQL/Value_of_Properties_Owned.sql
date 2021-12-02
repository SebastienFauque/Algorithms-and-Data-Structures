There are two tables in a database of real estate owners. One has
ownership information and the other has price information,
in millions. An owner may own multiple houses, but a house will have
only one owner.

Write a query to print the IDs of the owners who have at least 100 million
worth of houses and own more than 1 house. The order
of output does not matter. The result should be in the format: BUYER_ID TOTAL_Worth

Sample data tables:
      house
BUYER_ID | TOTAL_WORTH
1           abc123
2           def456
3           abc456
1           def123
2           def789


      price
HOUSE_ID | PRICE
abc123      60
def456      20
abc456      120
def123      40
def789      70

My solution:
SELECT BUYER_ID, SUM(PRICE) AS TOTAL_WORTH
FROM house h
INNER JOIN price p
ON h.HOUSE_ID = p.HOUSE_ID
GROUP BY BUYER_ID
HAVING COUNT(h.HOUSE_ID) > 1 AND SUM(PRICE) >= 100;
