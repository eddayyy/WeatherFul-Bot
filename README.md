# Weatherful Bot 🐦☀️

## Overview

Weatherful Bot is a Python-based automated system that tweets real-time weather updates for specific cities every 2 hours. This repository contains all the code and documentation needed to set up your own instance of Weatherful Bot. It aims to provide a convenient way for Twitter users to get updated weather information directly in their Twitter feed.

<!-- ![Weatherful Bot Demo](demo.png) -->

## Features

- **Real-Time Weather Updates**: Tweets the current weather every 2 hours.
- **Automated Mentions**: Capability to reply to users asking for weather updates (Feature in development).
- **Automated Hashtags**: Uses hashtags like `#WeatherUpdate`, `#WeatherForecast` to categorize tweets.
- **Retweet Weather Alerts**: Planned feature to retweet urgent weather warnings from official sources.

## Prerequisites

- Python 3.x
- Tweepy Library
- OpenWeatherMap API Key
- Twitter Developer Account

## Installation & Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/weatherful-bot.git
    ```

2. Navigate to the project directory and install the required packages:
    ```bash
    cd weatherful-bot
    pip install -r requirements.txt
    ```

3. Rename `.env.sample` to `.env` and fill in your OpenWeatherMap API key and Twitter API credentials.

4. Run the bot:
    ```bash
    python weatherful_bot.py
    ```

## Usage

Simply follow Weatherful Bot on Twitter to get the weather updates. Future features will include the ability to request weather updates for your city via mentions.

## Data Protection and Compliance

Weatherful Bot does not collect, store, or analyze personal data from Twitter users. It complies with Twitter's Developer Agreement and Policy, as well as all relevant data protection laws.

## Contributing

Feel free to fork this repository and submit pull requests. For major changes, please open an issue first to discuss the proposed changes.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
