import json
hu = json.load(open("hu.json", "r"))

file = open("test.pyhu", "r")
temp = file.read()

temp = temp.replace("kiiras", hu["kiiras"])

exec(temp)