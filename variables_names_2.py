1.
diamonds - sumOfSquirellDiamonds (sum_of_squirell_diamonds)
//более понятно что хранится в переменной

width - widthOfTheBiggestCar (width_of_the_biggest_car)
//изначально длина самой большой машины
//хранилась в width
//поменял название исходя из рекомендаций из первого занятия
//так же добавил абстракцию - Car

sumCost - volumeOfTheInkRate (volume_of_the_ink_rate)
//в переменной хранилось значение для общего 
//расхода чернил
//перешел на уровень абстракции
//непосредсвенно указал, что это объем расхода чернил

map1 - tankAttackStartCoords (tank_attack_start_coords)
//переменная для хранения координат
//начала атаки
//перешел на уровень абстракции и указал
//что это начальные координаты танковой атаки

yearsCounter - treeOfLifeTotalYears (tree_of_life_total_years)
//переменная для общего значения лет дерева жизни
//перешел на уровень абстрации задачи
//прямо указал что это общее количество лет для
//дерева жизни

2.

3.
class Vehicle(object):
 
    def __init__(self, color, doors, tires):
        self.color = color
        self.doors = doors
        self.tires = tires
//класс для описания автомобиля
//исходя из контекста имена переменных
//понятны и логичны

class Rectangle:
  
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
//класс для описания прямоугольника
//исходя из контекста имена переменных более понятны

class Person:
    
    def __init__(self, firstName, lastName, residenceAddress)
        self.firstName = firstName
        self.lastName = lastName
        self.residenceAddress = residenceAddress
        
//класс для описания пользователя
//исходя из контекста имена переменных более понятны

4.
width - widthOfTheBiggestCar
//переменная была из 5 символов
//сейчас ровно 20 (предельная граница)

tankAttackStartCoords - tankAttackStartDots
//переменная была длинной 21 символ
//заменил Coords на Dots

data - ufoDecriptedData
//переменная была длинной 4 символа
//добавил абстракции, сделал более понятным
//что в ней хранится по итогу 16 знаков

height - startMapHeight
//переменная была длинной 4 символа
//теперь 14 символо, более понятно что в ней хранится

doors - opendDoorsByKeyMaker
//переменная была длинной 5 символов
//добавил абстрации, стало более понятно
//что вней хранится и длинна 20 символов
