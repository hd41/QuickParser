import xml.etree.ElementTree as ET
import requests

def loadDoc():
    url = "http://www.quickfixengine.org/FIX42.xml"
    resp = requests.get(url)
    # print(resp.content)

tree = ET.parse('FIXCode.xml')
root = tree.getroot()  #fix

#root[0] -> header
#root[0]
def find_key_description(code):
    '''
        INPUT: code(character)
        OUTPUT: FIX description of that code

        This function takes in code and output the description of that code.
    '''

    for field in root[4]:        #root[4] -> fields
        if field.attrib['number'] == code:
            return (field.attrib['name'])

def find_val_description(key, code):
    '''
        INPUT: key and value
        OUTPUT: corresponding description of the vale

        This function take code of given message's value and provide the description of the same.
    '''
    for field in root[4]:
        point = field      #temporary give each field to temp variable point

        if (field.attrib['number'] == key):
            for val in point:
                if val.attrib['enum'] == code:
                    return val.attrib['description']
    return code

def find_key_code(key, val1):
    '''
        INPUT: parsed key and value pair
        OUTPUT: A string in which is joined by '='.

        This function takes the description as key value pair and give their respective exist if exist.
    '''

    new_key = ''
    new_val = val1
    for field in root[4]:
        point = field
        if(field.attrib['name']  == key):
            new_key = field.attrib['number']
            for val in point:
                if val.attrib['description'] == val1:
                    new_val = val.attrib['enum']

    return (new_key+"="+new_val)

# print(find_val_description("35","A"))
#
# print(find_key_code("EncryptMethod","NONE"))
#
# print(find_key_description("8"))
