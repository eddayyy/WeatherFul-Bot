# Weatherful Bot 🐦☀️

## Overview

Weatherful Bot is a Python-based automated system that tweets real-time weather updates specific to Fullerton, California, every hour. This repository contains all the code and documentation needed to set up your own instance of Weatherful Bot. It aims to provide a convenient way for Twitter users in Fullerton to stay updated on the weather directly through their Twitter feed.


## Features

- **Location-Specific**: Provides weather updates specifically for Fullerton, California.
- **Real-Time Weather Updates**: Tweets the current weather every hour.
- **Automated Mentions**: Capability to reply to users asking for weather updates in Fullerton (Feature in development).
- **Automated Hashtags**: Uses hashtags like `#WeatherUpdate`, `#WeatherForecast`, and `#FullertonWeather` to categorize tweets.
- **Retweet Weather Alerts**: Planned feature to retweet urgent weather warnings that pertain to Fullerton.

## Tech Stack

- Python 3.x
- AWS Lambda - Serverless Computing
- Tweepy Library
- Weatherbit Forecast API 
- Twitter Developer API Access

## Installation & Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/eddayyy/weatherful-bot.git
    ```

2. Navigate to the project directory and install the required packages:
    ```bash
    cd weatherful-bot
    pip install -r requirements.txt
    ```

3. Create a `.env` file and fill in your Weatherbit API key and Twitter API credentials for your location's weather tracking.

4. Run the bot:
    ```bash
    python main.py
    ```

## Usage

To receive weather updates for Fullerton, simply follow [WeatherfulBot on Twitter](https://twitter.com/WeatherfulBot) and turn on notifications. 

## Data Protection and Compliance

Weatherful Bot does not collect, store, or analyze personal data from Twitter users. It complies with Twitter's Developer Agreement and Policy, as well as all relevant data protection laws.

## Contributing

Feel free to fork this repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE.md](LICENSE.md) file for details.
