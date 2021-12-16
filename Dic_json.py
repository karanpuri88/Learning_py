# To convert Dictionary to Json

import json

dict123 = {"cisco" : "sdwan" , "juniper" : "contrail" , "velo_Cloud" : "sdwan1"}

# You have to dump the dictionary in json as string otherwise u will get error as TypeError: the JSON object must be str, bytes or bytearray, not dict

json_coversion = json.dumps(dict123, indent=4)

print(json_coversion) # <<  this output type is string 

#output = json.loads(json_coversion)

#print (output)