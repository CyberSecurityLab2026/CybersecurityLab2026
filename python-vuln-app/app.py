from flask import Flask, request
import sqlite3
import hashlib

app = Flask(__name__)

@app.route("/")
def home():
    return "Vulnerable Flask App Running"

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    # Weak cryptography (MD5)
    hashed = hashlib.md5(password.encode()).hexdigest()

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # SQL Injection vulnerability
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{hashed}'"
    cursor.execute(query)
    result = cursor.fetchone()

    if result:
        return "Login successful"
    return "Login failed"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
