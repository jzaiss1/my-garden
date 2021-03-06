from flask import Flask, render_template, request
from flaskext.mysql import MySQL
from dbconn import *
import json

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
    return render_template('home.html')

@app.route("/style")
def style():
    return render_template('style-guide.html')

@app.route("/create")
def create():
    return render_template('create.html')

@app.route("/update")
def update():
    return render_template('update.html')

@app.route("/dig")
def dig():
    return render_template('dig.html')

@app.route('/api/plants')
def plants():
    cur.execute("SELECT * FROM Plants")
    rv = cur.fetchall()
    row_headers=[x[0] for x in cur.description] #this will extract row headers
    json_data=[]
    for result in rv:
        json_data.append(dict(zip(row_headers,result)))
    return json.dumps(json_data)

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == "POST":
        plant = request.form['plant']
        # search by plantName
        cur.execute("SELECT * from Plants WHERE plantName LIKE %s", (plant))
        conn.commit()
        data = cur.fetchall()
        # all in the search box will return all the tuples
        if len(data) == 0 and plant == 'all':
            cur.execute("SELECT * from Plants")
            conn.commit()
            data = cur.fetchall()
        return render_template('search.html', data=data)
    return render_template('search.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0')
