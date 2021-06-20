'''
Реализовать проект расчета суммарного расхода ткани на 
производство одежды. Основная сущность (класс) этого 
проекта — одежда, которая может иметь определенное название. 
К типам одежды в этом проекте относятся пальто и костюм. 
У этих типов одежды существуют параметры: размер (для пальто) 
и рост (для костюма). Это могут быть обычные числа: V и H, 
соответственно. 
Для определения расхода ткани по каждому типу одежды использовать 
формулы: для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3). 
Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на 
практике полученные на этом уроке знания: реализовать абстрактные 
классы для основных классов проекта, проверить на практике 
работу декоратора @property.
'''

class Textil:
    def __init__(self, V, H):
        self.V = V
        self.H = H
    
    def get_s_V(self):
        return self.V / 6.5 + 0.5

    def get_s_H(self):
        return self.H * 2 + 0.3

    @property
    def get_s_all(self):
        return str(f'S общ. ткани = {(self.V / 6.5 + 0.5) + (self.H * 2 + 0.3)}')

class Coat(Textil):
    def __init__(self, V, H):
        super().__init__(V, H)
        self.s_of_coat = round(self.V / 6.5 + 0.5)

    def __str__(self):
        return f'S на пальто: {self.s_of_coat}'

class Jacket(Textil):
    def __init__(self, V, H):
        super().__init__(V, H)
        self.s_of_jacket = round(self.H * 2 + 0.3)

    def __str__(self):
        return f'S на костюм: {self.s_of_jacket}'

coat = Coat(1, 2)
jacket = Jacket(3, 4)

print(coat)
print(jacket)

print(coat.get_s_all)
print(jacket.get_s_all)

print(jacket.get_s_V())
print(jacket.get_s_H())