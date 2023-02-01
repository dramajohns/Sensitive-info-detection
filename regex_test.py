# -*- coding: utf-8 -*-
def regex_test(text):
    import re
    PHONE_NUMBER_pattern = re.compile(r'(\+*216|0)([ \-_/]*)(\d[ \-_/]*){8}') # tunisian phone number regex
    ID_NUMBER_pattern = re.compile(r'\d{8}')# tunisian ID CARD regex
    CREDIT_card = re.compile(r'\b\d{13,16}\b|\b(?:\d[ -]*?){13,16}\b')
    EMAIL = re.compile(r'[-\w\.]+@([\w-]+\.)+[\w-]{2,4}')
    SENSITIVE_Words_pattern = re.compile(r'\b(mot de pass|email|adress|code postal|cin)\b', re.I)# some sensitive words regex
    patern_list=[PHONE_NUMBER_pattern,SENSITIVE_Words_pattern,CREDIT_card,ID_NUMBER_pattern,EMAIL]# list contatining all the regex paterns
    status = True # True = no sensitive info / False = sensitive info detected
    for i in patern_list :# test all the regex paterns on the text file
        matches = i.finditer(text)
        for match in matches:
            if match is not None :
                status = False 
            else :
                status = status and True    
            #print([name for name in globals() if globals()[name] is i])# prints the REGEX Name
            print(match)# prints the REGEX
    return(status)# return False or True