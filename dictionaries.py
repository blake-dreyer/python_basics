#Exploring basic ways to use Python Dictionaries

#Information about a person
def Personal():
    person_0 = {
        'name': 'Courtney',
        'age': 36,
        'occupation': 'Medical Science Liason',
        'Marital Status': 'Married'
    }
    for info in person_0:
        print(info.title()+': '+str(person_0[(info)]))