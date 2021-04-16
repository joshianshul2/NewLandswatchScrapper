import pymysql

# Connect to the database
connection = pymysql.connect(host='db-postgresql-nyc3-22046-do-user-8994632-0.b.db.ondigitalocean.com',
                             user='LandScrap',
                             password='w87zhetrhgxdvo21',
                             db='LandScrap')

cursor = connection.cursor()

# Create a new record
sql = "INSERT INTO 'core_avgmaster' ('state', `Ename`, `DeptID`, `Salary`, `Dname`, `Dlocation`) VALUES (%s, %s, %s, %s, %s, %s)"

# Execute the query
cursor.execute(sql, ('rishu','Kabir',2,5000,'IT','New Delhi'))

# the connection is not autocommited by default. So we must commit to save our changes.
connection.commit()

# Create a new query that selects the entire contents of `employee`
sql = "SELECT * FROM 'core_avgmaster' "
cursor.execute(sql)

# Fetch all the records and use a for loop to print them one line at a time
result = cursor.fetchall()
for i in result:
    print(i)

connection.close()