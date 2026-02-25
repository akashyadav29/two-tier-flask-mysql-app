from flask import Flask, request
import mysql.connector

app = Flask(__name__)

# Database connection function
def get_db():
    return mysql.connector.connect(
        host="mysql-db",
        user="root",
        password="rootpass",
        database="akashdb"
    )

# Home page with Stylish Form
@app.route('/', methods=['GET'])
def form_page():
    return """
    <html>
    <head>
        <title>Akash's Message App 💬</title>
        <style>
            body {
                font-family: 'Arial', sans-serif;
                background: linear-gradient(to right, #6a11cb, #2575fc);
                color: white;
                text-align: center;
                padding-top: 60px;
            }
            h1 {
                font-size: 40px;
                margin-bottom: 20px;
            }
            .card {
                background: white;
                color: #333;
                width: 40%;
                margin: 0 auto;
                padding: 30px;
                border-radius: 15px;
                box-shadow: 0px 4px 20px rgba(0,0,0,0.3);
            }
            input {
                width: 80%;
                padding: 12px;
                font-size: 16px;
                border-radius: 10px;
                border: none;
                outline: none;
                margin-top: 10px;
            }
            button {
                margin-top: 20px;
                padding: 12px 30px;
                font-size: 18px;
                background-color: #2575fc;
                color: white;
                border: none;
                border-radius: 10px;
                cursor: pointer;
                transition: 0.3s;
            }
            button:hover {
                background-color: #6a11cb;
            }
            a {
                display: block;
                margin-top: 20px;
                font-size: 18px;
                color: yellow;
                text-decoration: none;
            }
            a:hover {
                color: #fff;
            }
        </style>
    </head>
    <body>

        <h1>💬 Welcome to Akash's Message App</h1>

        <div class="card">
            <h2>What's on Your Mind 🗄️</h2>
            <form action="/save" method="POST">
                <input name="msg" placeholder="Type your message here..." />
                <br>
                <button type="submit">Save Message 🚀</button>
            </form>

            <a href="/messages">📜 View Saved Messages</a>
        </div>

    </body>
    </html>
    """

# Save message into database
@app.route('/save', methods=['POST'])
def save():
    msg = request.form['msg']
    db = get_db()
    cursor = db.cursor()
    cursor.execute("INSERT INTO messages (msg) VALUES (%s)", (msg,))
    db.commit()

    return """
    <h2 style='font-family:Arial; text-align:center; margin-top:50px;'>
        ✅ Your message has been saved successfully!
    </h2>
    <div style='text-align:center;'>
        <a href='/' style='font-size:22px;'>🔙 Go Back</a>
    </div>
    """

# Show stored messages
@app.route('/messages')
def get_messages():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT msg FROM messages")
    rows = cursor.fetchall()

    html = """
    <html>
    <head>
        <title>Saved Messages 📜</title>
        <style>
            body {
                font-family: Arial;
                background: #f0f0f0;
                padding: 40px;
                text-align: center;
            }
            .msg-box {
                background: white;
                padding: 20px;
                width: 50%;
                margin: 10px auto;
                border-radius: 10px;
                box-shadow: 0px 3px 10px rgba(0,0,0,0.2);
                font-size: 20px;
            }
            a {
                font-size: 22px;
                text-decoration: none;
                color: #2575fc;
            }
        </style>
    </head>
    <body>
        <h1>📜 Saved Messages</h1>
    """

    for r in rows:
        html += f"<div class='msg-box'>💬 {r[0]}</div>"

    html += "<br><a href='/'>🔙 Back</a></body></html>"
    return html


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
