class Aura:
    def __init__(self, name = "Philip Value"):
        print("WELCOME TO AURA!")
        self.name = name
        print("{}".format(self.name), ", You really got AURA!")

# Below I create an object for my Aura class, which in return calls the constructor 


def main():
    print("WORKING WITH OBJECTS IN PYTHON")
    auraobj = Aura("Philo!")

if __name__ == "__main__": main()