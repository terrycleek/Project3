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
    #conn = sqlite3.connect("steam_data.db")
    conn = sqlite3.connect("webscraped_games.db")
    cursor = conn.cursor()

    # Fetch all game data from the database
    query = """Select Genre, sum(count_genre) as count_genre
               from(
               SELECT Genre1 as Genre, count(Genre1) as count_genre FROM 'webscraped_games' group by Genre1
               union all
               SELECT Genre2, count(Genre2) FROM 'webscraped_games' group by Genre2
               union all
               SELECT Genre3, count(Genre3) FROM 'webscraped_games' group by Genre3
               union all
               SELECT Genre4, count(Genre4) FROM 'webscraped_games' group by Genre4
               union all
               SELECT Genre5, count(Genre5) FROM 'webscraped_games' group by Genre5
               union all
               SELECT Genre6, count(Genre6) FROM 'webscraped_games' group by Genre6
               union all
               SELECT Genre7, count(Genre7) FROM 'webscraped_games' group by Genre7
               union all
               SELECT Genre8, count(Genre8) FROM 'webscraped_games' group by Genre8
               union all
               SELECT Genre9, count(Genre9) FROM 'webscraped_games' group by Genre9
               union all
               SELECT Genre10, count(Genre10) FROM 'webscraped_games' group by Genre10
               union all
               SELECT Genre11, count(Genre11) FROM 'webscraped_games' group by Genre11
               union all
               SELECT Genre12, count(Genre12) FROM 'webscraped_games' group by Genre12
               union all
               SELECT Genre13, count(Genre13) FROM 'webscraped_games' group by Genre13)
               where Genre not in ('null')
               group by Genre
               order by count_genre desc
               """
    cursor.execute(query)
    games = cursor.fetchall()
    
    # Return the data as JSON
    return jsonify({"games": games})
    
if __name__ == "__main__":
    app.run(debug=True, port=5002)  # Use a different port, e.g., 5002

