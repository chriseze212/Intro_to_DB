-- Select the database
USE alx_book_store;

-- Display the full description of the table 'books' without using  or EXPLAIN
-- Print full description of the 'Books' table using INFORMATION_SCHEMA
SELECT
    COLUMN_NAME,
    COLUMN_TYPE,
    IS_NULLABLE,
    COLUMN_KEY,
    COLUMN_DEFAULT,
    EXTRA
FROM
    INFORMATION_SCHEMA.COLUMNS
WHERE
    TABLE_SCHEMA = 'alx_book_store'
    AND TABLE_NAME = 'Books'
ORDER BY
    ORDINAL_POSITION;

