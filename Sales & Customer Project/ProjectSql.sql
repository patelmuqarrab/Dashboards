SELECT * FROM sales_data;

#1. What is the total revenue generated from each region?

SELECT Region, ROUND(SUM(Revenue),2) AS TotalRevenue
FROM sales_data
GROUP BY Region
ORDER BY TotalRevenue DESC;

#2. Which product category has the highest average profit margin? (Profit Margin = (Profit / Revenue) * 100)

SELECT `Product Category`, round(AVG((PROFIT/REVENUE)*100),2) AS AvgProfitMargin 
FROM sales_data
group by `Product Category`
ORDER BY AvgProfitMargin DESC
limit 10;

#3. List the top 5 products by units sold.

SELECT `Product Name`, SUM(`Units Sold`) AS TotalUnitsSold
FROM sales_data
GROUP BY `Product Name`
ORDER BY TotalUnitsSold DESC
LIMIT 5;

#4. What is the average customer satisfaction score for each product category?

SELECT `Product Category`, round(avg(`Customer Satisfaction`),2) as AvgCustSatisfaction
FROM sales_data
group by `Product Category`
order by AvgCustSatisfaction desc;

#5. Which region has the highest number of male customers?

SELECT `Region`, Count(*) AS MaleCust
from sales_data
where `Customer Gender` = 'Male'
group by `Region`
ORDER BY MaleCust DESC;

#6. Find the total profit for each product category in 2023.

SELECT `Product Category`, round(SUM(Profit),2) AS TotalProfit
FROM sales_data
WHERE YEAR(STR_TO_DATE(Date, '%Y-%m-%d')) = 2023
GROUP BY `Product Category`;

#7. Identify products with negative profit.

SELECT ROW_NUMBER() OVER() AS Index_Number, `Product Name`, Profit
FROM sales_data
WHERE Profit < 0;

#8. What is the average age of customers by region?

SELECT Region, round(AVG(`Customer Age`),2) AS AvgCustomerAge
FROM sales_data
GROUP BY Region
ORDER BY AvgCustomerAge DESC;

#9. Which month in 2023 had the highest sales?

SELECT MONTH(STR_TO_DATE(Date, '%Y-%m-%d')) AS Month, round(SUM(Revenue),2) AS TotalRevenue
FROM sales_data
WHERE YEAR(STR_TO_DATE(Date, '%Y-%m-%d')) = 2023
GROUP BY Month
ORDER BY TotalRevenue DESC
LIMIT 1;

#10. How does the revenue compare between male and female customers?

SELECT `Customer Gender`, round(SUM(Revenue),2) AS TotalRevenue
FROM sales_data
GROUP BY `Customer Gender`;