# Test DB connection and sample data

import mysql.connector
import csv
import json

with open('samples/sample-plants.json') as f:
  data = json.load(f)

plants = data['plants']
for plant in plants:
  print(plant['name'])