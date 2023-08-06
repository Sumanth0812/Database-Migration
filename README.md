
```
# Python and AWS Database Migration

This project demonstrates the migration of data from a local SQL Server database to an AWS S3 bucket using Python, Docker, pandas, NumPy, and AWS Glue. Additionally, it includes the automation of data crawling using AWS Glue.

## Table of Contents

- [Overview](#overview)
- [Set up the Development Environment](#set-up-the-development-environment)
- [Task 1 - Set up a Database using Docker](#task-1---set-up-a-database-using-docker)
- [Task 2 - Data Migration to AWS](#task-2---data-migration-to-aws)
- [Task 3 - Automate Data Crawler using AWS Glue](#task-3---automate-data-crawler-using-aws-glue)
- [Task 4 - Documentation and Presentation](#task-4---documentation-and-presentation)
- [Submission](#submission)

## Overview

Briefly describe the objective of the project and what it aims to achieve. Mention the technologies and tools used, along with any significant features or highlights.

## Set up the Development Environment

1. **Install Docker:** Visit the official Docker website (https://www.docker.com) and download Docker for your operating system. Install Docker on your machine.

2. **Install Python:** Visit the official Python website (https://www.python.org) and download the latest version of Python 3.x for your operating system. Install Python on your machine.

3. **Install Required Libraries:** Use pip to install the necessary Python libraries: pandas, NumPy, boto3, and AWS SDK for Python (boto3).

```bash
pip install pandas numpy boto3
```

## Task 1 - Set up a Database using Docker

1. **Create a Docker container for SQL Server:** Pull the SQL Server Docker image and create a container with the necessary configuration.

2. **Set up tables and schemas:** Connect to the SQL Server database inside the Docker container using SQL Server Management Studio or any other SQL client. Create the required tables with appropriate schemas.

3. **Insert sample data:** Write SQL statements to insert sample data into the tables.

## Task 2 - Data Migration to AWS

1. **Write a Python script:** Create a Python script that uses pandas and NumPy to connect to the SQL Server database and retrieve the data from the tables. Transform the data if needed.

2. **Create an AWS S3 bucket:** Log in to your AWS account and create an S3 bucket to store the transformed data.

3. **Upload data to S3:** Use the AWS SDK for Python (boto3) to upload the transformed data as CSV or Parquet files to the S3 bucket.

## Task 3 - Automate Data Crawler using AWS Glue

1. **Set up AWS Glue:** Log in to your AWS account and navigate to AWS Glue. Create a new database if needed.

2. **Create an AWS Glue crawler:** Configure the Glue crawler to automatically detect the data in the S3 bucket and create a Glue table.

3. **Schedule the Glue crawler:** Set up a schedule for the Glue crawler to run periodically (e.g., daily, hourly) to capture any new data in the S3 bucket and update the Glue table accordingly.

## Output - 
The final output will be a fully functional data migration pipeline that transfers data from a local SQL Server database to an AWS S3 bucket and automates the data crawling process using AWS Glue. The project will be well-documented, and the presentation will help showcase the project's key features and implementation details.

The successful completion of this assignment will demonstrate proficiency in using Python, Docker, SQL, AWS services, data migration techniques, and automation with AWS Glue.
## Good Luck.

