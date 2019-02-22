import csv
import requests
from requests.auth import HTTPBasicAuth
import logging
import nose
import json
global input
global nr
import helpers.api_assertions


def api_methods_all(input):
    nr = len(input)
    print(nr)
    for i in range(nr):

        if input[i]['method'] == 'post':
            ''' create API using post '''
            r = requests.post(input[i]['url'] + input[i]['resources'], data=input[i]['payload'])
            print (r.status_code)
            helpers.api_assertions.assert_status_code(None, r.status_code)            
#             print (r.status_code)
#             body = json.dumps(r.json(),indent=4)
#             print("body is : ", body)
#             print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
#             header = r.headers
#             print("header is : ", header)
#             get_instance_id(r)
                  

        if input[i]['method'] == 'get':
            ''' get all instances '''
            r = requests.get(input[i]['url'] ,data=input[i]['payload'])
            print (r.status_code)
            helpers.api_assertions.assert_status_code(None, r.status_code)

        if input[i]['method'] == 'put':
               ''' update newly created API instance  '''
               r = requests.put(input[i]['url'] + input[i]['resources'], data=input[i]['payload'])
               print (r.status_code)
               helpers.api_assertions.assert_status_code(None, r.status_code) 

        if input[i]['method'] == 'delete':
          ''' delete newly created API instance  '''
          r = requests.delete(input[i]['url'] + input[i]['resources'])
          print (r.status_code)
          helpers.api_assertions.assert_status_code(None, r.status_code)
