'''
Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», 
реализуйте перегрузку методов сложения и умножения комплексных чисел. 
Проверьте работу проекта, создав экземпляры класса (комплексные числа) и 
выполнив сложение и умножение созданных экземпляров. 
Проверьте корректность полученного результата.
'''
class ComplexNum:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
        self.c = 'a + b * d'

    def __add__(self, other):
        print(f'Сумма c1 и c2 равна')
        return f'c = {self.a + other.a} + {self.b + other.b} * d'

    def __mul__(self, other):
        print(f'Произведение c1 и c2 равно')
        return f'c = {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * d'

    def __str__(self):
        return f'c = {self.a} + {self.b} * d'


c_1 = ComplexNum(1, -2)
c_2 = ComplexNum(3, 4)
print(c_1)
print(c_1 + c_2)
print(c_1 * c_2)