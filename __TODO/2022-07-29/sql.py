import sqlite3


DATABASE = 'sql.db'

SQL = """
WITH important_categories AS (
    SELECT DISTINCT(category)
    FROM apollo11
    GROUP BY category
    HAVING COUNT(category) < 50
) -- CTE - Common Table Expression

SELECT datetime AS dt,
       category,
       event
FROM apollo11
WHERE datetime BETWEEN '1969-07-20 20:00' AND '1969-07-21 12:00'
  AND category IN ('CRITICAL', 'WARNING', 'ERROR')
  AND category IN (

    SELECT DISTINCT(category)
    FROM apollo11
    GROUP BY category
    HAVING COUNT(category) < 50

  )
  AND category IN important_categories
  AND category == 'CRITICAL'
  AND event LIKE '%CDR%'
ORDER BY datetime ASC,
         category DESC
LIMIT 100
OFFSET 0

"""


with sqlite3.connect(DATABASE) as db:
    for row in db.execute(SQL):
        print(row)
