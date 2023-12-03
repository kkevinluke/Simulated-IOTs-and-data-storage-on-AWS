# Simulated Ship Data Upload to AWS Services

This project demonstrates the simulation of ship sensor data using AWS IoT, the trigger of a Lambda function upon receiving IoT data, and the storage of this sensor data into an AWS S3 bucket for further analysis.

## Components:

1. **Simulating Ship Data (Code 1):**
   - The `simulate_ship_data.py` script generates simulated ship sensor data and sends it to AWS IoT Core using the AWS IoT Python SDK.

2. **Lambda Function (Code 3):**
   - The `store_sensor_data_lambda.py` script is a Lambda function triggered by AWS IoT Core events. It extracts the received IoT data and stores it as JSON files in an S3 bucket.

3. **Downloading Data from S3 (Code 2):**
   - The `download_from_s3.py` script demonstrates how to download data from the AWS S3 bucket to the local environment using the Boto3 library.

## Folder Structure:

- `scripts/`: Contains scripts for simulating ship data and downloading from S3.
  - `simulate_ship_data.py`: Simulates ship sensor data and sends it to AWS IoT.
  - `download_from_s3.py`: Downloads data from S3 to the local environment.
- `lambda_function/`: Contains Lambda function code triggered by AWS IoT.
  - `store_sensor_data_lambda.py`: Lambda function to store IoT data in an S3 bucket.
- `README.md`: This file explaining the project and usage instructions.

## Usage:

1. **Simulate Ship Data:**
   - Execute `simulate_ship_data.py` to simulate ship sensor data and send it to AWS IoT Core.

2. **Lambda Function Configuration:**
   - Create a Lambda function in the AWS Lambda console.
   - Copy and paste the code from `store_sensor_data_lambda.py` into the Lambda function.
   - Configure the trigger to be AWS IoT Core.
   
3. **AWS S3 Bucket Setup:**
   - Create an S3 bucket on AWS where the sensor data will be stored.
   - Adjust the bucket name in `store_sensor_data_lambda.py` (Code 3) and `download_from_s3.py` (Code 2) accordingly.

4. **Download Data from S3:**
   - Execute `download_from_s3.py` to download data from the S3 bucket to the local environment.

## Requirements:
- Python 3.x
- AWS IoT Python SDK
- Boto3 library for AWS S3 operations

## Note:
- Ensure AWS credentials are properly configured for accessing IoT Core and S3 services.
- Modify the code with your specific AWS IoT endpoint, S3 bucket name, and file paths as necessary.

