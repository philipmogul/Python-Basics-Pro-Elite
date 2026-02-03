def main():
    print(f"Polymorphism allows methods to do different things based on the object calling them.")
    print(f"Here, we define a function that takes different shapes and calls their area method.")
    print(f"This is an example of polymorphism in Python.\n")
    print(f"BASICALLY, DIFFERENT CLASSES WITH SAME METHOD NAMES:")

    class Shape:
        def area(self):
            raise NotImplementedError("Subclasses must implement this method.")
    class Circle(Shape):
        def __init__(self, radius):
            self.radius = radius
        def area(self):
            return 3.14159 * (self.radius ** 2)
    class Rectangle(Shape):
        def __init__(self, width, height):
            self.width = width
            self.height = height
        def area(self):
            return self.width * self.height
    def print_area(shape):
        print(f"The area is: {shape.area()}")
    circle = Circle(5)
    rectangle = Rectangle(4, 6)
    print_area(circle)
    print_area(rectangle)

if __name__ == "__main__":
    main()