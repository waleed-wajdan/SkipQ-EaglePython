import urllib3
import datetime
from cloudwatch_putData import AWSCloudWatch
import constants as constants

def lambda_handler(event, context):
    values = dict()
    """CloudWatch Object"""
    cloudwatch_object = AWSCloudWatch()

    """Executing functions to fetch website active status and latency"""
    # availability = [-1,-1,-1,-1]
    # latency = [-1,-1,-1,-1]
    # availability[0] = getAvail(constants.url[0])
    # latency[0] = getLatency(constants.url[0])
    # values.update({'availability_url1':availability[0], 'latency_url1':latency[0]})
    # availability[1] = getAvail(constants.url[1])
    # latency[1] = getLatency(constants.url[1])
    # values.update({'availability_url2':availability[1], 'latency_url2':latency[1]})
    # availability[2] = getAvail(constants.url[2])
    # latency[2] = getLatency(constants.url[2])
    # values.update({'availability_url3':availability[2], 'latency_url3':latency[2]})
    # availability[3] = getAvail(constants.url[3])
    # latency[3] = getLatency(constants.url[3])
    # values.update({'availability_url4':availability[3], 'latency_url4':latency[3]})
    
    for i in range(4):
        availability = getAvail(constants.url[i])
        latency = getLatency(constants.url[i])
        values.update({'availability_of_'+constants.url[i]:availability,'latency_of_'+constants.url[i]:latency})
        # values.update({f"{constants.url[i]}":f"Availablity = {availability}  ||  Latency = {latency}"})
        # values.update({"Availability":availability,"Latency":latency})
        dimensions = [{'Name': 'URL', 'Value': constants.url[i]}]
        cloudwatch_object.cloudwatch_metric_data(constants.namespace, constants.AvailabilityMetric, dimensions, availability)
        cloudwatch_object.cloudwatch_metric_data(constants.namespace, constants.LatencyMetric, dimensions, latency)
    
    # dimensions = [{'Name': 'URL1', 'Value': constants.url[0]},
    #               {'Name': 'URL2', 'Value': constants.url[1]},
    #               {'Name': 'URL3', 'Value': constants.url[2]},
    #               {'Name': 'URL4', 'Value': constants.url[3]}]

    # for i in range(4):
    #         dimensions.append(
    #              {'Name': 'Url', 'Value': constants.url[i]}
    #         )

    
    # cloudwatch_object.cloudwatch_metric_data(constants.namespace, constants.AvailabilityMetric, dimensions,availability)
    # cloudwatch_object.cloudwatch_metric_data(constants.namespace, constants.LatencyMetric, dimensions,latency)


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