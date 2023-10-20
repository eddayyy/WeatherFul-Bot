<script src="https://code.iconify.design/iconify-icon/1.0.7/iconify-icon.min.js"></script>

<h1 style="justify-conten: center; font-size: 55px; paddng-top: 15px; padding-bottom: 15px;">Weatherful Bot <iconify-icon icon="openmoji:twitter"></iconify-icon> <iconify-icon icon="meteocons:clear-day-fill"></iconify-icon></h1> 



## Overview

Weatherful Bot is a Python-based automated system deployed on AWS Lambda, designed to tweet real-time weather updates for Fullerton, California,  bi-hourly. This repository hosts the code and documentation of Weatherful Bot, providing a convenient way for Twitter users in Fullerton to stay updated on the weather directly through their Twitter feed.

## Features

- **Location-Specific**: Tailored weather updates for Fullerton, California.
- **Real-Time Weather Updates**: 
    - Tweets the current weather bi-hourly.
    - Tweets the sunrise and sunset every morning at 6 AM PST.
    - Tweets a 7-Day forecast every Sunday at 12 PM PST.
- **Automated Hashtags**: Utilizes hashtags like `#WeatherUpdate`, `#WeatherForecast`, and `#FullertonWeather` to categorize tweets.

## Tech Stack

- Python 3.11
- AWS Lambda
- Amazon S3 
- Weatherbit Forecast API 
- Twitter Developer API Access

## Deployment

Weatherful Bot is deployed on AWS Lambda, which allows it to run code in response to events without provisioning or managing servers. This serverless architecture is cost-effective and scales automatically by adjusting its capacity in response to incoming traffic.

### AWS Lambda Configuration

1. **Deployment Package**: 
   - Prepare a deployment package containing the code along with any dependencies.
   - Compress the deployment package into a zip file.
   - Upload the zipped deployment package to Amazon S3 (Amazon Simple Storage Service).
   - Once uploaded, link the deployment package to the AWS Lambda Function to complete the deployment process.
2. **Environment Variables**: Necessary environment variables like API keys and other configurations are set within the Lambda function settings.
3. **Event Sources**: Scheduled events are set up using Amazon EventBridge to trigger the Lambda function every other hour, every morning at 6 AM PST, and every Sunday at 12 PM PST.


## Usage

To receive weather updates for Fullerton, simply follow [WeatherfulBot on Twitter](https://twitter.com/WeatherfulBot) and turn on notifications. 

## Data Protection and Compliance

Weatherful Bot adheres to a strict data protection policy, ensuring it does not collect, store, or analyze personal data from Twitter users. Compliance with Twitter's Developer Agreement and Policy, as well as all relevant data protection laws, is a priority.

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE.md](LICENSE.md) file for details.
