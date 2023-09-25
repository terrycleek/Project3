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
In the realm of interactive entertainment, the dynamics of video game systems and their corresponding sales have undergone significant transformations over the years. Harnessing the power of data analytics, this project endeavors to unearth invaluable insights into the evolving landscape of video game consumer preferences. By delving into historical sales data and emerging market trends, we aim to chart a data-driven course for the future of the video game industry, guiding developers and stakeholders towards informed decisions and innovative strategies that will shape the next generation of gaming experiences.

Questions to Ask
1. What pc game genre is gorwing the fastest?
2. What is the most popular game genre out in the market?
3. How does price of games affect long term playability?


---
## Installation and Instructions


Download Python and the necessary Prerequisites
Link [Here](https://www.python.org/)

![Python Download Screen](https://docs.python.org/3/_images/win_installer.png)

Check if Python Installed Properly
 ```sh
   python --version
   ```
Clone Working Repository
 ```sh
   git clone https://github.com/terrycleek/Project3
   ```
Install Javascript dependencies
 ```sh
   npm install
   ```
   

aa

---

## Datasets Used

This project relies on a variety of datasets obtained from different sources to provide comprehensive insights into the video game industry. The datasets include:

### Steam Charts DB

- **Source**: [SteamDB](https://steamdb.info/charts/)
- **Description**: Steam Charts DB is a valuable resource for historical and real-time data on games available on the Steam platform. This dataset serves as the backbone of our analysis, providing information on game popularity, player counts, and more.

### CSV Data

- **Source**: Internet-based CSV files
- **Description**: We've sourced additional data from publicly available CSV files found on the internet. These files contain various information related to video games, including user reviews, game ratings, and sales figures.

### IGDB API

- **Source**: [IGDB API](https://api-docs.igdb.com/#getting-started)
- **Description**: The Internet Game Database (IGDB) API is a key component of our project. By accessing this API, we retrieve comprehensive details about video games, including genres, release dates, and user reviews. To use the IGDB API, we followed specific steps to create a Twitch developer account, register our application, and obtain API credentials.

### Steam Community Market Data

- **Source**: [Steam Community Market](https://store.steampowered.com/join)
- **Description**: We've incorporated data from the Steam Community Market to gain insights into the in-game items and virtual economies of popular games. To access this data, we created Steam user accounts and generated Web API keys.

Incorporating these diverse datasets allows us to paint a complete picture of the video game industry, from player preferences and game sales. Our project combines data from multiple sources to offer a comprehensive analysis that can benefit game developers, industry analysts, and gamers alike.


---

## Getting Started

## Usage


## Datasets used
Used Steam Charts DB datasets that were webscraped using Selenium
Downloaded csv sheets from other online sources.
Potentially using datasets obtained from API's

1. Steam Charts DB
  [Here](https://steamdb.info/charts/)
![Web scrape Steamdb]
Steam Web API
steamapi.xpaw.me

IGDB API

---
## Database 

SQLite

--

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

### Steam Community Market

Create a Steam User Account
link [Here](https://store.steampowered.com/join)
![Steam Create Acc](https://cdn.vcgamers.com/news/wp-content/uploads/2022/10/Cara-Bikin-Akun-Steam-Melalui-Client.png)
    
After creating Account copy down Steam ID #
![Steam ID](https://gamertweak.com/wp-content/uploads/2022/06/how-to-locate-steam-id.jpg)
    
1. Open the Steam app on your PC or Mac.
2. Sign into your account.
3. Click on your Profile name at the top right section of the screen.
4. Now click on Account Details.
5. You should now see Your Usernames Account. Under that, there will be your Steam ID of 17 digits.
    
See Steam Web Documentation. Link [Here](https://steamcommunity.com/dev)

Register for Web API Key
link [Here](https://steamcommunity.com/dev/apikey)
    
Use steamapi.xpaw. Link [Here](https://steamapi.xpaw.me/)
Fill out sheet and read documentation
    

---
## Contributing
Avary Edwards
Terry Cleek

## License

## Contact
