import os
import json

from models.trendStatus import trendStatus
from models.trendDirection import trendDirection
from models.statusOfInputInterface import statusOfInputInterface
from Utils.Utils import Utils
from Utils.fiveMinuteEncoder import fiveMinuteEncoder

from config.Config import getServerConfig, getSystemConfig

class trendStatusFiveMinute:
  def __init__(self, tradingSymbol):
    self.tradingSymbol = tradingSymbol
    self.trendStatus = trendStatus.NO_STATUS
    self.trendDirection = trendDirection.NO_DIRECTION
    self.lastStatusReceivedFromUser=None
    self.lastDirectionReceivedFromUser=None
    self.timeLastReadByUser = 0
    self.timeLastReadByUserInStringFormat = None
    self.timeLastReadBySystem = 0
    self.timeLastReadBySystemInStringFormat = None
    self.timeLastInputWasReceivedFromUser = 0
    self.timeLastInputWasReceivedFromUserInStringFormat = None
    self.statusOfInputInterface = statusOfInputInterface.STOPPED
  
  @staticmethod
  def createFiveMinuteStatus(trendStatusReceived):
    trendStatusReceivedFromUser=trendStatusFiveMinute("NSE:NIFTYBANK-INDEX")
    trendStatusList=[]
    trendStatusReceivedFromUser.timeLastInputWasReceivedFromUser=Utils.getEpoch()
    trendStatusReceivedFromUser.timeLastInputWasReceivedFromUserInStringFormat=Utils.convertEpochToDateTimeString(Utils.getEpoch())
    trendStatusReceivedFromUser.statusOfInputInterface=statusOfInputInterface.WAITING_FOR_USER_INPUT
    if trendStatusReceived=='1':
      trendStatusReceivedFromUser.trendStatus=trendStatus.TRENDING
      trendStatusReceivedFromUser.trendDirection=trendDirection.UP
    elif trendStatusReceived=='2':
      trendStatusReceivedFromUser.trendStatus=trendStatus.TRENDING
      trendStatusReceivedFromUser.trendDirection=trendDirection.DOWN
    elif trendStatusReceived=='3':
      trendStatusReceivedFromUser.trendStatus=trendStatus.RANGING
      trendStatusReceivedFromUser.trendDirection=trendDirection.NO_DIRECTION
    elif trendStatusReceived=='4':
      trendStatusReceivedFromUser.trendStatus=trendStatus.NO_STATUS
      trendStatusReceivedFromUser.trendDirection=trendDirection.NO_DIRECTION
      trendStatusReceivedFromUser.statusOfInputInterface=statusOfInputInterface.STOPPED

    
    trendStatusList.append(trendStatusReceivedFromUser)
    
    return trendStatusList
  
  @staticmethod
  def saveFiveMinuteStatusToFile(trendStatusReceivedFromUser):
    serverConfig = getServerConfig()
    tradesDir = os.path.join(serverConfig['deployDir'], 'fiveMinuteStatus')
    fiveMinuteStatusFilePath = os.path.join(tradesDir, 'fiveMinuteStatus.json')
    print(fiveMinuteStatusFilePath)
    with open(fiveMinuteStatusFilePath, 'w') as tFile:
      json.dump(trendStatusReceivedFromUser, tFile, indent=2, cls=fiveMinuteEncoder)
  
  @staticmethod
  def loadFiveMinuteStatusFromFile():
    serverConfig = getServerConfig()
    print("Loading Five Minute Status From File")
    tradesDir = os.path.join(serverConfig['deployDir'], 'fiveMinuteStatus')
    fiveMinuteStatusFilePath = os.path.join(tradesDir, 'fiveMinuteStatus.json')
    
    trendStatusList = []
    tFile = open(fiveMinuteStatusFilePath, 'r')
    trendStatusFile = json.loads(tFile.read())
    for tr in trendStatusFile:
      
      trendStatusFromFile = trendStatusFiveMinute.convertJSONToFiveMinuteStatus(tr)
      trendStatusList.append(trendStatusFromFile)
    
    print(trendStatusList)
    for tr in trendStatusList:
      print(tr.__dict__)
    return trendStatusList
  

  @staticmethod
  @staticmethod
  def convertJSONToFiveMinuteStatus(jsonData):
    fiveMinuteStatusObject = trendStatusFiveMinute(jsonData['tradingSymbol'])
    
    fiveMinuteStatusObject.trendStatus = jsonData['trendStatus']
    fiveMinuteStatusObject.trendDirection = jsonData['trendDirection']
    fiveMinuteStatusObject.lastStatusReceivedFromUser=jsonData['lastStatusReceivedFromUser']
    fiveMinuteStatusObject.lastDirectionReceivedFromUser=jsonData['lastDirectionReceivedFromUser']
    fiveMinuteStatusObject.timeLastReadByUser = jsonData['timeLastReadByUser']
    fiveMinuteStatusObject.timeLastReadByUserInStringFormat = jsonData['timeLastReadByUserInStringFormat']
    fiveMinuteStatusObject.timeLastReadBySystem = jsonData['timeLastReadBySystem']
    fiveMinuteStatusObject.timeLastReadBySystemInStringFormat = jsonData['timeLastReadBySystemInStringFormat']
    fiveMinuteStatusObject.timeLastInputWasReceivedFromUser = jsonData['timeLastInputWasReceivedFromUser']
    fiveMinuteStatusObject.timeLastInputWasReceivedFromUserInStringFormat = jsonData['timeLastInputWasReceivedFromUserInStringFormat']
    fiveMinuteStatusObject.statusOfInputInterface = jsonData['statusOfInputInterface']

    return fiveMinuteStatusObject

      
      
    
    