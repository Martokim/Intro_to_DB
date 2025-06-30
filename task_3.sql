"""
Write a script that list all the tables in alx_book_store in your MySQL server.

The name of the file should be task_3.sql
The database name will be passed as argument of mysql command
"""
SELECT * FROM information_schema.tables
WHERE table_schema = 'alx_book_store';
-- The above query retrieves all tables from the 'alx_book_store' database