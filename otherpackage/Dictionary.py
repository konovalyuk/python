myDictionary = {"BK": 5, "Maksym": 3}
print(myDictionary)
print(myDictionary["BK"])
myDictionary["Maksym"] = 7
print(myDictionary)
xx = "BQ"
myDictionary[xx] = "1"
print(myDictionary)
del myDictionary["BQ"]
print(myDictionary)

myDictionary = {"BK": 5.5, 3.5: "Three point five", 5: "-", 5.5: 7}
print(myDictionary["BK"])
