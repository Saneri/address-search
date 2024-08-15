# converts municipalities.txt (copied from DVV file directly into txt) to json

import json

with open('municipalities.txt', 'r') as f:
    data = f.read()

lines = data.split("\n")
data_list = []
for line in lines:
    # Skip empty lines
    if not line.strip():
        continue

    name, code = line.rsplit("\t", 1)
    data_list.append({code.strip(): name.strip()})

with open("municipalities.json", "w") as f:
    json.dump(data_list, f)