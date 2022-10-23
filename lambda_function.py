import os
import boto3
import csv
from io import StringIO
from serializer.serializer import DataSerializer
from orm_db.orm_db import add_and_commit_db


def lambda_handler(event, context):
    obj = access_s3(event)

    csvreader = read_obj_s3(obj)

    list_obj = create_list_obj(csvreader)

    add_and_commit_db(list_obj)

    return {
        'statusCode': 200
    }


def create_list_obj(list_rows):
    list_obj = []
    for row in list_rows:
        obj = DataSerializer(row).create_obj()
        list_obj.append(obj)
    return list_obj


def access_s3(event):
    queryString = event['queryStringParameters']
    s3 = boto3.client('s3')
    try:
        obj = s3.get_object(Bucket=queryString['bucket_name'], Key=queryString['object_key'])
    except Exception as e:
        print(e)
    return obj


def read_obj_s3(obj):
    data = obj['Body'].read().decode('ISO-8859-1')
    files = StringIO(data)
    csvreader = csv.DictReader(files, delimiter=';')
    return csvreader