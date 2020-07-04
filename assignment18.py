'''

    Find a package in the Python standard library for dealing with JSON.
    Import the library module and inspect the attributes of the module. Use the
    help function to learn more about how to use the module. Serialize a
    dictionary mapping 'name' to your name and 'age' to your age, to a JSON
    string. Deserialize the JSON back into Python.

'''
import json
# print(help(json))
# print('-'*50)
dict1 = {'name': 'rajesh', 'age': 22}
jsonSeralize = json.dumps(dict1)
print(f'JsonSeralized => {jsonSeralize}')
print(type(jsonSeralize))
print('-'*50)
dictDeserialize = json.loads(jsonSeralize)
print(f'JsonDeseralized => { dictDeserialize }')
print(type(dictDeserialize))
