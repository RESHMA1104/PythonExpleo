class Circle:
    def __init__(self, radius=1.0, color='red'):
        self._radius = radius
        self._color = color

    # Class method - alternative constructor (only radius)
    @classmethod
    def withRadius(cls, radius):
        return cls(radius)

    # Class method - alternative constructor (radius + color)
    @classmethod
    def withRadiusAndColor(cls, radius, color):
        return cls(radius, color)

    # Instance methods
    def getRadius(self):
        return self._radius

    def getColor(self):
        return self._color

    def setRadius(self, radius):
        self._radius = radius

    def setColor(self, color):
        self._color = color

    def getArea(self):
        return 3.14159 * self._radius * self._radius

    def __str__(self):
        return f"Circle[radius={self._radius}, color={self._color}]"


# Creating objects
circle1 = Circle()
print(circle1)

circle2 = Circle.withRadius(2.5)   # using class method
print(circle2)

circle3 = Circle.withRadiusAndColor(3.5, "blue")  # using class method
print(circle3)