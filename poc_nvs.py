import boto3
import json
import requests
import urllib3

# from botocore.vendored import requests
def lambda_handler(event, context):

    # # TODO implement
    # url='https://portal.cognizant-1facility.com/energy-management/energy/system'
    # response=requests.get(url)
    # print(response.text)
    
    a='https://dashboard.smart-impulse.com/api/2.0/power/85965a2e-c437-4549-884f-8fb826fdc615/aHawNkQgA6zUzScCcx3KxyOlB6pA2Vwx'
    b='https://dashboard.smart-impulse.com/api/2.0/energy/85965a2e-c437-4549-884f-8fb826fdc615/aHawNkQgA6zUzScCcx3KxyOlB6pA2Vwx'
    c='https://dashboard.smart-impulse.com/api/2.0/energy/day/85965a2e-c437-4549-884f-8fb826fdc615/aHawNkQgA6zUzScCcx3KxyOlB6pA2Vwx'
    d='https://dashboard.smart-impulse.com/api/2.0/power/load/85965a2e-c437-4549-884f-8fb826fdc615/aHawNkQgA6zUzScCcx3KxyOlB6pA2Vwx'
    e='https://dashboard.smart-impulse.com/api/2.0/energy/load/85965a2e-c437-4549-884f-8fb826fdc615/aHawNkQgA6zUzScCcx3KxyOlB6pA2Vwx'
    
    # f='https://portal.cognizant-1facility.com/energy-management/energy/system'
    
    ar=requests.get(a)
    br=requests.get(b)
    cr=requests.get(c)
    dr=requests.get(d)
    er=requests.get(e)
    # fr=requests.get(f)
    print(ar.text)
    print(br.text)
    print(cr.text)
    print(dr.text)
    print(er.text)
    # print(fr.text)
    
    smartimpulse = []
    smartimpulse.append(ar)
    print (smartimpulse)
    
    return 'success'
    

# lambda_handler (1,2)
urllib3.disable_warnings()