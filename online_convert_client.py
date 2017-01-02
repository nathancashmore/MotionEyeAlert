# Python 2.7.10
# online_convert_client.py

import json
import time

import requests

import config
from custom_exceptions import TooManyRequests

CONVERT_API_KEY = config.CONVERT_API_KEY
CONVERT_API_URL = "https://api2.online-convert.com/jobs"


class OnlineConvertClient(object):
    AUTH_HEADER = {"x-oc-api-key": CONVERT_API_KEY}

    # --------------------------------------------------------------------------#

    def convertFile(self, input_file):
        job_id = self.getJobId(input_file)

        file_url = self.getConvertedFileUrl(job_id)

        print(
            "OnlineConvertClient :\nInput file: {0} \nJob id: {1} \nOutput file: {2}".format(input_file, job_id,
                                                                                             file_url))
        return file_url

    # --------------------------------------------------------------------------#

    @staticmethod
    def postFileForConversion(file_source):
        """Makes a REST service call to online-convert with file source and returns response"""

        payload = {
            "input": [{
                "type": "remote",
                "source": file_source
            }],
            "conversion": [{
                "target": "mp4"
            }]
        }

        return requests.post(CONVERT_API_URL, headers=OnlineConvertClient.AUTH_HEADER, json=payload)

    # --------------------------------------------------------------------------#

    @staticmethod
    def getJobStatus(job_id):
        """Returns the job status for a given job id"""
        return requests.get(CONVERT_API_URL + "/" + job_id, headers=OnlineConvertClient.AUTH_HEADER)

    # --------------------------------------------------------------------------#

    @staticmethod
    def getJobId(file_source):
        """Post the AVI file which needs to be converted to an MP4"""
        convert_response = OnlineConvertClient.postFileForConversion(file_source)

        if convert_response.ok:
            return json.loads(convert_response.content).get("id")
        else:
            return convert_response.raise_for_status()

    # --------------------------------------------------------------------------#

    @staticmethod
    def getConvertedFileUrl(job_id):
        """Keep requesting the status of the job until its complete then return the response"""
        job_status = "working"
        request_count = 0
        status_response = ""

        while (job_status != "completed") & (request_count < 5):
            status_response = OnlineConvertClient.getJobStatus(job_id)

            if status_response.ok:
                job_status = json.loads(status_response.content).get("status").get("code")
            else:
                return status_response.raise_for_status()

            time.sleep(1)
            request_count += 1

        if request_count == 5:
            raise TooManyRequests("No successful response from third party API after multiple attempts")

        return json.loads(status_response.content).get("output")[0].get("uri")

        # --------------------------------------------------------------------------#
