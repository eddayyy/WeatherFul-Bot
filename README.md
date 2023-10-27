<div align="center">
    <img width=35% src="./data/media/Profile Picture.png">
    <h1>Weatherful Bot ☀️</h1>
    <a href="https://twitter.com/WeatherfulBot">
        <img alt="Status" src="https://img.shields.io/badge/Status-Live-brightgreen">
    </a>
    <img alt="Python Version" src="https://img.shields.io/badge/Python-v3.10%2B-blue">
    <img alt="AWS Lambda" src="https://img.shields.io/badge/AWS-Lambda-f4800b">
    <img alt="AWS S3" src="https://img.shields.io/badge/AWS-S3-43985a">
    <img alt="AWS EventBridge" src="https://img.shields.io/badge/AWS-EventBridge-ff00e7">
    <a href="https://opensource.org/licenses/MIT">
        <img alt="License" src="https://img.shields.io/badge/License-MIT-blue.svg">
    </a>
</div>



## Table of Contents
1. [Overview](#overview)
2. [Features](#🚀-features)
3. [Setting up the Development Environment](#🔧-setting-up-the-development-environment)
5. [Demo and Pictures](#demo)
4. [License](#📄-license)

## Overview

Weatherful Bot is a Python-based automated system deployed on AWS Lambda, designed to tweet real-time weather updates for Fullerton, California, bi-hourly. 

## 🚀 Features


#### Location-Specific 
- Tailored weather updates exclusively for Fullerton, California.

#### Real-Time Weather Updates
- **Bi-Hourly Reports**: Stay updated with current weather conditions, tweeted every two hours.
- **Sunrise & Sunset**: Get notified about the sunrise and sunset every morning at 6 AM PST.
- **7-Day Forecast**: Gain insights into the week ahead with a comprehensive 7-Day forecast every Sunday at 12 PM PST.

#### Automated Hashtags 
- Enhance tweet discoverability with categorizing hashtags like `#WeatherUpdate`, `#WeatherForecast`, and `#FullertonWeather`.

## 🔧 Setting up the Development Environment

Follow these steps to set up and deploy the Weatherful Bot:

1. **Clone the Repository**: 
   - Use the command `git clone https://github.com/eddayyy/WeatherFul-Bot` to get the codebase onto your local machine.

2. **Install Requirements**:
   - Navigate to the project directory and run `pip install -r requirements.txt` to install necessary dependencies.

3. **API Configuration**:
   - Obtain API keys for both Twitter and Weatherbit.
   - Save these keys securely, as they'll be necessary for authenticating and making API requests.

4. **Function Modifications**:
   - Modify functions or scripts within the codebase as needed to fit your specific requirements or adjustments.

5. **AWS Deployment**:

   - **Deployment Package**:
     - Prepare a deployment package containing the code along with any dependencies.
     - Compress the deployment package into a zip file.
     - Upload the zipped deployment package to Amazon S3 (Amazon Simple Storage Service).
     - Once uploaded, link the deployment package to the AWS Lambda Function to complete the deployment process.

   - **Environment Variables**:
     - Set necessary environment variables, like the API keys and other configurations, within the Lambda function settings.

   - **Event Sources**:
     - Set up scheduled events using Amazon EventBridge. This will trigger the Lambda function at the times you have scheduled

Remember to always maintain the security of your API keys and any other sensitive data during the entire setup and deployment process.

## Demo 

#### Twitter Profile: 

<img alt="Twitter Profile" width=50% height=100% src="./data/media/Profile Demo.png">

#### Bi-Hourly Tweet Tweet: 
<img alt="Bi-Hourly Tweet" width=50% height=100% src="./data/media/Bi-Hourly-Tweet Demo.png">

#### Sunset / Sunrise Tweet: 
<img alt="Sunset / Sunrise Tweet" width=50% height=100% src="./data/media/Sunrise Sunset Demo.png">

#### Weekly Forecast Tweet: 
<img alt="Weekly Forecast Tweet" width=50% height=100% src="./data/media/Weekly Forecast Demo.png"


## 📄 License

This project is licensed under the MIT License - see [LICENSE.md](LICENSE.md) for details.