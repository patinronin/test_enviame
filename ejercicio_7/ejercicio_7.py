
# pip3 install mysqlclient
import MySQLdb

# modify this variables for your own database data 
DB_HOST = 'localhost' 
DB_USER = 'pato' 
DB_NAME = 'prueba' 
DB_PASS = 'patinronincheta'

#cant be 0
adjustment_factor = 100

#connection string 
data = [DB_HOST, DB_USER, DB_PASS, DB_NAME] 

#connecting 
conn = MySQLdb.connect(*data) 

# crate a cursor to execute querys 
cursor = conn.cursor()

# this query return a table with the name, lastname
# country, continent and anual adjustment for the employees 
#with salary < 5000

query = """select employees.id ,
 first_name, last_name,salary,  
 countries.name ,
 continents.name,
 continents.anual_adjustment
from employees 
inner join countries on countries.id = employees.country_id 
inner join continents on countries.continent_id = continents.id
where (salary < '5000');
"""

cursor.execute(query)
records = cursor.fetchall()


#extract the data from the query to calculate the new salary and update 

for record in records: 
	print(record)
	new_salary = int(record[3]) + int(record[3])*int(record[6])/adjustment_factor
	query = 'UPDATE employees SET salary ={} WHERE id = {};'.format(new_salary,record[0])
	cursor.execute(query)


# commit the changes and close connection

cursor.close()
conn.commit()
conn.close()                   

