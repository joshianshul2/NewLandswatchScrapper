import psycopg2

import pandas as pds
import testdb

from sqlalchemy import create_engine

import pandas.io.sql as psql




 # username = LandScrap
# password = w87zhetrhgxdvo21
# host = db-postgresql-nyc3-22046-do-user-8994632-0.b.db.ondigitalocean.com
# port = 25060
# database = LandScrap
# sslmode = require

# Create an engine instance

alchemyEngine   = create_engine('postgresql+psycopg2://LandScrap:w87zhetrhgxdvo21@db-postgresql-nyc3-22046-do-user-8994632-0.b.db.ondigitalocean.com:25060/LandScrap', pool_recycle=3600);

#  dialect+driver://username:password@host:port/database

# Connect to PostgreSQL server

dbConnection    = alchemyEngine.connect();



# chunksize = 500
# i=0
# j=0
# # data_frame  = pds.read_sql("select count(*) from \"core_propertymaster\"", dbConnection,chunksize);
# for df in pds.read_sql("select count(*) from \"core_propertymaster\"", dbConnection,chunksize=chunksize,iterator=True) :
#         print("Hello",df)


# Read data from PostgreSQL database table and load into a DataFrame instance

# chunk_size = 10000
# offset = 0
# dfs = []
# i=1
# while True:
#   sql = "SELECT * FROM core_propertymaster  limit %d offset %d " % (chunk_size,offset) 
#   print("Query Fetched")
#   dfs.append(psql.read_sql(sql,dbConnection))
#   print("Chunk",i)
#   i+=1
#   offset += chunk_size
#   if len(dfs[-1]) < chunk_size:
#     break
# full_df = pds.concat(dfs)
# for i in dfs:
#     print(i)
chunk_size = 10000
offset = 0
dfs = []
i=1
while True:
#   sql = "SELECT * FROM core_propertymaster  limit %d offset %d " % (chunk_size,offset) 
  sql = "SELECT * FROM core_propertymaster INNER JOIN core_avgmaster ON core_avgmaster.price <= core_propertymaster.price limit %d offset %d " % (chunk_size,offset)
  print("Query Fetched")
  dfs.append(psql.read_sql(sql,dbConnection))
  print(dfs[0])
  print("Chunk",i)
  i+=1
  offset += chunk_size
  if len(dfs[-1]) < chunk_size:
    break
full_df = pds.concat(dfs)
for i in dfs:
    print(i)


 

pds.set_option('display.expand_frame_repr', False);

 

# Print the DataFrame

# print(dataFrame);

 

# Close the database connection

dbConnection.close();