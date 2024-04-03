# We tried to make the preprocess, but pandas library is not preinstalled so we 
# created installed pandas in the virtual environment and we created a zip file 
# with the pandas library to upload it from the zip file. We wanted to make the preprocess 
# of the file but the file was too heavy so we created a S3 bucket to upload the
# zip but then when we tried to upload it from the S3 bucket into this lambda 
# function(PredictionResult), we had this error: Unzipped size must be smaller
# than 262144000 bytes. At this point, we did not know how to solve the error 
# and we started trying replace pandas unsuccesfully.

import json
import boto3
import pandas as pd
import io
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder

# Initialize clients
sagemaker_runtime = boto3.client('sagemaker-runtime')
s3 = boto3.client('s3')

def lambda_handler(event, context):
    try:
        # The API Gateway event is assumed to pass the S3 key in the 'body'
        key = json.loads(event['body'])['s3_key']
        bucket = 'api-ec2'  # Specify the S3 bucket name

        # Get the CSV file from S3
        response = s3.get_object(Bucket=bucket, Key=key)
        csv_file = response['Body'].read().decode('utf-8')
        
        # Load CSV data into a DataFrame
        data = pd.read_csv(io.StringIO(csv_file))
        
        # Define your preprocessors and column transformer as you have them
        # Preprocess the data
        preprocessed_data = preprocessor.transform(data)
        preprocessed_df = pd.DataFrame(preprocessed_data, columns=numerical_cols + list(preprocessor.named_transformers_['cat'].named_steps['onehot'].get_feature_names(categorical_cols)))
        
        # Convert DataFrame to CSV format for SageMaker
        csv_buffer = io.StringIO()
        preprocessed_df.to_csv(csv_buffer, header=False, index=False)
        csv_data = csv_buffer.getvalue()
        
        # Send the preprocessed CSV data to the SageMaker endpoint
        response_from_sagemaker = sagemaker_runtime.invoke_endpoint(
            EndpointName='sagemaker-xgboost-2024-04-02-17-46-16-966',
            ContentType='text/csv',
            Body=csv_data
        )
        
        # Process SageMaker's response
        result = response_from_sagemaker['Body'].read().decode('utf-8')
        
        # Store the prediction result back in S3 under the results directory
        result_key = f'results/{key}'
        s3.put_object(Bucket=bucket, Key=result_key, Body=result)
        
        return {
            'statusCode': 200,
            'body': json.dumps(f'Prediction successful. Results stored in: {result_key}')
        }
        
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error processing request: {str(e)}')
        }
