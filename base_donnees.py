import sqlite3
import datetime

def initialiser_bdd():
    conn = sqlite3.connect('detections.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS detections (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT,
            timestamp TEXT
        )
    ''')
    conn.commit()
    conn.close()

def enregistrer_detection(nom):
    conn = sqlite3.connect('detections.db')
    c = conn.cursor()
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    c.execute('INSERT INTO detections (nom, timestamp) VALUES (?, ?)', (nom, timestamp))
    conn.commit()
    conn.close()

def recuperer_detections():
    conn = sqlite3.connect('detections.db')
    c = conn.cursor()
    c.execute('SELECT nom, timestamp FROM detections ORDER BY id DESC')
    resultats = c.fetchall()
    conn.close()
    return resultats
