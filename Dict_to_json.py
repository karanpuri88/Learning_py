# Dictionary to Json

import json

Dict = {"cisco_sdwan" : "viptela" , "Cisco_dc" : "aci" , "cisco_access" : "dna", "cisco_iot" : "kinetics"}

# Print Dict way

print(Dict)

#print Json way, use indent other wise python will not provide indentation

print (json.dumps(Dict, indent = 4))


