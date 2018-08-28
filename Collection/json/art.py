import json

with open("minart.json") as artfile:
    art = json.load(artfile)
    print(art["description"])