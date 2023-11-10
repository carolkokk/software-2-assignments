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
        "Number": number,
        "isPrime": primeInteger
    }
    return response

if __name__ == '__main__':
    app.run(use_reloader=True,host='127.0.0.1', port=5000, debug=True)
