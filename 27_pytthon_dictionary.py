mydict = {}
mydict.update({"jatin":"A CyberSec Guy"})
print(mydict.get("jatin"))
mydict.update({"jatin":"A CyberSec Guy And Red Teamer"})
mydict.update({"Archi":"Secret Name of jatin"})
print(mydict.items())
print(mydict["Archi"])
print(mydict.get("Archi"))
print(mydict.get("jatin"))
mydict.update({"NextGoal":"OSCP NEXT YEAR"})
print(mydict.get("NextGoal"))