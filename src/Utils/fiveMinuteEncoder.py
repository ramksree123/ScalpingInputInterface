
from json import JSONEncoder

class fiveMinuteEncoder(JSONEncoder):
  def default(self, o):
    return o.__dict__