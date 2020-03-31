import json

# use json to parse dict

def toolJSON():
    # cerate a dict 
    x =  '{ "name":"John", "age":30, "city":"New York"}'

    # parse x
    y = json.loads(x)

    print(y["age"])

# convert python to json and save it
def convertJSON():
    # a Python object (dict):
    x = {
    "name": "John",
    "age": 30,
    "city": "New York"
    }

    # convert into JSON:
    y = json.dumps(x)

    # the result is a JSON string:
    print(type(y)) 

    # save the json object to file
    file = open("list.json","w")
    file.write(y)

# In python, the json format is regarded as string object. 