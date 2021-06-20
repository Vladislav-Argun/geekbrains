class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)
    def __str__(self):
        return f'Result: \n{"*" * self.quantity}' # если умножить строку на цифру, то эта строка продублируется.
    def __add__(self, other):
        return Cell(self.quantity + other.quantity)
    def __sub__(self, other):
        if (self.quantity - other.quantity) > 0:
            return self.quantity - other.quantity
        elif (self.quantity - other.quantity) == 0:
            print('Ошибка. Результат равен 0.')
        else:
            print('Ошибка. Результат отрицательный.')
    def __mul__(self, other):
        return Cell(int(self.quantity * other.quantity))
    def __truediv__(self, other):
        return Cell(round(self.quantity / other.quantity))
    def make_order(self, row_cells):
        row = ''
        for i in range(int(self.quantity / row_cells)):
            row += f'{"*" * row_cells} \\n'
        row += f'{"*" * (self.quantity % row_cells)}'
        return row

cells1 = Cell(32)
cells2 = Cell(98)

print(cells1)
print(cells1 + cells2)
print(cells2 - cells1)

print(cells2.make_order(10))
print(cells1.make_order(5))