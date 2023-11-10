#Exercise 13.1
from flask import Flask, redirect, url_for, request

app= Flask(__name__)

@app.route('/prime_number/<number>')
def check_prime(number):
    number = int(number)
    primeInteger = True

    for i in range(2,number):
        if(number % i == 0):
            primeInteger = False

    response = {
        "Number":number,
        "isPrime":primeInteger
    }
    return response

if __name__ == '__main__':
    app.run(use_reloader=True,host='127.0.0.1', port=5000, debug=True)


#Exercise 13.2
import mysql.connector

from flask import Flask, redirect, url_for, request

def icao_search(icao):
    sql = "SELECT ident AS 'ICAO',name AS 'Name',municipality AS 'Location' FROM airport WHERE ident = '"+icao+"'"
    cursor=connection.cursor(dictionary=True)
    cursor.execute(sql)
    result=cursor.fetchall()
    return result

connection=mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='0528',
    autocommit=True
)

app=Flask(__name__)
@app.route('/airport/<icao>')
def get_info_with_icao(icao):
    result = icao_search(icao)[0]
    response={
        "ICAO":result["ICAO"],
        "Name":result["Name"],
        "location":result["Location"]
    }

    return response

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)
