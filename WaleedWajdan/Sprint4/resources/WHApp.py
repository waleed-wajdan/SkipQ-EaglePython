import urllib3
import datetime
from resources.cloudwatch_putData import AWSCloudWatch
import resources.constants as constants

def lambda_handler(event, context):
    values = dict()
    """CloudWatch Object"""
    cloudwatch_object = AWSCloudWatch()

    """Executing functions to fetch website active status and latency"""
    
    for i in range(4):
        availability = getAvail(constants.url[i])
        latency = getLatency(constants.url[i])
        values.update({'availability_of_'+constants.url[i]:availability,'latency_of_'+constants.url[i]:latency})
        dimensions = [{'Name': 'URL', 'Value': constants.url[i]}]
        cloudwatch_object.cloudwatch_metric_data(constants.namespace, constants.AvailabilityMetric, dimensions, availability)
        cloudwatch_object.cloudwatch_metric_data(constants.namespace, constants.LatencyMetric, dimensions, latency)
    
    return values

def getLatency(myurl):
    http = urllib3.PoolManager()
    start = datetime.datetime.now()
    response = http.request("GET", myurl)
    end = datetime.datetime.now()
    delta = end - start
    latencySec = round(delta.microseconds * 0.000001,6)
    return latencySec

def getAvail(myurl):
    http = urllib3.PoolManager()
    response = http.request("GET",myurl)
    if response.status == 200:
        return 1.0
    else:
        return 0.0