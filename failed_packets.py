from hashlib import sha256
import hmac
import base64
import requests
import time
import datetime
import json

def unixtime(days=0, hours=0, minutes=0):

    now_time = datetime.datetime.now()  
    # days=None, seconds=None, microseconds=None, milliseconds=None, minutes=None, hours=None, weeks=None
    jisuantime = now_time + datetime.timedelta(days=days, hours=hours, minutes=minutes)
    
    tss1 = jisuantime.strftime('%Y-%m-%d %H:%M:%S')
    
    timeArray = time.strptime(tss1, "%Y-%m-%d %H:%M:%S")
   
    timeStamp = int(time.mktime(timeArray))
    return timeStamp  # 1381419600

def get_sign(data, key):
    key = key.encode('utf-8')
    message = data.encode('utf-8')
    sign = base64.b64encode(hmac.new(key, message, digestmod=sha256).digest())
    sign = str(sign, 'utf-8')
    return sign

class OpenApiDemo(object):
    def __init__(self):
        self.base_url = "https://apis.iobscan.io"
        self.api_key = "[insert API key]" # contact the Iris team for an API key and secret
        self.api_secret = "[insert API secret]"

    def ibc_failure(self):
        path = "/ibc/transfers/statistics/cosmoshub/failure?[insert start_date and end_date]"
        signing_string = f"X-Timestamp: {unixtime()}\nURI: {path}\nBody: "
        signature = get_sign(signing_string, self.api_secret)
        headers = {"X-Api-Key": self.api_key,
                   "X-Timestamp": str(unixtime()),
                   "X-Signature": signature}
        r = requests.get(self.base_url + path, headers=headers)
        cgtresult = r.json()
        print(json.dumps(cgtresult, indent=4))
        return cgtresult
    
        
if __name__ == '__main__':
    a = OpenApiDemo()
    a.ibc_failure()