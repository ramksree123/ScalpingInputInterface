from flask.views import MethodView
from flask import render_template, request
from models.trendStatusFiveMinute import trendStatusFiveMinute
import json
from Utils.Utils import Utils
from datetime import datetime

class FetchTrendStatusAPI(MethodView):
  def get(self):
    if 'fetchTrendStatus' in request.args and request.args['fetchTrendStatus'] == 'true':
      print("Can Fetch Trend Status")
      print("hello World")
      trendStatusFromFile=trendStatusFiveMinute.loadFiveMinuteStatusFromFile()
      trendStatusFromFileNew=trendStatusFromFile[0]
      
      trendStatusFromFileNew.systemTimeWhenStatusWasFetched=Utils.getEpoch()
      trendStatusFromFileNew.systemTimeWhenStatusWasFetchedInStringFormat=Utils.convertEpochToDateTimeString(Utils.getEpoch())
      
      return(trendStatusFromFileNew.__dict__)

    else:
      print("No status was found to fetch")
      return("No status was found to fetch")
  
  def fetchTrendStatus():
    with open('../config/system.json', 'r') as system:
      jsonSystemData = json.load(system)
      return jsonSystemData
    
  def fetchTrendStatusAloneFromFile():
    trendStatusFromFile=trendStatusFiveMinute.loadFiveMinuteStatusFromFile()
    trendStatusFromFileNew=trendStatusFromFile[0]
    #The above object contains the object
    print(trendStatusFromFileNew.__dict__)
    return trendStatusFromFileNew

      
    