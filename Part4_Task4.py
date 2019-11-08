# 4)ContactList
# Создайте класс ContactList, который должен наследоваться от
# встроенного класса list. В нем должен быть реализован метод
# search_by_name, который должен принимать имя, и возвращать список
# всех совпадений. Замените all_contacts = [ ] на all_contacts =
# ContactList(). Создайте несколько контактов, используйте метод
# search_by_name.
# class List():
#     def __init__(self,name):
#       self.name = name  
   
# class ContactList (List):
#     def search_by_name (self):
#         all_contacts = [ ]
        
      
# all_contacts = ContactList(list(input().split()))
# print(all_contacts)
# all_contacts.search_by_name(name)

class ContactList(list):
    def __init__(self, contact_, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.contact_ = contact_
    
    def search_by_name(self, name):
        item = []
        for i in self.contact_:
            if i == name:
                item.append(i)
        print(item)

all_contacts = ContactList(['Mayram','Bakyt', 'Elnazar', 'Baityk'])
all_contacts.search_by_name('Mayram')