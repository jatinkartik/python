myFirstDict = {"jatin":"A btech student","mani":"A Nickname","ayank":"A true friend","vishal":"still friend",
"linke":{"abir":"A senior student","kunal":"A mentor","student":"jatin,kunal,abir,ayank,vishal"}}
# print(myFirstDict.items())
print(myFirstDict.values())
print(myFirstDict.keys())
diction = {"CWH":"A CODE TEACHER"}
myFirstDict["linke"].update(diction)
# print(myFirstDict)
myFirstDict["linke"].update(diction)
myFirstDict.update({"jatin":"A CyberSec Enthusiast"})
print(myFirstDict.get("jatin"))
print(myFirstDict.get("linke").get("abir"))
myFirstDict.get("linke").update({"abir":"A senior student and mentor"})
myFirstDict.pop("mani")
print(myFirstDict.get("linke").get("abir"))
print(myFirstDict.items())