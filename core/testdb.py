import psycopg2
import pandas as pd
import sys
# Connection parameters, yours will be different
param_dic = {
    "host"      : "db-postgresql-nyc3-22046-do-user-8994632-0.b.db.ondigitalocean.com",
    "database"  : "LandScrap",
    "user"      : "LandScrap",
    "password"  : "w87zhetrhgxdvo21",
    "port"      : "25060",

}



# username = LandScrap
# password = w87zhetrhgxdvo21
# host = db-postgresql-nyc3-22046-do-user-8994632-0.b.db.ondigitalocean.com
# port = 25060
# database = LandScrap
# sslmode = require


def connect(params_dic):
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params_dic)
    except (Exception, psycopg2.DatabaseError) as error:
        print("AJ")
        print(error)
        print("Hello")
        sys.exit(1) 
    print("Connection successful")
    return conn

a=connect(param_dic)
print(a)