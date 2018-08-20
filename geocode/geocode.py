'''
Stephanie M. Davis - 6-28-2018
s.davis@bestbees.com
steffie.davis@gmail.com

Python script geocodes Buzz data and
adds latitude,longitude coordinates to it.
h/t: http://geopy.readthedocs.io/en/stable/#indices-and-search

https://sunnykrgupta.github.io/a-practical-guide-to-geopy.html
'''
# import necessary packages
import os
import csv
import json
import geopy

# open & read the api key for use in geopy
fopen = open('_api-google.txt','r')
apikey = fopen.read()

# import Google geocoder module
from geopy.geocoders import GoogleV3
#geolocator = GoogleV3(apikey)

# create a Google geolocator object
location = geolocator.geocode('10 Downing Street, UK',language='en')

print(location.address)
