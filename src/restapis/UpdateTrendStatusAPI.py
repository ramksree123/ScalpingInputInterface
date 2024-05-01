from flask.views import MethodView
from flask import render_template, request

from models.trendStatusFiveMinute import trendStatusFiveMinute

class UpdateTrendStatusAPI(MethodView):
  def get(self):
    if 'updateTrendStatus' in request.args and request.args['updateTrendStatus'] == 'true':
      trendStatusReceived=request.args['trendStatus']
      trendStatusReceivedFromUser=trendStatusFiveMinute.createFiveMinuteStatus(trendStatusReceived)
      trendStatusFiveMinute.saveFiveMinuteStatusToFile(trendStatusReceivedFromUser)


    
      print("Can update Trend Status",trendStatusReceived)
      return(trendStatusReceivedFromUser[0].__dict__)

    else:
      print("No status was found")
      return("No status was found")
      
    