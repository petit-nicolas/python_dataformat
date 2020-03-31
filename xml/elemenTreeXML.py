import xml.etree.ElementTree as ET


def readXML():
    tree = ET.parse('xmlfile.xml')
    root = tree.getroot()

    # one specific item attribute
    print('Item #2 attribute:')
    print(root[0][1].attrib)
    print(root[0][1].attrib['name'])
    root[0][1].attrib['name'] = 'itemLabel'
    print(root[0][1].attrib)


    # all item attributes
    print('\nAll attributes:')
    for elem in root:
        for subelem in elem:
            print(subelem.attrib)

    # one specific item's data
    print('\nItem #2 data:')
    print(root[0][1].text)

    # all items data
    print('\nAll item data:')
    for elem in root:
        for subelem in elem:
            print(subelem.text)

def counting_elements():
    tree = ET.parse('xmlfile.xml')
    root = tree.getroot()

    # total amount of items
    print(len(root[0]))
    print(root[0][0])

def writeXML():

    # 1. create an element, which will act as our root element.
    # In our case, the tag for this elment is "data"
    # 2. Once we have our root element, we can create sub-element
    # by using the SubElement function
    # SubElement(parent, tag, attrib={}, **extra)
    # 3. we have another function : set() to set the valuse

    # create the file structure
    data = ET.Element('data')
    items = ET.SubElement(data,'items')
    item1 = ET.SubElement(items,'item')
    item2 = ET.SubElement(items,'item')
    item1.set('name','item1')
    item2.set('name','item2')
    item1.text = 'item1abc'
    item2.text = 'item2abc'

    # create a new XML file with the results
    mydata = ET.tostring(data)
    mydata = mydata.decode("utf-8")
    myfile = open("items2.xml", "w")
    # print(type(mydata))
    myfile.write(mydata)

def findingElements():
    tree = ET.parse('xmlfile.xml')
    root = tree.getroot()

    # find the first 'item' object
    for elem in root:
        print(elem.find('item').get('name'))

    # find all "item" objects and print their "name" attribute
    for elem in root:
        for subelem in elem.findall('item'):
        
            # if we don't need to know the name of the attribute(s), get the dict
            print(subelem.attrib)      
        
            # if we know the name of the attribute, access it directly
            print(subelem.get('name'))

def modifyingXML():
    tree = ET.parse('xmlfile.xml')
    root = tree.getroot()

    # changing a field text
    for elem in root.iter('item'):
        elem.text = 'new text'

    # modifying an attribute
    for elem in root.iter('item'):
        elem.set('name', 'newitem')

    # adding an attribute
    for elem in root.iter('item'):
        elem.set('name2', 'newitem2')

    tree.write('newitems.xml')

def ceratingSubEle():
    tree = ET.parse('xmlfile.xml')
    root = tree.getroot()

    # adding an element to the root node
    attrib = {}
    element = root.makeelement('seconditems', attrib)
    root.append(element)

    # adding an element to the seconditem node
    attrib = {'name2': 'secondname2'}
    subelement = root[0][1].makeelement('seconditem', attrib)
    ET.SubElement(root[1], 'seconditem', attrib)
    root[1][0].text = 'seconditemabc'

    # create a new XML file with the new element
    tree.write('newitems2.xml')

def tryxml():
    tree = ET.parse('xmlfile.xml')
    root = tree.getroot()

    seconditems = ET.SubElement(root, 'seconditems')
    seconditem1 = ET.SubElement(seconditems, 'item')
    seconditem2 = ET.SubElement(seconditems, 'item')
    seconditem1.set('name', 'seconditem1')
    seconditem2.set('name', 'seconditem2')
    seconditem1.text = 'seconditemabc1'
    seconditem2.text = 'seconditemabc2'

    mydata = ET.tostring(root)
    mydata = mydata.decode('utf-8')
    myfile = open("xmlfile001.xml","w")
    myfile.write(mydata)


def deletingXML():
    tree = ET.parse('xmlfile.xml')
    root = tree.getroot()

    # removing an attribute
    root[0][0].attrib.pop('name', None)

    # create a new XML file with the results
    tree.write('newitems3.xml')

    root = tree.getroot()
    # removing one sub-element
    root[0].remove(root[0][0])

    # create a new XML file with the results
    tree.write('newitems4.xml')

    root = tree.getroot()
    # removing all sub-elements of an element
    root[0].clear()

    # create a new XML file with the results
    tree.write('newitems5.xml')