import re

pattern_check = "^[a-zA-Z0-9]+[\._]?[a-zA-Z0-9]+[@]\w+[\.]\w+$"
id = input("Email ID: ")
match = re.search(pattern_check,id)
# print (match)
if match != None:
    print (f"{id} is valid mail")
    host = re.findall(".@(\w+[\.]\w+)",id)
    #print (host)
    #converting list to string using ''.join(..)
    print (f"Host: {''.join(host)}")
else:
    print(f"{id} is not a valid mail")
