import json

# Open and load the JSON file
poketcg = open('./PokeTCG.json', encoding='utf8')
data = json.load(poketcg)
specificData = data["data"]

# Print the loaded data (optional)
#print the name of all fighting type pokemon
requested = "Fighting"
filteredResults = [d for d in specificData if requested in [d["types"]]]
if not filteredResults:
    print(f"I'm sorry, I couldn't find anything.")
else:
    for i in filteredResults:
        print(f"Name: {i['name']}")

#print all cards from the set "HeartGold & SoulSilver"
requested2 = "HeartGold & SoulSilver"
filteredResults2 = [d for d in specificData if requested2 in d["set"]["series"]]
if not filteredResults2:
    print(f"I'm sorry, I couldn't find anything.")
else:
    for i in filteredResults2:
        print(f"Name: {i['name']}")
#print all cards where the averageSellPrice is greater than 1.5
