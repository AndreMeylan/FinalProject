# FinalProject

---

### Section B - Team 6
## Team Members
- Umberto Cirilli
- Iñaki Galdiano
- Ting Jin
- Joel Pascal Kömen
- Olaf Odinn Lesniak
- André Olivier Meylan

---

# Diabetes Risk Prediction on AWS

## Project Overview

This project focuses on addressing a significant healthcare concern: the early identification of diabetes risk. Given the substantial direct healthcare costs associated with diabetic patients, which account for a considerable portion of the Spanish National Health System expenditure, there's an urgent need to mitigate the prevalence of this condition. Our solution leverages AWS services to deploy a machine learning model capable of predicting an individual's risk of developing diabetes based on various physical health indicators. This early detection system aims to facilitate prompt lifestyle adjustments and interventions, potentially reducing the financial and health burden of diabetes.

## Problem Statement

Diabetic patients incur high direct healthcare costs, significantly impacting the Spanish National Health System's budget. Early detection of diabetes risk states and subsequent lifestyle modifications can dramatically reduce the incidence of this condition. Our goal is to deploy a predictive model that identifies individuals at risk of developing diabetes, thus alleviating the economic strain on healthcare systems.

## AWS Architecture

### Architecture Diagram

#### Overview

The repository includes a detailed architecture diagram that outlines the workflow and interaction between various AWS services used in our diabetes risk prediction model.

![Architecture Diagram](https://github.com/AndreMeylan/FinalProject/blob/main/%20architecture_diagram.png)

##### Workflow Description

The architecture diagram illustrates the following key processes:

1. **Data Ingestion:** Raw data uploaded to an S3 bucket is picked up by a SageMaker notebook instance for processing.
   
2. **Model Training:** The SageMaker notebook conducts preprocessing steps on the data and uses it to train the machine learning model.
   
3. **Model Deployment:** The trained model is deployed to a SageMaker endpoint for generating predictions based on new data.
   
4. **Prediction Handling:** A Lambda function retrieves new predictions from the S3 bucket and writes them to a DynamoDB table for persistent storage.
   
5. **API Integration (Future Implementation):** An API Gateway will be set up to trigger a Lambda function for making prediction requests, with the future potential to streamline the prediction retrieval process.

##### Security and Access Control

The diagram also highlights the use of AWS Identity and Access Management (IAM) to manage permissions and access control across all services, ensuring secure and authorized operations within the workflow.

##### Current Status and Future Enhancements

This diagram represents the current state of our AWS-based architecture while also indicating future enhancements such as the implementation of an API Gateway for improved request handling. As we continue to develop and refine our model, we anticipate further optimizations and additions to this architecture.

---

# Repository Contents Summary

In this repository, you will find the following files, each contributing to our project's goal of predicting diabetes risk using AWS services:

### `ML_Model_Team_6_Final.ipynb`

This Jupyter Notebook is the core of our project, detailing the entire process from data retrieval to model training and evaluation. Key aspects include:

- **AWS Integration:** Demonstrates setting up AWS configurations for effective data management, with a focus on utilizing S3 for data storage and retrieval.
- **Data Pipeline:** Establishes a comprehensive pipeline for data preprocessing, including data loading, cleaning, and transformation, ensuring the data is in the proper format for model training.
- **Model Preparation:** Guides through the process of preparing the data for the model, including splitting the dataset into training, validation, and testing sets and applying necessary transformations.

This notebook encapsulates our approach to deploying a machine learning model on AWS, aimed at early detection of diabetes risk.

---

## AWS Lambda Functions for Diabetes Risk Prediction

### Directory Overview

This repository includes dedicated directories for AWS Lambda functions that are integral to managing and processing data for our diabetes risk prediction model.

#### `Diabetes_storage` Directory

Contains the Lambda function that interacts with our main data storage, the `Diabetes_storage` S3 bucket.

- **`lambda_function.py`:** The Python script set up as an AWS Lambda function to handle data ingestion and management tasks triggered by new file uploads in the `Diabetes_storage` S3 bucket.
- **`text event.txt`:** A mock event file that simulates the S3 `put` event for testing the Lambda function without an actual file upload.

#### `PredictionResult` Directory

This folder is designed to hold the results of our diabetes prediction model and includes:

- **`lambda_function.py`:** A Python script that acts upon the trigger from the `PredictionResult` S3 bucket to process the incoming prediction results.
- **`test event.txt`:** A test event file containing a JSON object that mimics the Lambda trigger for a new result file upload, allowing us to ensure that our function correctly handles new prediction data.

### Usage Instructions

For both Lambda functions:

#### Deployment

1. Log in to your AWS Management Console and navigate to the Lambda section.
2. Click "Create function," choose "Author from scratch," and fill out the basic information including the function name and runtime (Python).
3. In the "Function code" area, upload the respective `lambda_function.py` file for the function you are setting up.
4. Under the "Designer" section, set the appropriate S3 bucket as the trigger, configuring it to react to object creation events.
5. Save your Lambda function.

#### Testing

1. In the AWS Lambda console, open the function you wish to test.
2. Click on the "Test" tab and configure a new test event using the content from the `text event.txt` file corresponding to the function.
3. Name your test event and click "Test" to simulate the S3 event and verify the function's response.

Each Lambda function is tailored to respond to specific S3 bucket events, ensuring that our data flow is managed correctly throughout the diabetes risk prediction pipeline.

---
## Challenges and Troubleshooting

### Issue with Pandas Library in AWS Lambda

While developing the `PredictionResult` Lambda function, we intended to preprocess the data using the Pandas library. However, we faced the following challenges:

1. **Pandas Not Preinstalled:** AWS Lambda's default Python environment does not come with Pandas preinstalled.
   
2. **Virtual Environment and Packaging:** To circumvent this, we installed Pandas in a virtual environment and created a deployment package. This package included our function code and the Pandas library.

3. **Deployment Package Size Limitation:** When attempting to upload our file to the Lambda function, we encountered a size constraint. AWS Lambda requires the unzipped deployment package to be smaller than 262,144,000 bytes (250 MB).

4. **Error Upon Uploading to S3 Bucket:** We tried to use an S3 bucket to store and reference the ZIP file. However, when the Lambda function attempted to use the Pandas library from the S3 bucket, we were met with the error: "Unzipped size must be smaller than 262144000 bytes."

5. **Alternatives to Pandas:** Given the file size limitation, we explored alternative methods to replace Pandas. Unfortunately, these attempts did not yield a successful outcome.

### Current Status

We are actively seeking solutions to handle large file preprocessing within the constraints of AWS Lambda's deployment package size limit. This challenge remains open, and we welcome contributions and ideas on how to resolve it.


