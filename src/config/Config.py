import json
import os

def getServerConfig():
  print(os.getcwd())
  with open('../config/server.json', 'r') as server:
    jsonServerData = json.load(server)
    return jsonServerData

def getSystemConfig():
  with open('../config/system.json', 'r') as system:
    jsonSystemData = json.load(system)
    return jsonSystemData

