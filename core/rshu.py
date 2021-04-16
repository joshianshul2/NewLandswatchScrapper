from sqlalchemy import create_engine
import psycopg2 
import io
import pandas as pds
import testdb
import pandas.io.sql as psql

engine = create_engine('postgresql+psycopg2://LandScrap:w87zhetrhgxdvo21@db-postgresql-nyc3-22046-do-user-8994632-0.b.db.ondigitalocean.com:25060/LandScrap', pool_recycle=3600);
dbConnection    = engine.connect();


# alchemyEngine   = create_engine('postgresql+psycopg2://LandScrap:w87zhetrhgxdvo21@db-postgresql-nyc3-22046-do-user-8994632-0.b.db.ondigitalocean.com:25060/LandScrap', pool_recycle=3600);

#  dialect+driver://username:password@host:port/database

# Connect to PostgreSQL server

# dbConnection    = alchemyEngine.connect();


# df = ("SELECT state,county, SUM(price)/SUM(acres) AS NETPRICE FROM core_propertymaster GROUP BY state,county  limit 200",dbConnection) 
# df.head(0).to_sql('core_avgmaster', engine, if_exists='replace',index=False) #drops old table and creates new empty table
# conn = engine.raw_connection()
# cur = dbConnection.cursor()
# output = io.StringIO()
# df.to_csv(output, sep='\t', header=False, index=False)
# output.seek(0)
# contents = output.getvalue()
# cur.copy_from(output, 'core_avgmaster', null="") # null values become ''
# dbConnection.commit()




df = pds.read_sql("select * from \"core_avgmaster\" limit 10", dbConnection);


# pds.set_option('display.expand_frame_repr', False);

# print(dataFrame);
# conn = engine.raw_connection()
# cur = conn.cursor()
# output = io.StringIO()
# df.to_csv(output, sep='\t', header=False, index=False)
# output.seek(0)
# contents = output.getvalue()
# cur.copy_from(output, 'core_avgmaster', null="") # null values become ''
# conn.commit()

# dataFrame.commit()



# # Close the database connection

# dbConnection.close();


df.head(0).to_sql('core_avgmaster', engine, if_exists='replace',index=False) #drops old table and creates new empty table

conn = engine.raw_connection()
cur = conn.cursor()
output = io.StringIO()
df.to_csv(output, sep='\t', header=False, index=False)
output.seek(0)
contents = output.getvalue()
cur.copy_from(output, 'core_avgmaster', null="") # null values become ''
conn.commit()