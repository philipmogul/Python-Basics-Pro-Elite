
class Parent:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, my name is {self.name}."
    
class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name) # super() calls the Parent's __init__ 
        #super() allows access to methods of a superclass from the subclass
        self.age = age

    def introduce(self):
        return f"{self.greet()} I am {self.age} years old."

def main():
    print("Testing inheritance in Python.")
    # Create an instance of Child
    child_instance = Child("Philip Mumo", 33)
    print(child_instance.introduce())
        

if __name__ == "__main__":main()
