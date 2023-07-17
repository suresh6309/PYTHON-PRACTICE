import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="123456789",
  database="suresh"
)

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM clg")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
