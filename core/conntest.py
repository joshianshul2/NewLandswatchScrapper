import psycopg2 as pg
import pandas.io.sql as psql
import pandas as pd
import testdb

conn = testdb.connect
print(conn)
# connection = pg.connect("host='102.153.103.22' dbname=dbtest user=admin password='passwords'")
# df = psql.DataFrame("SELECT count(*) FROM core_propertymaster", conn)
# Df1=pd.DataFrame(columns=[‘Email’])
# df = pd.read_sql_query('select count(*) from core_propertymaster',con=conn)
print(df)
import pyodbc
import pandas as pd


# Prepare sql query
psql = "SELECT state FROM core_propertymaster LIMIT 100" 
cursor = conn.cursor()
# Execute cursor
cursor.execute(psql)
# Fetch all the records
tuples = cursor.fetchall()
# list of columns
cols = list(core_propertymaster.columns)
core_propertymaster = pd.DataFrame(tuples,columns=cols) 
# Print few records
print(core_propertymaster.head())
# Close the cursor
cursor.close()
# Close the connection
conn.close()

# conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\Ron\Desktop\testdb.accdb;')

# SQL_Query = pd.read_sql_query(
# "select state from core_propertymaster", conn)

# df = pd.DataFrame(SQL_Query)
# # ,'product_price_per_unit','units_ordered','revenue'])
# print (df)


# # product_price_per_unit,
# # units_ordered,
# # ((units_ordered) * (product_price_per_unit)) AS revenue