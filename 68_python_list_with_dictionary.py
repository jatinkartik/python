persons = [{"name":"jatin","occupation":"student","class":"CSE21a","addr":"bijnor"},{"name":"sahil","occupation":"student_comedian","class":"CSE21a","addr":"firozpur"}]
for person in persons:
    for value in person:
        print(value,end="        ")
        print(person[value])
    print()
    print()