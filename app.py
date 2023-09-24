# Python Flask API
import sqlite3
from flask import Flask, jsonify, render_template


# Initialize Flask
app = Flask(__name__)


@app.route("/")
def website():
    return render_template("index.html")


# Define an API endpoint to retrieve Steam Data
@app.route("/api/games", methods=["GET"])
def get_games():
    conn = sqlite3.connect("steam_data.db")
    cursor = conn.cursor()

    # Fetch all game data from the database
    cursor.execute("SELECT * FROM games")
    games = cursor.fetchall()
    
    # Return the data as JSON
    return jsonify({"games": games})
    
if __name__ == "__main__":
    app.run(debug=True, port=5002)  # Use a different port, e.g., 5002

