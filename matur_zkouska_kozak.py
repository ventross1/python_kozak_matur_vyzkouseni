import json

class cards:
    def __init__(self, name, colour, symbol):
        self.name = name
        self.colour = colour
        self.symbol = symbol
    
    def __str__(self):
        return f"name of the card is {self.name}, colour of the card is {self.colour} and symbol is {self.symbol}"

f = open("matur_zkouska_kozak.json")
data = json.load(f)
c = []
for i in data["cards"]:
    p = cards(i["name"], i["colour"], i["symbol"])
    c.append(p)

for b in range(len(c)):
    print(c[b])