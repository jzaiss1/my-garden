from flask import Flask
from flaskext.mysql import MySQL

app = Flask(__name__)
mysql = MySQL(app)

app.config['MYSQL_DATABASE_USER'] = ''
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = ''
app.config['MYSQL_DATABASE_HOST'] = ''

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

if __name__ == "__main__":
    app.run(host='0.0.0.0')