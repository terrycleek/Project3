# Video Game Analysis

---
## Table of Contents

- [Project Description](#project-description)
- [Installation and Instructions](#installation-and-instruction)
- [Datasets Used](#datasets-used)
- [Getting Started](#getting-started)
    - [Usage](#usage)
- [Database](#database)
    - [API](#api)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## Project Description
In the realm of interactive entertainment, the dynamics of PC video games and their corresponding sales have undergone significant transformations over the years. Harnessing the power of data analytics, this project endeavors to unearth invaluable insights into the evolving landscape of video game consumer preferences. By delving into historical sales data and emerging market trends, we aim to chart a data-driven course for the future of the PC video game industry, guiding developers and stakeholders towards informed decisions and innovative strategies that will shape the next generation of gaming experiences.

-**Questions to Ask**
1. What pc game genre is growing the fastest?
2. What is the most popular game genre out in the market?
3. How does price of games affect long term playability?


---
## Installation and Instructions


-**Download Python and the necessary Prerequisites**
Link [Here](https://www.python.org/)

![Python Download Screen](https://docs.python.org/3/_images/win_installer.png)

-Check if Python Installed Properly
 ```sh
   python --version
   ```
-Clone Working Repository
 ```sh
   git clone https://github.com/terrycleek/Project3
   ```
-Install Javascript dependencies
 ```sh
   npm install
   ```
   


---

## Datasets Used

This project relies on a variety of datasets obtained from different sources to provide comprehensive insights into the video game industry. The datasets include:

### Steam Charts DB Web Scraped

- **Source**: [SteamDB](https://steamdb.info/charts/)
- **Description**: Steam Charts DB is a valuable resource for historical and real-time data on games available on the Steam platform. This dataset serves as the backbone of our analysis, providing information on game popularity, player counts, and more.

### CSV Data

- **Source**: Internet-based CSV files
- **Description**: We've sourced additional data from publicly available CSV files found on the internet. These files contain various information related to video games, including user reviews, game ratings, and sales figures.

### IGDB API

- **Source**: [IGDB API](https://api-docs.igdb.com/#getting-started)
- **Description**: The Internet Game Database (IGDB) API is a key component of our project. By accessing this API, we retrieve comprehensive details about video games, including genres, release dates, and user reviews. To use the IGDB API, we followed specific steps to create a Twitch developer account, register our application, and obtain API credentials.

### Steam Web API

- **Source**: [Steam Web Api](https://steamapi.xpaw.me/)
- **Description**: We've incorporated Steam Data API access various data and functionality related to the Steam platform, including information about games, user profiles, user inventories, and more.



---


## Getting Started

## Usage

-**Navigate** to the project directory and run
 ```sh
   python app.py
   ```
   
### Python Flask API

This initializes a Python Flask web application that serves as the backend of our project. It includes the following components:

### Importing Libraries

- Imports the SQLite3 library for database operations.
- Imports essential modules from Flask, a web framework in Python.


### Route for the Website

- Defines a route for the root URL ("/") that serves the website. When a user accesses the root URL, it renders the "index.html" template, creating the main webpage for the project.

### API Endpoint for Retrieving Steam Data

- Defines an API endpoint ("/api/games") that allows clients to retrieve Steam game data.
- This function is executed when the "/api/games" endpoint is accessed. It performs the following tasks:
    - Connects to an SQLite database named "steam_data.db."
    - Executes an SQL query to fetch all game data from the "games" table in the database.
    - Retrieves the fetched data and returns it as JSON, allowing clients to access the game data programmatically.



This Python Flask API serves as the backend for our project, providing a website and an API endpoint for retrieving Steam game data stored in an SQLite database.



## API

### IGDB 

link [Here](https://api-docs.igdb.com/#getting-started)

Account Creation

In order to use IGDB API, you must have a Twitch Account.

![Twitch SignUp](https://www.dummies.com/wp-content/uploads/twitch-channel-setup.jpg)


1. Sign Up with Twitch for a free account
2. Ensure you have Two Factor Authentication enabled
3. Register your application in the Twitch Developer Portal
4. Manage your newly created application
5. Generate a Client Secret by pressing New Secret
6. Take note of the Client ID and Client Secret

The base URL for IGDB is: https://api.igdb.com/v4

### Steam Web Api

-**Create a Steam User Account**
link [Here](https://store.steampowered.com/join)
![Steam Create Acc](https://cdn.vcgamers.com/news/wp-content/uploads/2022/10/Cara-Bikin-Akun-Steam-Melalui-Client.png)
    
-**After creating Account copy down Steam ID #**
![Steam ID](https://gamertweak.com/wp-content/uploads/2022/06/how-to-locate-steam-id.jpg)
    
1. Open the Steam app on your PC or Mac.
2. Sign into your account.
3. Click on your Profile name at the top right section of the screen.
4. Now click on Account Details.
5. You should now see Your Usernames Account. Under that, there will be your Steam ID of 17 digits.
    
-**See Steam Web Documentation** Link [Here](https://steamapi.xpaw.me/)

-**Register for Web API Key**
link [Here](https://steamcommunity.com/dev/apikey)
    

-**Fill out sheet and read documentation**
    

---
## Contributing
Avary Edwards
Terry Cleek

## License

## Contact
