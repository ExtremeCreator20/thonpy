import json, os

os.system("cls")

while True:
    locale = input("Locale: ")

    read = open(f"{os.getcwd()}/lang/{locale}.json", "r")
    
    original = json.loads(read.read())

    read.close()

    swap = {value: key for key, value in original.items()}

    write = open(f"{os.getcwd()}/lang/{locale}.json", "w")

    json.dump(swap, write)

    write.close()

    print(f"Process finished! Swapped locale: {locale}")