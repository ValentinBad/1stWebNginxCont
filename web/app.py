from flask import Flask, jsonify, request
import mysql.connector
import os

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host='db',
        user='user',
        password='password',
        database='counter_db'
    )

@app.route('/counter', methods=['GET'])
def get_counter():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT value FROM counter WHERE id = 1')
    counter = cursor.fetchone()[0]
    conn.close()
    return jsonify(counter=counter)

@app.route('/increment', methods=['POST'])
def increment_counter():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('UPDATE counter SET value = value + 1 WHERE id = 1')
    conn.commit()
    cursor.execute('SELECT value FROM counter WHERE id = 1')
    counter = cursor.fetchone()[0]
    conn.close()
    return jsonify(counter=counter)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
