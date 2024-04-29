import json, os

os.system("cls")

def swapdata(data):
    try:
        datad = json.load(data)
        keys = list(datad.keys())
        if len(keys) >= 2:
            keys[0], keys[1] = keys[1], keys[0]
            swapped_data = {key: datad[key] for key in keys}
            return json.dumps(swapped_data)
    except json.JSONDecodeError as error:
        raise error

locale = input("Locale: ")

dumpread = open(f"{os.getcwd()}/lang/{locale}.json", "r")
dumpwrite = open(f"{os.getcwd()}/lang/{locale}.json", "w")

processed = swapdata(dumpread)

dumpwrite.write(processed)
dumpwrite.close()

print(f"Process finished! Swapped locale: {locale}")