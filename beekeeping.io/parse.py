"""
This script is built upon Dave Strickler's API for Beekeeping.io research api
The documentation:https://documenter.getpostman.com/view/514163/RWEduLSZ
It will be used to mashup UBL data & Beekpeeing.io data
Modified by Stephanie M. Davis - github.com/stephaniemdavis

url = "https://api.beekeeping.io/api_v2/research/postal_codes/" # api URL

"""
import requests,json,pprint # import required libraries


url = "https://api.beekeeping.io/api_v2/research/postal_codes/" # api URL
# Open the beekeeping.io api key text file
api-key = open(_api_beekeeping-io.txt)
headers = {'license_key': api-key} # api parameters

response = requests.get(url,headers) # query api, create object
print(response) # verify successful GET request

response.json = json.loads(response.text) # deserialize json object
print(response.json.keys()) # generate dict key list

#pprint.pprint(response.json['payload']) # pretty printing payload object
print('The length of the payload dictionary is %d items.' % len(response.json['payload']))

# NEXT - Parse all the Masssachusetts records
