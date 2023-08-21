"""
pokDB - World's most simple DB tool
"""
import json
import os

class db:
    """
    ### db class
    This class has write and get function.
    This class needs an unique dbcode.
    """
    def __init__(self, dbcode):
        if not os.path.isfile('./pokDBdb.jsonx'):
          with open('./pokDBdb.jsonx', 'w') as f:
           json.dump({'pokDB' : 'is a module'}, f, indent=4)
        
        self.dbcode = dbcode

    def write(self, key, value):
      """
      ### write function
      This function needs key and value.
      """
      try:
       with open('pokDBdb.jsonx', "r") as jf:
          data = json.load(jf)
      except:
       with open('./pokDBdb.jsonx', 'w') as f:
          json.dump({'pokDB' : 'is a module'}, f, indent=4)
      try:
        data[self.dbcode].append({
            key : value
        })
      except:
        data[self.dbcode] = []
        data[self.dbcode].append({
            key : value
        })
      with open('pokDBdb.jsonx', 'w') as f:
          json.dump(data, f, indent=4)

    def get(self, key):
      """
      ### get function
      This function needs key.
      This function returns a value.
      """
      with open('pokDBdb.jsonx', "r") as jf:
          data = json.load(jf)
      return data[self.dbcode][0].get(key)

    def rm(self, key):
      """
      ### rm function
      This function needs key.
      This function returns 'True'.
      """
      with open('pokDBdb.jsonx', "r") as jf:
          data = json.load(jf)

      del data[self.dbcode][0][key]
      data["1"] = [item for item in data["1"] if item]
      
      with open('pokDBdb.jsonx', 'w') as f:
          json.dump(data, f, indent=4)
        
      return True