class Complex:
    def __init__(self, r, i):
        self.real = r
        self.img = i
    def __add__(self, sec): #overloading the add
        r = self.real + sec.real
        i = self.img + sec.img
        return Complex(r, i)
    def __str__(self):
        return str(self.real) + '+' +str(self.img) + 'i'
c1 = Complex(5, 3)
c2 = Complex(2, 4)
print("sum = ", c1+c2)