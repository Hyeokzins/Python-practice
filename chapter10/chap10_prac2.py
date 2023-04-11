class Person (object):
    def __init__(self,name):
        self.name = name

    def language(self):
        pass

class Earthling(Person):
    def language(self,language):
        return language
    

class Groot(Person):
    def language(self,language):
        return 'I am Groot'
    
name=['Gachon','Dr.Strange','Groot']

country=['KOR','USA','Galaxy']
language=['koran','english','groot']

for idx,name in enumerate(name):
    if country[idx].upper() != 'Galaxy':
        person=Earthling(name)

    print(person.language(language[idx]))


else:
    groot=Groot(name)
    print(groot.language(language[idx]))
