from flask import Flask, render_template, request
from flaskext.mysql import MySQL
from dbconn import *

app = Flask(__name__)
mysql = MySQL(app)

mygardendb = MyGardenDB()

app.config['MYSQL_DATABASE_USER'] = mygardendb.MYSQL_DATABASE_USER
app.config['MYSQL_DATABASE_PASSWORD'] = mygardendb.MYSQL_DATABASE_PASSWORD
app.config['MYSQL_DATABASE_DB'] = mygardendb.MYSQL_DATABASE_DB
app.config['MYSQL_DATABASE_HOST'] = mygardendb.MYSQL_DATABASE_HOST

mysql = MySQL()
mysql.init_app(app)
conn = mysql.connect()
cur = conn.cursor()

@app.route("/")
def hello():
    return "<h1 style='color:blue'>Hello There!</h1>"

@app.route("/style")
def style():
    return "<h1 style='color:green'>Style Guide</h1>"

@app.route('/plants')
def users():
    cur.execute("SELECT * FROM Plants")
    rv = cur.fetchall()
    return str(rv)

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == "POST":
        plant = request.form['plant']
        # search by author or book
        cur.execute("SELECT * from Plants WHERE plantName LIKE %s OR details LIKE %s", (plant, plant))
        conn.commit()
        data = cur.fetchall()
        # all in the search box will return all the tuples
        if len(data) == 0 and plant == 'all': 
            cur.execute("SELECT * from PlantsBook")
            conn.commit()
            data = cur.fetchall()
        return render_template('search.html', data=data)
    return render_template('search.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0')
