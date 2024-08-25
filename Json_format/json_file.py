import json

person = {
    "name": "Paul",
    "age": 23,
    "friends": ["Sophie", "Jane", "Thierry"]
}

json_person = json.dumps(person) # Serialize
person = json.loads(json_person) # Deserialize

print(f"JSON: {json_person}")
print(f"JSON: {person}")

