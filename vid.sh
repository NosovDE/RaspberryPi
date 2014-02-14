#!/bin/bash

while true;
do

backupdate=$(date +%Y.%m.%d)
backuptime=$(date +%H.%M.%S)
savedir="/home/pi/$backupdate/"

mkdir -p $savedir

echo "---------------------------------"
echo "Video.. $backupdate-$backuptime.avi"

###########################################################################################
# RASPISTILL Befehl um die Kamera anzusprechen

#/opt/vc/bin/raspivid -w 1920 -h 1080 -fps 30 -t 20000 -o $savedir/$backupdate-$backuptime.avi
/opt/vc/bin/raspivid --intra 10 -n -v -w 800 -h 600 -fps 24 -t 20000 -awb fluorescent -o $savedir/$backupdate-$backuptime.avi
###########################################################################################

echo "Photo.."

for i in {0..5}
do
  backuptime=$(date +%H.%M.%S)
  filename="$backupdate-$backuptime"

  ###########################################################################################
  # RASPISTILL Befehl um die Kamera anzusprechen

  # /opt/vc/bin/raspistill -w 2592 -h 1944 -q 100 -sh 10 -awb horizon -vf -p -f -o $savedir$filename.jpg
  /opt/vc/bin/raspistill -n -w 800 -h 600 -q 100 -sh 10 -awb fluorescent -p -f -o $savedir$filename.jpg

  ###########################################################################################

  sleep 10
done

echo "------------------------------"
 sleep 300
done
