#!/usr/bin/env bash

source /root/.profile

# Usage:
# ./alert.sh <id> <name>
# e.g. ./alert.sh 1 MotionCam

runDir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

cd ${runDir}
params=`env`
echo "Alert request for motion on camera $2 with the id $1"
echo "ENV= ${params}"

python motion_eye_alert/alert_handler.py $1 $2
