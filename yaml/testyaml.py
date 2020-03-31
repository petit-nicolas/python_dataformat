import yaml

def readYAML1():
    with open("fruits.yaml","r") as file:
        fruits_list = yaml.load(file, Loader=yaml.FullLoader)
        print(fruits_list)

def readYAML2():
    with open("categories.yaml","r") as file:
        documents = yaml.load(file, Loader=yaml.FullLoader)
        print(documents)
        print("--------------------")
        for item, doc in documents.items():
            print(item, ":", doc)

def writingYAML():
    dict_file = [{'sports' : ['soccer', 'football', 'basketball', 'cricket', 'hockey', 'table tennis']},
                {'countries' : ['Pakistan', 'USA', 'India', 'China', 'Germany', 'France', 'Spain']}]

    with open('writeYAML.yaml', 'w') as file:
        yaml.dump(dict_file, file)

# sort elements with the dump function
def dumpSortYAML():
    with open("fruits.yaml") as file:
        doc = yaml.load(file, Loader=yaml.FullLoader)

    sort_file = yaml.dump(doc, sort_keys=True)
    print(sort_file)

# we can take the dict's methods to modify the yaml object 
# in other words, (In python) yaml element = dict object


# Maybe consider using yaml.safe_load() 
# due to yaml.load() is insecure, 
# and executes python code in the yaml file.