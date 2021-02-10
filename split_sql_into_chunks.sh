#!/bin/bash
# From high performance MySQL.
# Need to lookup the do_query function from the book.
rows_affected = 0
do {
 rows_affected = do_query(
   "DELETE FROM messages WHERE created < DATE_SUB(NOW(),INTERVAL 3 MONTH)
   LIMIT 10000"
 )
} while rows_affected > 0
