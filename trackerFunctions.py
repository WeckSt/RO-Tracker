import json
import os

#import json file and return the data in readable format
def getJsonData(configpath):
    if os.path.isfile(configpath):
           with open(configpath) as rawJson:
                jsondata = json.load(rawJson)
                return jsondata
    else:
       return "error - no data found"

#get bossdata out of a json structure
def getBossData(jsondata):
    for key, value in jsondata.items():
        if key == "bosses" :
            bossvalues = value
    return bossvalues

def writeInfo(eventObject,returnvalue):
    print(returnvalue)