from psycopg2 import connect, extensions


autocommit = extensions.ISOLATION_LEVEL_AUTOCOMMIT

con = connect(
    database='jitguru',
    user='postgres',
    host='localhost',
    port='5432'
)

print(con.status)
con.set_isolation_level(autocommit)
cursor = con.cursor()
# cursor.execute("SET AUTOCOMMIT = ON")

