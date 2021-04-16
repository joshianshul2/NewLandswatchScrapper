from sqlalchemy import create_engine
import psycopg2
import io
import psycopg2 as pg
import pandas.io.sql as psql
import pandas as pd

# engine = create_engine('postgresql+psycopg2://LandScrap:w87zhetrhgxdvo21@db-postgresql-nyc3-22046-do-user-8994632-0.b.db.ondigitalocean.com:25060/LandScrap', pool_recycle=3600);
#
# dbConnection =engine.connect();
#
# dfs = []
# def anji(dfs):
#     return dfs
#
# def show():
#     # Alert()
#     # if request.POST.
#     chunk_size = 60000
#     offset = 0
#
#     i=0
#     while True:
#         sql = "SELECT * FROM core_propertymaster  limit %d offset %d " % (chunk_size,offset)
# #       sql = "SELECT * FROM core_propertymaster WHERE core_avgmaster.Finale <= core_propertymaster.price limit %d offset %d " % (chunk_size,offset)
#         print("Query Fetched from anji")
#         dfs.append(psql.read_sql(sql,dbConnection))
#         print("Chunk rishu",i)
#         # i+=1
#         print(dfs[i])
#         anji(dfs[i])
#         i+=1
#         offset += chunk_size
#         if len(dfs[-1]) < chunk_size:
#             break
#         full_df = pd.concat(dfs)
    # for i in dfs:
    #     print(i)
    # return dfs


#
# show()
# print("Successfully")
# rishu=anji(dfs)
# print("Rishu RUI",rishu)
#

# def show2():
#     # Alert()
#     # if request.POST.
#     chunk_size = 60000
#     offset = 0
#     dfs = []
#     i=0
#     while True:
#         sql = "SELECT * FROM core_propertymaster  limit 10 "
#         # % (chunk_size,offset)
# #       sql = "SELECT * FROM core_propertymaster WHERE core_avgmaster.Finale <= core_propertymaster.price limit %d offset %d " % (chunk_size,offset)
#         print("Query Fetched from anji")
#         dfs.append(psql.read_sql(sql,dbConnection))
#         print("Chunk rishu",i)
#         # i+=1
#         print(dfs[i])
#         i+=1
#         # offset += chunk_size
#         if len(dfs[-1]) < chunk_size:
#             break
#         full_df = pd.concat(dfs)
#     for i in dfs:
#         print(i)
#     return dfs

# a=show2()
# print(type(a))
# print("Rishu",a)

# import pandas as pd
# import pyodbc
# #
# # conn = pyodbc.connect('Driver={SQL Server};'
# #                       'Server=RON\SQLEXPRESS;'
# #                       'Database=TestDB;'
# #                       'Trusted_Connection=yes;')
# #
# #
# #
# # sql_query = pd.read_sql_query('''
# #                               select * from TestDB.dbo.Person
# #                               '''
# #                               ,conn) # here, the 'conn' is the variable that contains your database connection information from step 2
# #
# # df = pd.DataFrame(sql_query)
# # df.to_csv (r'C:\Users\Ron\Desktop\export_data.csv', index = False) # place 'r' before the path name to avoid any errors in the path

# assign a variable that contains a string of your credentials
credentials = "postgresql+psycopg2://LandScrap:w87zhetrhgxdvo21@db-postgresql-nyc3-22046-do-user-8994632-0.b.db.ondigitalocean.com:25060/LandScrap"
# read in your SQL query results using pandas
dataframe = pd.read_sql("""
            SELECT * FROM core_propertymaster 
            """, con = credentials)
# return your first five rows
dataframe.head()