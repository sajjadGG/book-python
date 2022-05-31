import sqlite3

# CREATE TABLE IF NOT EXISTS "apollo11" (
#   "datetime" TIMESTAMP,
#   "date" DATE,
#   "time" TIME,
#   "met" INTEGER,
#   "category" TEXT,
#   "event" TEXT
# );

SQL = """

WITH important_categories AS (
    SELECT DISTINCT(category)
    FROM apollo11
    GROUP BY category
    HAVING COUNT(category) < 50
    ORDER BY category ASC
    LIMIT 5
    OFFSET 0
)


SELECT datetime AS dt,
       category,
       event

FROM apollo11

WHERE category != 'DEBUG'
  AND date >= '1969-07-16'
  AND date <= '1969-07-24'
  AND (date = '1969-07-20' OR date = '1969-07-21')
  AND datetime BETWEEN '1969-07-20 20:17:41' AND '1969-07-21 15:00'
  AND event LIKE '%CDR%'
  AND category IS NOT NULL
  AND (category NOT IN ('DEBUG', 'INFO'))
  AND category IN ('CRITICAL', 'ERROR')
  AND category IN important_categories
  AND category IN (

    SELECT DISTINCT(category)
    FROM apollo11
    GROUP BY category
    HAVING COUNT(category) < 50
    ORDER BY category ASC
    LIMIT 5
    OFFSET 0

  ) -- CRITICAL, ERROR


ORDER BY category DESC,
         date ASC NULLS FIRST,
         time ASC NULLS LAST

LIMIT 30
OFFSET 0

"""






"""

"""

print('\n'*3)

DATABASE = 'space.db'

with sqlite3.connect(DATABASE) as db:
    # db.row_factory = sqlite3.Row
    for row in db.execute(SQL):
        print(row)
        # print(dict(row))

print('\n'*3)
