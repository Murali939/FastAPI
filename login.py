from flask import Flask, jsonify
from db_connect import get_connection

app = Flask(__name__)

@app.route("/")
def home():
    return "Flask server is running!"

@app.route("/data")
def data():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM hmsuser")  # CHANGE THIS
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(rows)

if __name__ == "__main__":
    app.run(debug=True)
