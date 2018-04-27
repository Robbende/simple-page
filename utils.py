import json

def getConfig():
    return json.loads(open('config.json').read())