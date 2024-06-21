from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Anushka@123",
    database="temp"
)

@app.route('/')
def index():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM customers")
    customers = cursor.fetchall()
    return render_template('index.html', customers=customers)

@app.route('/customer/<int:id>')
def customer(id):
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM customers WHERE id = %s", (id,))
    customer = cursor.fetchone()
    return render_template('index.html', customers=[customer])  # Pass as a list

@app.route('/transfer', methods=['POST'])
def transfer():
    sender_id = request.form['sender_id']
    receiver_id = request.form['receiver_id']
    amount = float(request.form['amount'])
    
    cursor = db.cursor()
    cursor.execute("UPDATE customers SET balance = balance - %s WHERE id = %s", (amount, sender_id))
    cursor.execute("UPDATE customers SET balance = balance + %s WHERE id = %s", (amount, receiver_id))
    cursor.execute("INSERT INTO transfers (sender_id, receiver_id, amount) VALUES (%s, %s, %s)", (sender_id, receiver_id, amount))
    db.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
