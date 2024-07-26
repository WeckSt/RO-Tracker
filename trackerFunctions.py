import json
import os

def getJsonData(configpath):
    if os.path.isfile(configpath):
           with open(configpath) as rawJson:
                jsondata = json.load(rawJson)
                return jsondata
    else:
       return "error - no data found"

def getBossData(jsondata):
    for key, value in jsondata.items():
        if key == "bosses" :
            bossvalues = value
    return bossvalues

def writeInfo(eventObject,returnvalue):
    print(returnvalue)

test2 = getJsonData('./trackerConfig.json')

getBossData(test2)