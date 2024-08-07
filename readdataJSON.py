# import json


# #read file

# myjsonfile=open(r"C:\Users\ssheelav\Desktop\Test\Load\Demodata25.json")

# jsondata=myjsonfile.read()


# #parse

# obj=json.loads(jsondata)

# #print(str(obj['Robot_name']))
# print(obj)


import json
 
# Opening JSON file
#f = open('Demodata25.json')
 
# returns JSON object as
# a dictionary
#data = json.load(f)

import pandas as pd
payload = pd.read_json('Demodata25.json',lines=True)

print(payload)

#print(data['Robot_name'])
 
# # Iterating through the json
# # list
# for i in data['index']:
#     print(i)
 
# # Closing file
# f.close()
