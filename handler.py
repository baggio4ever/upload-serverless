# -*- coding: utf-8 -*-
 
import os
import logging
import datetime
import base64
import boto3
import json

logger = logging.getLogger()
logger.setLevel(logging.INFO)
 
s3 = boto3.client('s3')
BUCKET_NAME = os.environ['bucketName']


def saveImage(event, context):
    todaydetail = datetime.datetime.today()
    FILENAME = (todaydetail.strftime("%Y%m%d-%H%M%S") + '.jpg')
 
    dec_save(data = event['body'], FILENAME = FILENAME)
    s3.upload_file('/tmp/' + FILENAME, BUCKET_NAME, FILENAME)
    os.remove('/tmp/' + FILENAME)
 
    responce = {
         "statusCode": 200,
         "body": "Upload Sccessful \n"
    }
    logger.info(responce)
    return responce
 
# ------------ バイナリデータをデコードして/tmpに保存する -------------
def dec_save(data, FILENAME):
    dec_data = base64.b64decode(data)
    f = open('/tmp/' + FILENAME,'wb')
    f.write(dec_data)
    f.close()
    return

