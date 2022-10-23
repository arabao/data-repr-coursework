import json

data = {
    "employees": [
        {
            "firstName": "John",
            "lastName": "Doe",
            "address": "13 Main Street, Carrigaline, Co.Cork",
            "age": 41
        },
        {
            "firstName": "Anna",
            "lastName": "Smith",
            "address": "52 The walk, Foxtrot, Co.Meath",
            "age": 22
        },
        {
            "firstName": "Peter",
            "lastName": "Jones",
            "address": "1 Riverview, Athy, Co.Kildare",
            "age": 61
        },
        {
            "firstName": "Joe",
            "lastName": "Bloggs",
            "address": "The Square, Oldbawn, Co.Dublin",
            "age": 52
        },
        {
            "firstName": "Mary",
            "lastName": "Fox",
            "address": "The avenue, longMile, Co.Meath",
            "age": 37
        }
    ]   
}
#print(data)

file = open("dr2.4-json.json", 'w')
json.dump(data,file, indent=4)
jsonString = json.dumps(data)
print(jsonString)