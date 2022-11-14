# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 19:10:11 2022

@author: ankit
"""

import boto3

conn = boto3.client('s3')
s3_resource = boto3.resource('s3')
my_bucket = 'my_bucket'
bucket_prefix = 'bucket_prefix/'
dest_file = 'destination_path/'
file_ext = '.mmdb'

contents = conn.list_objects(Bucket=my_bucket, Prefix=bucket_prefix)['Contents']
for f in contents:
    #print(f['Key'],str(f['LastModified']).replace(" ", "-"))
    if f['Key'].endswith('.mmdb') and str(f['LastModified']).startswith('2022'):
        #print(f['Key'])
        datetime = str(f['LastModified']).replace(" ", "-")
        print(datetime)
        filename=f['Key'].split("/")[-1]
        filename = filename.split('.mmdb')[0]
        #print(filename)
        print(dest_file+str(datetime)+'_'+str(filename)+str(file_ext))
        s3_resource.Bucket(my_bucket).download_file(f['Key'], dest_file+str(datetime)+'_'+str(filename)+str(file_ext))