from flask import Flask, jsonify, make_response
import pandas as pd
import requests
import mysql.connector


app = Flask(__name__)

mydb = mysql.connector.connect(
    host= '216.238.104.158',
    user= 'backend_db_usr',
    password= 'LFHOp5KyOA5aXOLw',
    port= 3306,
    database= 'backend_db'
)

mydb.is_connected()

@app.route('/assinatura', methods=['GET'])
def get_assinature():
    my_cursor = mydb.cursor()
    my_cursor.execute('SELECT * FROM calculos')
    my_calcs = my_cursor.fetchall()
    columns = [desc[0] for desc in my_cursor.description]
    calcs = [dict(zip(columns, row)) for row in my_calcs]

    my_cursor.close()
    return make_response(
        jsonify(calcs), 200
        )

app.run()