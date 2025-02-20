SELECT
    product_id
FROM
    Products
WHERE
    low_facts = 'Y'
    and recyclable = 'Y';

/* Runtime 873 ms, 45.96 % */
