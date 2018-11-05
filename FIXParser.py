import sys
from XMLParser import find_key_description, find_val_description, find_key_code

def parser(fixMsg):

    '''
        INPUT: FIX message in a string format.
        OUTPUT: Dictionary of FIX message.

        This function will parse the input FIX message and generate those messages in a dictionary format.
    '''

    dict = {}

    fixComp = fixMsg.split('|')
    for k in fixComp[:-1]:
        k = k.strip()
        tmp = k.split('=')
        key = find_key_description(tmp[0].strip())
        val = find_val_description(tmp[0].strip(),tmp[1].strip())
        dict[key] = val

    return dict

def process(msg):
    '''
        INPUT: msg(dictionary format)
        OUTPUT: process another dictionary format response

        This takes dictionary of message, process it to apply process of pricing.
    '''

    pass

def sendMessage(processedMsg):
    '''
        INPUT: processed message(dictionary format)
        OUTPUT: FIX message that is readable to SONATA.

        This function takes dictionary as a message and covert that dictionary to FIX Message.
    '''

    lis = []

    for k in processedMsg:
        key,val = k, processedMsg[k]
        lis.append(find_key_code(key,val))

    return '|'.join(lis)+'|'

def main():
    '''
        As of now a static fixMessage is tested.
        Driver function.
    '''

    fixMsg = '8=FIX.4.1|9=61|35=A|49=INVMGR|56=BRK|34=1|52=20000426-12:05:06|98=0|108=30|10=157|'
    fixMsg1 = '8=FIX.4.1|9=154|35=6|49=BRKR|56=INVMGR|34=239|52=19980604-08:00:36|23=115687|28=N|55=PIRI.MI|54=1|27=300000|44=5950.000000|25=H|10=168|'
    print("Request: ",fixMsg1)
    print("After Parsing: ", parser(fixMsg1) )
    print("Response: ", sendMessage(parser(fixMsg1)))


main()
