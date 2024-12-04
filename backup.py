import os
from datetime import date
from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'arnav',
    'database': 'test'
}

def get_db_connection():
    return mysql.connector.connect(**db_config)

def init_database():
#to create a table for events
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS events (
        id INT AUTO_INCREMENT PRIMARY KEY,
        event_name VARCHAR(255) NOT NULL UNIQUE,
        event_date DATE NOT NULL,
        event_location VARCHAR(255) NOT NULL
    )
    ''')
    conn.commit()
    cursor.close()
    conn.close()

def create_event_table(event_name):
#to create a table for each event to store participants
    table_name = event_name
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(f'''
    CREATE TABLE IF NOT EXISTS `{table_name}` (
        id INT AUTO_INCREMENT PRIMARY KEY,
        participant_name VARCHAR(255) NOT NULL,
        participant_email VARCHAR(255) NOT NULL,
        participant_phone VARCHAR(50) NOT NULL
    )
    ''')
    conn.commit()
    cursor.close()
    conn.close()

@app.route('/')
def index():
#to add events "upcoming events" on home page
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM events WHERE event_date >= %s ORDER BY event_date ASC', (date.today(),))
    events = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('index.html', events=events)

@app.route('/create', methods=['POST'])
def create_event():
#creating a new event and adding it to the events table
    event_name = request.form['event_name']
    event_date = request.form['event_date']
    event_location = request.form['event_location']

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('''
    INSERT INTO events (event_name, event_date, event_location)
    VALUES (%s, %s, %s)
    ''', (event_name, event_date, event_location))
    conn.commit()

    create_event_table(event_name)

    cursor.close()
    conn.close()
    return redirect('/')

@app.route('/register', methods=['POST'])
def register_participant():
#to register a participant for an event and add it to the respective event table
    event_name = request.form['event_name']
    participant_name = request.form['participant_name']
    participant_email = request.form['participant_email']
    participant_phone = request.form['participant_phone']

    table_name = event_name

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(f'''
    INSERT INTO `{table_name}` (participant_name, participant_email, participant_phone)
    VALUES (%s, %s, %s)
    ''', (participant_name, participant_email, participant_phone))
    conn.commit()

    cursor.close()
    conn.close()
    return redirect('/')

@app.route('/event/<event_name>')
#to fetch all the participants of an event and display in respective event page 
def view_event_participants(event_name):
    table_name = event_name

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)


    cursor.execute('SELECT * FROM events WHERE event_name = %s', (event_name,))
    event = cursor.fetchone()

    cursor.execute(f'SELECT * FROM `{table_name}`')
    participants = cursor.fetchall()

    cursor.close()
    conn.close()
    return render_template('event_details.html', event=event, participants=participants)

if __name__ == '__main__':
    init_database()
    app.run(debug=True)
