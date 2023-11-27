class Rectangle:
    count = 0
    
    def __init__(self, length, width):
        self.length = length
        self.width = width
        Rectangle.count += 1

    def get_length(self):
        return self.length

    def set_length(self, value):
        self.length = value

    def get_width(self):
        return self.width

    def set_width(self, value):
        self.width = value

    def is_equal(self, rect):
        if self.width == rect.width and self.length == rect.length:
            return True
        else:
            return False

    def perimeter(self):
        return 2 * (self.length + self.width)

    def area(self):
        return self.length * self.width

    def to_string(self):
        return f"""Rectangle:
Length: {self.length}
Width: {self.width}"""


class Parallelogram(Rectangle):
    para_count = 0

    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height
        Parallelogram.para_count += 1

    def get_height(self):
        return self.height

    def set_height(self, value):
        self.height = value

    def area(self):
        return (self.length * self.width) * 2 + (self.length * self.height) * 2 + (self.width * self.height) * 2

    def volume(self):
        return self.width * self.length * self.height

    def to_string(self):
        return f"""Parallelepiped:
Length: {self.length}
Width: {self.width}
Height: {self.height}"""


rect1 = Rectangle(10, 10)
rect2 = Rectangle(10, 10)

para1 = Parallelogram(1, 2, 3)
para2 = Parallelogram(3, 3, 3)

print("------------------------------------------------------------------------------------------------------------")
print("------------------------------------------------------------------------------------------------------------")
print(rect1.to_string())
print("Perimeter:", rect1.perimeter())
print("Area:", rect1.area())
print("Are the two rectangles equal?:", rect1.is_equal(rect2))

print("------------------------------------------------------------------------------------------------------------")
print("------------------------------------------------------------------------------------------------------------")

print(para1.to_string())
print("Volume:", para1.volume())
print("Area:", para1.area())
print("Are the two parallelograms equal?:", para1.is_equal(para2))
print("------------------------------------------------------------------------------------------------------------")
print("------------------------------------------------------------------------------------------------------------ \n")

print("Number of instances created:", Rectangle.count ,"\n")

print("------------------------------------------------------------------------------------------------------------")
print("------------------------------------------------------------------------------------------------------------")
