from flask.views import MethodView
from flask import render_template, request
from models.trendStatusFiveMinute import trendStatusFiveMinute
import json

class FetchTrendStatusAPI(MethodView):
  def get(self):
    if 'fetchTrendStatus' in request.args and request.args['fetchTrendStatus'] == 'true':
      print("Can Fetch Trend Status")
      print("hello World")
      trendStatusFromFile=trendStatusFiveMinute.loadFiveMinuteStatusFromFile()
      #print(trendStatusFromFile)
      return(trendStatusFromFile[0].__dict__)

    else:
      print("No status was found to fetch")
      return("No status was found to fetch")
  
  def fetchTrendStatus():
    with open('../config/system.json', 'r') as system:
      jsonSystemData = json.load(system)
      return jsonSystemData
      
    