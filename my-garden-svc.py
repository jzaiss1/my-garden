# Test DB connection and sample data

import mysql.connector
import csv
import json

mydb = mysql.connector.connect(
  host="mygarden-db-instance.c0uwy4mfszo8.us-east-2.rds.amazonaws.com",
  user="mygarden_user",
  passwd="11IOIifCQo!",
  database="mygarden"
)

mycursor = mydb.cursor()

def convertPhoto(imageFile):
    # Convert plant photo to binary
    with open(imageFile, 'rb') as file:
        binaryData = file.read()
    return binaryData

def processPlant(data):
  plants = data['plants']
  for plant in plants:
    p = plant['name']
    w = plant['watering']
    h = plant['hardiness']
    t = plant['totalSize']
    f = plant['fertilization']
    s = plant['spacing']
    d = plant['details']
    b = plant['blooms']
    z = plant['zones']
    sql = "INSERT INTO Plants (plantName, watering, hardiness, totalSize, fertilization, spacing, details, blooms, zones)"
    sql += "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = (p, w, h, t, f, s, d, b, z)
    mycursor.execute(sql, val)
    mydb.commit()

def queryAllPlants():
    mycursor = mydb.cursor()

    columns = "plantName, watering, hardiness, totalSize, fertilization, spacing, details, blooms, zones"
    qry =  "SELECT {} ".format(columns)

    table = "Plants"
    qry += "FROM {} ".format(table)

    # filt = "name=''"
    # qry += "WHERE {} ".format(filt)

    #options = "LIMIT 0, 10000"
    options = ""
    qry += "{}".format(options)

    mycursor.execute(qry)

    myresult = mycursor.fetchall()

    for x in myresult:
      print(x)

with open('samples/sample-plants.json') as f:
  data = json.load(f)

processPlant(data)

# queryAllPlants()
