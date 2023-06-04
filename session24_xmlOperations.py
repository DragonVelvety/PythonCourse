import xmltodict

handle = open("sampleInput.xml","r")

content = handle.read()
# print(content)

d = xmltodict.parse(content)
print(d["catalog"]["book"])
d["catalog"]["book"] = 4
# print(d)

x = xmltodict.unparse(d)
print(x)