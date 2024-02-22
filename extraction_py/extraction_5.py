import json
import boto3
import pandas as pd
import requests

s3 = boto3.client('s3')

def lambda_handler(event, context):
    bucket ='semistructuredata'
    url = 'https://data.cityofnewyork.us/resource/kpav-sd4t.json'
    
    
    params = {'$limit': 1000, '$offset':4000}
    response = requests.get(url,params=params)
    data = response.json()


    df = pd.DataFrame(data)
    df.drop_duplicates(inplace=True)
    
    
    csv_data = df.to_csv(index=False)
    fileName = 'data5.csv'
    uploadByteStream = bytes(csv_data.encode('utf-8'))
    s3.put_object(Bucket=bucket, Key=fileName, Body=uploadByteStream)
    print('Put Complete')