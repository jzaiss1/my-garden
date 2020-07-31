# Test DB connection and sample data

import mysql.connector
import csv
import json

mydb = mysql.connector.connect(
  host="",
  user="",
  passwd="",
  database='mygarden'
)

mycursor = mydb.cursor()

def convertPhoto(imageFile):
    # Convert plant photo to binary
    with open(imageFile, 'rb') as file:
        binaryData = file.read()
    return binaryData

def processPlant():
# Testing with a sample file 
# Need to replace with json payload from API  
  with open('samples/sample-plants.json') as f:
    data = json.load(f)

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

processPlant()
