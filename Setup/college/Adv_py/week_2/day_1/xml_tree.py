import json 

def read_json(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

def write_json(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

filename = 'data.json'
data = {"name": "John", "age": 30, "city": "New York"}

write_json(filename, data)
read_data = read_json(filename)
print(read_data)
