person = {'name':'Nick','address':'cheonan','email':'lee@kopo.ac.kr'}
print(person)
print(person['name'])
print(person['email'])
print(person.items())
for key, value in person.items():
    print("\nkey \\ '" + key+ "'")
    print("value \\ '" + value+ "'")

person['name']='jay'
print(person)