import mysql.connector

conn=mysql.connector.connect(
host = "sql12.freesqldatabase.com",
username= "sql12792572",
password= "5SekwbnJtn",
database= "sql12792572"
)

csr=conn.cursor()