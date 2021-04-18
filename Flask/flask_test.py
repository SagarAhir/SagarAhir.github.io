import sqlite3
from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/s")
def temp():
    return render_template("form.html", name=name, address=address, contact_no=contact_no)

@app.route("/static/student.html")
def student():
    return render_template("student.html", name=name, address=address, contact_no=contact_no)

conn = sqlite3.connect("DE.db")
cursor = conn.execute("SELECT Name from School")
cursor1 = conn.execute("SELECT Address from School")
cursor2 = conn.execute("SELECT Contact_no from School")

name = []
address = []
contact_no = []

for row in cursor:
    name.append(row)    
for row in cursor1:
    address.append(row)
for row in cursor2:
    contact_no.append(row)

conn.close()
if __name__ == "__main__":
    app.run(debug=True)

