# Final Project - Diabetes Risk Prediction on AWS
## Section B - Team 6

---

## Table of Contents
1. [Team Members](#team-members)
2. [Project Overview](#project-overview)
3. [Problem Statement](#problem-statement)
4. [Architecture Diagram](#architecture-diagram)
5. [Repository Contents Summary](#repository-contents-summary)
6. [AWS Lambda Functions for Diabetes Risk Prediction](#aws-lambda-functions-for-diabetes-risk-prediction)
7. [Challenges and Troubleshooting](#challenges-and-troubleshooting)
8. [Future Development Roadmap](#future-development-roadmap)

---

<a name="team-members"></a>
## Team Members
- Umberto Cirilli
- Iñaki Galdiano
- Ting Jin
- Joel Pascal Kömen
- Olaf Odinn Lesniak
- André Olivier Meylan

---

<a name="project-overview"></a>
## Project Overview

This project focuses on addressing a significant healthcare concern: the early identification of diabetes risk. Given the substantial direct healthcare costs associated with diabetic patients, which account for a considerable portion of the Spanish National Health System expenditure, there's an urgent need to mitigate the prevalence of this condition. Our solution leverages AWS services to deploy a machine learning model capable of predicting an individual's risk of developing diabetes based on various physical health indicators. This early detection system aims to facilitate prompt lifestyle adjustments and interventions, potentially reducing the financial and health burden of diabetes.

---

<a name="problem-statement"></a>
## Problem Statement

Diabetic patients incur high direct healthcare costs, significantly impacting the Spanish National Health System's budget. Early detection of diabetes risk states and subsequent lifestyle modifications can dramatically reduce the incidence of this condition. Our goal is to deploy a predictive model that identifies individuals at risk of developing diabetes, thus alleviating the economic strain on healthcare systems.

---

<a name="architecture-diagram"></a>
## Architecture Diagram

### Overview

The repository includes a detailed architecture diagram that outlines the workflow and interaction between various AWS services used in our diabetes risk prediction model.

![Architecture Diagram](https://github.com/AndreMeylan/FinalProject/blob/main/%20architecture_diagram.png)

#### Workflow Description

The architecture diagram illustrates the following key processes:

1. **Data Ingestion:** Raw data uploaded to an S3 bucket is picked up by a SageMaker notebook instance for processing.
   
2. **Model Training:** The SageMaker notebook conducts preprocessing steps on the data and uses it to train the machine learning model.
   
3. **Model Deployment:** The trained model is deployed to a SageMaker endpoint for generating predictions based on new data.
   
4. **Prediction Handling:** A Lambda function retrieves new predictions from the S3 bucket and writes them to a DynamoDB table for persistent storage.
   
5. **API Integration (Future Implementation):** An API Gateway will be set up to trigger a Lambda function for making prediction requests, with the future potential to streamline the prediction retrieval process.

#### Security and Access Control

The diagram also highlights the use of AWS Identity and Access Management (IAM) to manage permissions and access control across all services, ensuring secure and authorized operations within the workflow.

#### Current Status and Future Enhancements

This diagram represents the current state of our AWS-based architecture while also indicating future enhancements such as the implementation of an API Gateway for improved request handling. As we continue to develop and refine our model, we anticipate further optimizations and additions to this architecture.

---

<a name="repository-contents-summary"></a>
## Repository Contents Summary

In this repository, you will find the following files, each contributing to our project's goal of predicting diabetes risk using AWS services:

### `ML_Model_Team_6_Final.ipynb`

This Jupyter Notebook is the core of our project, detailing the entire process from data retrieval to model training and evaluation. Key aspects include:

- **AWS Integration:** Demonstrates setting up AWS configurations for effective data management, with a focus on utilizing S3 for data storage and retrieval.
- **Data Pipeline:** Establishes a comprehensive pipeline for data preprocessing, including data loading, cleaning, and transformation, ensuring the data is in the proper format for model training.
- **Model Preparation:** Guides through the process of preparing the data for the model, including splitting the dataset into training, validation, and testing sets and applying necessary transformations.

This notebook encapsulates our approach to deploying a machine learning model on AWS, aimed at early detection of diabetes risk.

### AWS Lambda Functions for Diabetes Risk Prediction

### Directory Overview

This repository includes dedicated directories for AWS Lambda functions that are integral to managing and processing data for our diabetes risk prediction model.

### `Diabetes_storage` Directory

Contains the Lambda function that interacts with our main data storage, the `Diabetes_storage` S3 bucket.

- **`lambda_function.py`:** The Python script set up as an AWS Lambda function to handle data ingestion and management tasks triggered by new file uploads in the `Diabetes_storage` S3 bucket.
- **`text event.txt`:** A mock event file that simulates the S3 `put` event for testing the Lambda function without an actual file upload.

### `PredictionResult` Directory

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

<a name="challenges-and-troubleshooting"></a>
## Challenges and Troubleshooting

### Issue with Pandas Library in AWS Lambda

While developing the `PredictionResult` Lambda function, we intended to preprocess the data using the Pandas library. However, we faced the following challenges:

1. **Pandas Not Preinstalled:** AWS Lambda's default Python environment does not come with Pandas preinstalled.
   
2. **Virtual Environment and Packaging:** To circumvent this, we installed Pandas in a virtual environment and created a deployment package. This package included our function code and the Pandas library.

3. **Deployment Package Size Limitation:** When attempting to upload our file to the Lambda function, we encountered a size constraint. AWS Lambda requires the unzipped deployment package to be smaller than 262,144,000 bytes (250 MB).

4. **Error Upon Uploading to S3 Bucket:** We tried to use an S3 bucket to store and reference the python file. However, when the Lambda function attempted to use the Pandas library from the S3 bucket, we were met with the error: "Unzipped size must be smaller than 262144000 bytes."

5. **Alternatives to Pandas:** Given the file size limitation, we explored alternative methods to replace Pandas. Unfortunately, these attempts did not yield a successful outcome.

### Current Status

We are actively seeking solutions to handle large file preprocessing within the constraints of AWS Lambda's deployment package size limit. This challenge remains open, and we welcome contributions and ideas on how to resolve it.

---

<a name="future-development-roadmap"></a>
## Future Development Roadmap

### To-Do List

As we strive to enhance the current infrastructure and capabilities of our diabetes prediction model, we are prioritizing the following tasks:

1. **Pandas Library Integration:** We are exploring solutions to integrate the Pandas library within our AWS Lambda function without exceeding the package size limit. Potential strategies include the use of AWS Lambda Layers and alternative lightweight data processing libraries.

2. **API Connectivity:**
    - **Implement an API Gateway:** We plan to set up an API Gateway to provide a secure and robust interface for handling prediction requests and integrating with other systems.
    - **Connect Lambda with API Gateway:** Our goal is to establish a seamless connection between AWS Lambda functions and the API Gateway, facilitating efficient data flow and management.

These immediate action items are aimed at resolving current limitations and setting the foundation for future enhancements.

### Future Technical Improvements

Looking beyond the immediate to-do list, we intend to implement the following technical improvements to the diabetes prediction model:

- **Refining Model Metrics:** Ongoing monitoring and optimization of model metrics will ensure we avoid overfitting and maintain high predictive accuracy.

- **Advanced Fine-Tuning:** Iterative fine-tuning processes, utilizing sophisticated techniques, will be conducted to progressively enhance model performance.

- **Diversifying Model Portfolio:** We will explore building separate models for different demographic groups and experiment with a range of machine learning models to improve predictive performance.

- **Innovative Feature Engineering:** The adoption of advanced feature engineering techniques will be investigated to unlock further predictive insights within our data.

### Future Business Recommendations

From a business standpoint, our model's deployment aligns with strategic initiatives aimed at reducing healthcare costs and improving patient outcomes:

- **Data Quality and Consistency:** It is essential to maintain high standards of data quality, with healthcare professionals ensuring consistent and accurate data recording.

- **Inclusion of Predictive Features:** Incorporating additional risk factors, such as smoking history, into the model is critical to enhancing its predictive accuracy and utility.

- **Cost-Effective Deployment:** Leveraging the AWS platform, we aim to demonstrate that our model can be deployed efficiently, offering a cost-effective solution for large-scale health systems.

### Long-Term Considerations

Our vision for long-term development includes:

- **Comprehensive Data Collection:** The successful implementation of the model is contingent upon the collection of comprehensive and reliable patient data.

- **Professional Training:** Healthcare professionals must receive training to ensure data is recorded consistently and accurately.

- **Feature Expansion:** Adding key features known to influence diabetes risk, such as smoking history, will improve the model's predictive power.

By addressing these technical and business aspects, we aim to deliver a model that not only excels in accuracy and efficiency but also provides significant value to the healthcare system.

*Note: This roadmap is based on current model performance and projected healthcare trends. As the model is deployed and more data become available, these recommendations may evolve to reflect new insights and opportunities.*
