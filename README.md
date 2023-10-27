<div align="center">
    <img width=35% src="./data/media/Profile Picture.png">
    <h1>Weatherful Bot ☀️</h1>
    <img alt="Python Version" src="https://img.shields.io/badge/Python-v3.10%2B-blue">
    <img alt="AWS Lambda" src="https://img.shields.io/badge/AWS-Lambda-f4800b">
    <img alt="AWS S3" src="https://img.shields.io/badge/AWS-S3-43985a">
    <img alt="AWS EventBridge" src="https://img.shields.io/badge/AWS-EventBridge-ff00e7">
    <a href="https://opensource.org/licenses/MIT">
        <img alt="License" src="https://img.shields.io/badge/License-MIT-blue.svg">
    </a>
</div>

## Table of Contents
- [Overview](#-overview)
- [Features](#-features)
- [Setup and Deployment](#️-setup-and-deployment-or-development-environment)
- [License](#-license)
- [Features and Demo](#features-and-demo-link-to-any-demo-or-visual-guide)

## Overview

Weatherful Bot is a Python-based automated system deployed on AWS Lambda, designed to tweet real-time weather updates for Fullerton, California,  bi-hourly. This repository hosts the code and documentation of Weatherful Bot, providing a convenient way for Twitter users in Fullerton to stay updated on the weather directly through their Twitter feed.

## 🚀 Features

- **Manage Student Grades**: 
    - **Modify Student Grades**: Swiftly adjust and update student grades.
    - **Sort Grades**: Organize student grades for quick insights.
    - **Search for Students**: Efficient student searches using Student ID (SID).

- **Statistical Analysis**: 
    - Generate insights on class performance for specific assignments, such as mean, median, standard deviation, missing assignments, and scores' range.

- **Data Import/Export**: 
    - **Import Students**: Import student data seamlessly from CSV files.
    - **Export Modified Data**: Export updated student data conveniently to a CSV file.

- **User-Friendly Interface**: 
    - Designed for ease of use, ensuring educators can navigate and operate the application efficiently.

- **Extended Features**: (or "Visual Demos", or another appropriate title)
    - For a visual representation of features and demos, check [this link](https://github.com/eddayyy/RA-Assessment/tree/main).

## Tech Stack

- Python 3.11
- AWS Lambda
- Amazon S3 
- Weatherbit Forecast API 
- Twitter Developer API Access

## 🛠️ Setting up the Development Environment

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