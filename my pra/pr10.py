#class Person:
#    def _init_(self, name, age):
#        self.name = name
#        self.age =age
#        print("Создание объекта Person")
#
#
#tom = Person("Tom", 22)
#
#print(tom.name)
#print(tom.age)
#
#tom.age = 37
#print(tom.age)

class Phone:
    def __init__(self, model, number):
        self.model = model
        self.number = number
    def display_info(self):
        print(f"Модель: {self.model}, Номер: {self.number}")
    def call(self):
        print(f"Звонок на номер: {self.number}")
cell = Phone("Samsung", 123)
cell._display_info()
cell.call()