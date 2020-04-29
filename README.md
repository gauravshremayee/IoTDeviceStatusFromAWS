# IoTDeviceStatusFromAWS
Run Commands on IoT From AWS and Get the Status

This Script Get the Command file from AWS uploaded by User and then execute the command mentioned in the file.
Each line should contain only ne command


# Cron job runs this python script every minute 
# enter below line in crontab file
# crontab -e
* * * * * /home/pi/getDeviceStatus.py

# content of commands.txt file to be uploaed to aws
command1
command2
command3
command4

