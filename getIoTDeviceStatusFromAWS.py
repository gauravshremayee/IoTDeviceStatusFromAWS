#!/usr/bin/python
import os
import boto3
import subprocess
import datetime
from botocore.exceptions import NoCredentialsError
ACCESS_KEY = 'AKIAYHSZEPGXXXX'
SECRET_KEY = 'OrCJb9Ke0vi3r/8Vb/N66Rsb5g3XXBXXXX'
BUCKET_NAME= 'wittybucket'
CMD_STATUS_FILE='/home/pi/devicestatus.txt'

outputFile=open(CMD_STATUS_FILE,'a')
outputFile.write(str(datetime.datetime.now()))
outputFile.write(str(datetime.datetime.now().time()))
outputFile.write("\n")
def write_command_output(command):
     print("Command is ", command)
     result = subprocess.check_output(command,shell=True)
     print("Command result is",result)
     
     outputFile.write(result)
     print (result)

def read_aws_file(commandfile):
    cmdFile = open(commandfile, 'r')
    cmds = cmdFile.readlines()

    for cmd in cmds:
        cmd=cmd.rstrip()
        write_command_output(cmd)

def upload_to_aws(local_file, bucket, s3_file):
    s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY,
                      aws_secret_access_key=SECRET_KEY)

    try:
        s3.upload_file(CMD_STATUS_FILE, bucket,"s3witty.txt")
        print("Upload Successful")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False

def download_file_from_aws():
    s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY,
                      aws_secret_access_key=SECRET_KEY)
    #try:
    s3.download_file(BUCKET_NAME,'commands.txt','commands.txt')
    #except botocore.exceptions.ClientError as e:
    #    if e.response['Error']['Code'] == "404":
    #        print("The object does not exist.")
    #    else:
    #        raise

#download commands.txt from aws s3
download_file_from_aws()

read_aws_file('/home/pi/commands.txt')

uploaded = upload_to_aws(CMD_STATUS_FILE, BUCKET_NAME , 's3witty.txt')

#uploaded1 = upload_to_aws('/home/pi/devicestatus.txt' , BUCKET_NAME , 'deviceStatus.txt')

download_file_from_aws()

