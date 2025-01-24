/* Write your MySQL query statement below */
SELECT
    name
FROM
    Customer
WHERE
    referee_id <> 2
    OR referee_id IS NULL;

/* Runtime 868 ms, 36.62 % */
