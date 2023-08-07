import boto3

s3 = boto3.client('s3')

s3.upload_file('C:/Users/suman/transformed_data.csv', 'data-08', 'samdata transformed.CSV')
