import boto3
import os

# Get credentials from GitHub Secrets
AWS_ACCESS_KEY = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_KEY = os.environ['AWS_SECRET_ACCESS_KEY']

BUCKET_NAME = "automate-file-upload-on-s3"

s3 = boto3.client(
    's3',
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY
)

# Upload index.html
s3.upload_file(
    'index.html',
    BUCKET_NAME,
    'index.html',
    ExtraArgs={'ContentType': 'text/html'}
)

print("✅ Website uploaded successfully to S3!")
