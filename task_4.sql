USE alx_book_store
SELECT 
 COLUMN_NAME, COLUMN_TYPE 
FROM 
 INFORMATION_SCHEMA.COLUMNS
WHERE 
 TABLE_NAME ='Books'
 AND TABLE_SCHEMA = 'alx_book_store';

