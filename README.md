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
1. [Overview](#-overview)
2. [Features and Demo](#features-and-demo)
3. [Setting up the Development Environment](#-setting-up-the-development-environment)
4. [License](#-license)

## 🌟 Overview

Weatherful Bot is a Python-based automated system deployed on AWS Lambda, designed to tweet real-time weather updates for Fullerton, California, bi-hourly. 

## **Features and Demo**

### Feature 1: Twitter Profile
- **Description**: Provide users with clean profile landing page, give a clear description of the bots purpose along with the bots tweet schedule. 

    - **Screenshot**: 

        ![Feature 1 Screenshot](./data/media/Profile%20Demo.png)

### Feature 2: Bi-Hourly Tweet Tweet
- **Description**: Tweet the weather every other hour in the following format, keeping the tweets clear and concise. Along with a few emojis to make the tweet a little nicer to look at. 

    - **Screenshot**: 

        ![Feature 2 Screenshot](./data/media/Bi-Hourly-Tweet%20Demo.png)

### Feature 3: Sunset / Sunrise Tweet 
- **Description**: Everyday at 6am the bot will tweet the sunrise and sunset times for that specific day. The tweet is well structured for easy readability and concise for clarity. 

    - **Screenshot**: 

        ![Feature 3 Screenshot](./data/media/Sunrise%20Sunset%20Demo.png)

### Feature 4: Weekly Forecast Tweet
- **Description**: Every Sunday at 12 PM PST the bot will tweet the 7-day forecast for the upcoming days. The tweet is formatted so that it distinguishes the type of weather that will occurr on specific days (cloudy, rainy, sunny, etc.).

    - **Screenshot**: 

        ![Feature 4 Screenshot](./data/media/Weekly%20Forecast%20Demo.png)
## 🛠️ Setting up the Development Environment

Follow these steps to set up and deploy the Weatherful Bot:

1. **Clone the Repository**: 
   - Use the command `git clone https://github.com/eddayyy/WeatherFul-Bot` to clone the repository.

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

## 📄 License

This project is licensed under the MIT License - see [LICENSE.md](LICENSE.md) for details.