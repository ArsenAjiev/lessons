"""
Создать класс Dog. Класс имеет четыре атрибута: height, weight, name, age.
Класс имеет три метода: jump, run, bark. Каждый метод выводит сообщение на экран.
Создать объект класса Dog, вызвать все методы объекта и вывести на экран все его атрибуты.
"""
from library.dog import Dog
from library.cat import Cat

if __name__ == "__main__":
    dog = Dog(height=100, weight=100, name="Dog", age=4)
    dog.bark()

    cat = Cat(height=100, weight=100, name="Cat", age=5)
    cat.meow()