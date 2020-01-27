# --------------
#  Read the data of the format .yaml type
import json

# using with open command to read the file
with open (path) as f :
    data = json.load(f)
f.close()

Nobel_India = []
category = {}
chem = {}
org = {}
noble_1994 ={}

#print (data)
print (len(data))


#  Women who got the first Nobel Prize?

for i in data :
    if (i['Sex'] == 'Female') :
        First_Female = i['Full Name']
        break

print (First_Female)
    
#  How many have come from india?

for d in data :
    if d['Birth Country'] == 'India' :
        Nobel_India.append(d['Full Name'])
        if d['Category'] in category :
             category[d['Category']] += 1
        else :
                category[d['Category']] = 1

    if d['Category'] == 'Chemistry' :
        if d['Birth Country'] in chem :
             chem[d['Birth Country']] += 1
        else :
                chem[d['Birth Country']] = 1
    if ((d['Category'] == 'Chemistry') or (d['Category'] == 'Physics')) :
        if d['Organization Name'] in org :
             org[d['Organization Name']] += 1
        else :
                org[d['Organization Name']] = 1

    if d['Full Name'] == 'Marie Curie, née Sklodowska' :
            motivation = d['Motivation']
    if d['Year'] == 1994 :
            noble_1994[d['Full Name']] = d['Category']


print (len(Nobel_India))


#  Calculate category wise number of prizes for the people who came from India?
print (category)
#   Which country has produced the highest number of Nobel winners for category `Chemistry`?
from collections import Counter
import operator

chem_country = max(chem, key = chem.get)
print (chem_country, chem[chem_country])

#  Which Organization won the most nobel prizes in the category "Physics" and "Chemistry" ?
print (max(org, key = org.get))
#  What was the Motivation for awarding the Nobel Prize for Marie Curie, nÃ©e Sklodowska?
print (motivation)
#  In which category people got Noble Prize in the year 1994?
print (noble_1994)


