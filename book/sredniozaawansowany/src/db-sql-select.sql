SELECT * FROM kontakty

select 'John' as name, 42 as age

SELECT * FROM stocks ORDER BY price;


SELECT * FROM Customers
WHERE CustomerName LIKE 'a%';

SELECT * FROM Customers
WHERE CustomerName LIKE '%or%';

SELECT * FROM Customers
WHERE CustomerName LIKE 'a_%_%';


SELECT * FROM Customers
WHERE Country IN ('Germany', 'France', 'UK');


SELECT * FROM Customers
WHERE Country IN (SELECT Country FROM Suppliers);

SELECT DISTINCT Country FROM Customers;

SELECT COUNT(DISTINCT Country) FROM Customers;

-- COUNT()
SELECT COUNT(column_name)
FROM table_name
WHERE condition;

-- AVG()
SELECT AVG(column_name)
FROM table_name
WHERE condition;

-- SUM()
SELECT SUM(column_name)
FROM table_name
WHERE condition;