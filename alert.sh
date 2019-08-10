#!/usr/bin/env bash

# Usage:
# ./alert.sh <id> <name>
# e.g. ./alert.sh 1 MotionCam

runDir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

cd ${runDir}
echo "Alert request for motion on camera $2 with the id $1"
sleep 2s
python motion_eye_alert/alert_handler.py $1 $2
