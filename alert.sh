#!/usr/bin/env bash

# Usage:
# ./alert.sh <name> <id>
# e.g. ./alert.sh BirdCam 1

runDir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

cd /var/lib/motioneye/$1
filepath=`find . -name  *.avi | xargs ls -t | head -1`
filesource="/movie/$2/download/$filepath"

cd ${runDir}
echo "Alert request for filesource : $filesource in 30 seconds time once we have enough footage"
sleep 30s
python motion_eye_alert/alert_handler.py ${filesource}
