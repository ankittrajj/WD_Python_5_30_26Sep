import  mysql.connector as c
con = c.connect(host = 'localhost',
               user = 'root',
               passwd = 'Ankit@8285',
                database = 'std')

cursor = con.cursor()

name = input("Enter your name")
age = int(input("Enter your age"))
marks = int(input("Enter your marks"))

query = "Insert into bb values('{}',{},{})".format(name,age,marks)
cursor.execute(query)
con.commit()
print("Data enterd successfully!!")



