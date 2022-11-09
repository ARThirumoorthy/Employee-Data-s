import sqlite3
con=sqlite3.connect('employee.db')

def insertData(name,age,city):
	qry="insert into employee_table (NAME,AGE,CITY) values (?,?,?) ;"
	con.execute(qry,(name,age,city))
	con.commit()
	print("User Details Added")

def updateData(name,age,city,id):
	qry=" update employee_table set NAME=?, AGE=?, CITY=? where id=?;"
	con.execute(qry,(name,age,city,id))
	con.commit()
	print("User Details Added")

def deleteData(id):
	qry="delete from employee_table where id=?;"
	#con.execute(qry,(id,))
	con.execute(qry,[id])
	con.commit()
	print("User Details Deleted")

def selectData():
	qry="select * from employee_table"
	result=con.execute(qry)
	for row in result: 
		print(row)


	
print("""
1.Insert
2.Update
3.Delete
4.Select
""")
ch=1
while ch==1:
	c=int(input("select your choice:"))
	if(c==1):
		print("Add new record")
		name=input("Enter the Name :")
		age=int(input("Enter the Age :")) 
		city=input("Enter the City:")
		insertData(name,age,city) 
	elif(c==2):
		print("Edit a record")
		id=int(input("Enter the id"))
		name=input("Enter the Name :")
		age=int(input("Enter the Age :")) 
		city=input("Enter the City:")
		updateData(name,age,city,id)
	elif(c==3):
		print("Delete a record")
		id=int(input("Enter the id"))
		deleteData(id)
	elif(c==4):
		print("Print All Record")
		selectData()
	else:
		print("Invalid selection")
	ch=int(input("Enter 1 to continue: "))
print("Thank you")