#!/usr/bin/env bash

# Usage:
# ./alert.sh <name> <id>
# e.g. ./alert.sh BirdCam 1

runDir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

cd /var/lib/motioneye/$1
filepath=`find . -name  *.avi | xargs ls -t | head -1`
filesource="/movie/$2/download/$filepath"

cd ${runDir}
echo "Alert request for filesource : $filesource"
python motion_eye_alert/alert_handler.py ${filesource}
