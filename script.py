## importing the necessary files

from ast import literal_eval
from credentials import APP_ID,APP_CODE
import herepy
import json
from read import point1,point2


## setting up credentials and calling the api's

routingApi = herepy.RoutingApi(APP_ID, APP_CODE)
geocoderapi = herepy.GeocoderApi(APP_ID,APP_CODE)

## taking input of the area we want to start our journey

response1 = geocoderapi.free_form('E-orbit cinema sai nagar amravati maharashtra')
response1.as_json_string()
f = open('result.json','w')
f.write(str(response1))
f.close()
a,b = point1()

## taking the input of the area we want to go

response2 = geocoderapi.free_form("Brijlal Biyani Science college Ravi nagar Amravati Maharashtra")
response2.as_json_string()
f = open('result2.json','w')
f.write(str(response2))
f.close()
c,d = point2()

## calculating the distance and cost
response = routingApi.car_route([a, b],
                                [c, d],
                                [herepy.RouteMode.car, herepy.RouteMode.fastest])

data=literal_eval(str(response))
data=literal_eval(str(data["response"].get("route")[0]))
data=literal_eval(str(data["leg"][0]))
distance=data["length"]/1000

## printing out the data
print("distance",distance,"km")
print("price cost is : ", distance* 25)