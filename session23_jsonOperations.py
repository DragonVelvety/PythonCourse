# json objects dict {"key":"value"}
# numbers 1,10.55 int float
# array [10,"string"] list
#					  tuple

import json
handle = open("sample.json","r")	
content = handle.read()
handle.close()

# print(content)

d = json.loads(content)
#print(d["glossary"]["title"])

d["glossary"]["title"] = 33
# print(d["glossary"]["GlossDiv"]["title"])
d["glossary"]["GlossDiv"]["title"] = ("S","My S")
# print(d)

j = json.dumps(d, indent=4,sort_keys=True)
# print(j)
handle = open("json_output.json", "w")
handle.write(j)
handle.close()