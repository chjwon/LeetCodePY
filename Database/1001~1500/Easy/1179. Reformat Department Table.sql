# Write your MySQL query statement below
SELECT 
    id,
	SUM(case when month = 'JAN' then revenue else null end) AS Jan_Revenue,
	SUM(case when month = 'FEB' then revenue else null end) AS Feb_Revenue,
	SUM(case when month = 'MAR' then revenue else null end) AS Mar_Revenue,
	SUM(case when month = 'APR' then revenue else null end) AS Apr_Revenue,
	SUM(case when month = 'MAY' then revenue else null end) AS May_Revenue,
	SUM(case when month = 'JUN' then revenue else null end) AS Jun_Revenue,
	SUM(case when month = 'JUL' then revenue else null end) AS Jul_Revenue,
	SUM(case when month = 'AUG' then revenue else null end) AS Aug_Revenue,
	SUM(case when month = 'SEP' then revenue else null end) AS Sep_Revenue,
	SUM(case when month = 'OCT' then revenue else null end) AS Oct_Revenue,
	SUM(case when month = 'NOV' then revenue else null end) AS Nov_Revenue,
	SUM(case when month = 'DEC' then revenue else null end) AS Dec_Revenue
FROM department
GROUP BY id
ORDER BY id