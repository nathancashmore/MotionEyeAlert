# MotionEyeAlert
Scripts to provide notifications when MotionEye spots activity.
Integration uses:

* __Slack__ - For delivering the notifications.

# Installation

* Install MotionEye on your Raspberry Pi (https://github.com/ccrisan/motioneye/wiki/Installation)
* Clone this project into the home directory on the Pi
* Add the required 3rd party modules to the python installation (See External Dependencies section below) 
* Add the following command on the MotionEye in 
_Preferences > Motion Notifications > Command_
``/root/MotionEyeAlert/alert.sh 1 MyCamera``

Where:

``MyCamera`` - is the Camera Name and 
``1`` - is the Camera ID

# Configuration

Environment variables must be set for the application to run:

```
export MOTION_EYE_SERVER_URL=http://motioncam.somewhere.com
export MOTION_EYE_USER=admin
export MOTION_EYE_SIGNATURE=xxxxxxxxxxxxxxxxxx
export SLACK_WEBHOOK_URL=https://hooks.slack.com/services/XXXXXXX/XXXXXX/XXXXXXXXXX
export SLACK_CHANNEL=alert
```

These should be located in your ```.profile``` on the Pi itself.  
If they are specified for the default admin user they should be located in a
profile file you should create called ```/admin/.profile```.  These will then be 
automatically set when the ```alert.sh``` script runs.

MOTION_EYE_SIGNATURE can be obtained by looking at the ```Video Streaming > Snapshot URL``` 

##Slack
* Register on Slack on the [Create a New Team page](https://slack.com/create#email)
* Add a new webhook and channel you would like to use for notifications on the [Incoming-Webhook setup page](https://my.slack.com/services/new/incoming-webhook/)
* Put the Webhook URL and channel name in the config file.

##External Dependencies
Communication with Slack is carried out using the ```requests``` module.  Because the default MotionEye image does not contain
much in the way of utilities this can just be lifted from a local install and copied into the default python install directory on the pi.  This is obviously not the best method but 
is more convenient than installing MotionEye on top of a default Pi image.

```
scp -r /Library/Python/2.7/site-packages/requests admin@xx.xx.xx.xx:/usr/lib/python2.7/requests
```

# Testing
Run the tests using
```nosetests```
