from xml.dom import minidom

def minidom_module():
    # parse an xml file by name
    mydoc = minidom.parse('xmlfile.xml')

    items = mydoc.getElementsByTagName('item')

    # one specific item attribute
    print('Item #2 attibute:')
    print(items[1].attributes['name'].value)
    print(items[1].attributes['name'].value)
    
    # all item attributes
    print('\nAll attributes:')
    for elem in items:
        print(elem.attributes['name'].value)

    # one specific item's data
    print('\nItem #2 data:')
    print(items[1].firstChild.data)
    print(items[1].childNodes[0])
    print('\nAll item data:')
    for elem in items:
        print(elem.firstChild.data)
# we can load an opened file directly 
# datasource = open('items.xml')
# mydoc = parse(datasource)

# if the XML data was alreay loaded as a string
# than we could have used the parseString() instrad. 

# minidom_module()

def counting_elemens():
    # parse an xml file by name
    mydoc = minidom.parse('xmlfile.xml')
    items = mydoc.getElementsByTagName('item')
    # total amount of items
    print(len(items))
    # cause we can recollect all the tag which shatre
    # the same name by function : getElementsByTagName

counting_elemens()