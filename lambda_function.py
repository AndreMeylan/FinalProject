import boto3
import csv
from io import StringIO

# Initialize the S3 and DynamoDB clients
s3_client = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')

# Change to the new DynamoDB table name
table = dynamodb.Table('DiabetesPR_storage')

def lambda_handler(event, context):
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    file_key = event['Records'][0]['s3']['object']['key']
    
    try:
        csv_file_obj = s3_client.get_object(Bucket=bucket_name, Key=file_key)
        csv_file_content = csv_file_obj['Body'].read().decode('utf-8')
        csv_reader = csv.DictReader(StringIO(csv_file_content))
        
        with table.batch_writer() as batch:
            for row in csv_reader:
                # Convert PolicyHolderID to an integer, providing a default value if missing
                policy_holder_id = int(row.get('PolicyHolderID', 0))

                # Construct the DynamoDB item, ensuring it includes the partition key
                dynamodb_item = {'PolicyHolderID': policy_holder_id}

                # Add other data from the CSV row to the DynamoDB item
                for key, value in row.items():
                    if key != 'PolicyHolderID':
                        dynamodb_item[key] = value

                # Add the item to the batch
                batch.put_item(Item=dynamodb_item)
        
        return {'statusCode': 200, 'body': f'Successfully processed {file_key}.'}
    except Exception as e:
        print(e)
        return {'statusCode': 500, 'body': f'Error processing {file_key}.'}
