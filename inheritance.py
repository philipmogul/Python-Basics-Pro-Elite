
class Parent:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, my name is {self.name}."
    
    def inherited(self):
        return "This method is inherited from the Parent class."
    
class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name) # super() calls the Parent's __init__ 
        #super() allows access to methods of a superclass from the subclass
        self.age = age

    def introduce(self):
        # To inherit a method from the Parent class, user super().method_name()
        inherited_message = super().inherited()
        return f"{self.greet()} I am {self.age} years old.\n{inherited_message}"

def main():
    print("Testing inheritance in Python.")
    # Create an instance of Child
    child_instance = Child("Philip Mumo", 33)
    print(child_instance.introduce())
        

if __name__ == "__main__":main()
