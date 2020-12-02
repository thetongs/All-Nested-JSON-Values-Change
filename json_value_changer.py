## JSON changer
#
import json

# Open
with open("Data/Sample_Json.json", "r", encoding = 'utf-8' ) as file:
    data = json.load(file)

data1 = data

# Get through all key and values including nested blocks
def get_key(data1):
    for k, v in data1.items():
        if(isinstance(v, list)):
            dict1 = v[0]
            get_key(dict1)
        elif(isinstance(v, dict)):
            dict2 = v
            get_key(dict2)
        else:
            data1[k] = "no_values"

# call
get_key(data1)

# New file
o_file = open("New_sample.json", "w")
json.dump(data1, o_file, indent = 2)

# End