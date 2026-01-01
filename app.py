import os
from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_USER'] = 'db_user'
app.config['MYSQL_PASSWORD'] = os.getenv('DB_PASSWORD', 'zaza2310')
app.config['MYSQL_DB'] = 'employee_db'
app.config['MYSQL_HOST'] = '127.0.0.1'

mysql = MySQL(app)

@app.route('/')
def main():
    return "Flask MySQL App"

@app.route('/employees')
def employees():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM employees")
    rows = cursor.fetchall()
    cursor.close()
    res = "<h1>Employee List</h1><table border='1'><tr><th>ID</th><th>Name</th><th>Position</th><th>Salary</th><th>Date</th></tr>"
    for row in rows:
        res += f"<tr><td>{row[0]}</td><td>{row[1]}</td><td>{row[2]}</td><td>{row[3]}</td><td>{row[4]}</td></tr>"
    res += "</table>"
    return res

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)