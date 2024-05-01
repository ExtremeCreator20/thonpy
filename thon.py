import json, sys, os

fpath = sys.argv[1]

lfs = f"{os.getcwd()}/lang/"

langfs = {"engb":"en-GB.json","huhu":"hu-HU.json"}

engb = json.load(open(lfs + langfs["engb"], "r"))
huhu = json.load(open(lfs + langfs["huhu"], "r"))

file = open(fpath, "r")
temp = file.read()

lang = f"{fpath}".split(".")[-2]

langrps = lfs+langfs[lang]

for i in range(len(langrps)):
    temp = temp.replace(i, huhu[i])

exec(temp)