#!/usr/bin/env bash

# Usage:
# ./alert.sh <name> <id>
# e.g. ./alert.sh BirdCam 1

cd /var/lib/motioneye/$1
filepath=`find . -name  *.avi | xargs ls -t | head -1`
filesource="/movie/$2/download/$filepath"

echo "Alert for filesource : $filesource"
#python -m motion_eye_alert/alert_handler.py $filesource
