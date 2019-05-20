import json

def point1():
    with open('result.json') as json_file:
        data = json.load(json_file)
        a = (data["Response"]["View"][0]["Result"][0]["Location"]["DisplayPosition"]["Latitude"])
        b = (data["Response"]["View"][0]["Result"][0]["Location"]["DisplayPosition"]["Longitude"])
        return a,b

def point2():
    with open('result2.json') as json_file:
        data = json.load(json_file)
        c =(data["Response"]["View"][0]["Result"][0]["Location"]["DisplayPosition"]["Latitude"])
        d =(data["Response"]["View"][0]["Result"][0]["Location"]["DisplayPosition"]["Longitude"])
        return c,d

