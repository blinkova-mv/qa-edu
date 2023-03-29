# 5.1. Создайте любой класс с произвольным количеством подклассов, экземпляров, атрибутов и методов
#     - как минимум один атрибут должен быть с уровнем доступа private. Соответственно, для получания значений этого атрибута
#     нужно использовать методы get и set
# 5.2. Cоздайте репозиторий на gi и отправте файл с домашним заданием в этот удаленный репозиторий
class Cat:
    bio_class = 'Animal'
    def __init__(self, name, weight,):
        self._name = name
        self.weight = weight
        # self.col = col

    def eat(self):
        return 'I like tasty food'
    def get_name (self):
        return f'Hi! My name is {self._name}'
cat_1 = Cat('Vasja', 5)
cat_2 = Cat('Masha', 4)
# # print(cat_1.name)
# # print(cat_2.eat())
# print(cat_2.get_name())
# print(cat_1.get_name())


class AgeCat(Cat):
    def __init__(self, name, weight, col, age):
        super().__init__(name, weight)
        self.age = age,
        self.col = col
    def eat(self):
        return 'I like all food'
    def get_name (self):
        return f'Hi! My name is {self._name}'
    def set_name(self, new_name):
        self._name = new_name
cat_3 = AgeCat('Yoko', 6, 'white', 10)
print(cat_3.set_name('Dred'))
print (cat_3.get_name())
print(cat_3.age)
print(cat_3.eat())

