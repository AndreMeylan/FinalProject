# FinalProject
---
### Section B - Team 6
## Team Members
- 
-
- 
-
-
- 

---

# Diabetes Risk Prediction on AWS

## Project Overview

This project focuses on addressing a significant healthcare concern: the early identification of diabetes risk. Given the substantial direct healthcare costs associated with diabetic patients, which account for a considerable portion of the Spanish National Health System expenditure, there's an urgent need to mitigate the prevalence of this condition. Our solution leverages AWS services to deploy a machine learning model capable of predicting an individual's risk of developing diabetes based on various physical health indicators. This early detection system aims to facilitate prompt lifestyle adjustments and interventions, potentially reducing the financial and health burden of diabetes.

## Problem Statement

Diabetic patients incur high direct healthcare costs, significantly impacting the Spanish National Health System's budget. Early detection of diabetes risk states and subsequent lifestyle modifications can dramatically reduce the incidence of this condition. Our goal is to deploy a predictive model that identifies individuals at risk of developing diabetes, thus alleviating the economic strain on healthcare systems.

### AWS Architecture

![AWS Architecture Diagram]( put here the link once we have it)

---

# Repository Contents Summary

In this repository, you will find the following files, each contributing to our project's goal of predicting diabetes risk using AWS services:

## `ML_Model_Team_6_Final.ipynb`

This Jupyter Notebook is the core of our project, detailing the entire process from data retrieval to model training and evaluation. Key aspects include:

- **AWS Integration:** Demonstrates setting up AWS configurations for effective data management, with a focus on utilizing S3 for data storage and retrieval.
- **Data Pipeline:** Establishes a comprehensive pipeline for data preprocessing, including data loading, cleaning, and transformation, ensuring the data is in the proper format for model training.
- **Model Preparation:** Guides through the process of preparing the data for the model, including splitting the dataset into training, validation, and testing sets and applying necessary transformations.

This notebook encapsulates our approach to deploying a machine learning model on AWS, aimed at early detection of diabetes risk.

---

## `lambda_function.py`

This Python script is intended for deployment as an AWS Lambda function. The function's primary purpose is to interact with AWS S3, performing data management tasks upon the triggering of specific events. Key functionalities include:

- **S3 Event Handling:** The function is triggered by events in an S3 bucket, such as the upload of new data files, to initiate processing.
- **Data Transfer:** It contains logic to copy the data from a source bucket to a destination bucket, facilitating the flow of data within the AWS ecosystem.
- **Error Handling:** The function is robustly designed with error handling to ensure graceful failure and provide informative error messages in case of exceptions.

This Lambda function is a crucial component of our data processing pipeline, ensuring seamless data movement and management for our diabetes risk prediction model.

