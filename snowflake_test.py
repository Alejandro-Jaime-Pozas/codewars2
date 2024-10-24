import pyodbc

conn = pyodbc.connect('DSN=SNOWFLAKE_DEFAULT;UID=jjaimeal@jci.com;PWD=@Ajpgp17626604')
cursor = conn.cursor()

# cursor.execute("SELECT CURRENT_VERSION()")
cursor.execute("SELECT * FROM GLOBAL_PRODUCTS_STAGE.STT_CONFIG LIMIT 5")
rows = cursor.fetchall()
print(rows)

cursor.close()
conn.close()
