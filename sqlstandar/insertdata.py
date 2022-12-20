import mysql.connector

mydb = mysql.connector.connect(
  host="172.25.171.7",
  port=23306,
  user="root",
  password="p455w0rd",
  database="basis_data"
)

db = mydb.cursor()

sql = "INSERT INTO students (name, nim) VALUES (%s, %s)"
val = ("Baby", "20210801330")
db.execute(sql, val)
mydb.commit()

print(db.rowcount, "berhasil insert")