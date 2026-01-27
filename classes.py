class Fibonacci:
    def __init__(self, n):
        self.n = n

    def generate(self):
        sequence = []
        a, b = 0, 1
        for _ in range(self.n):
            sequence.append(a)
            a, b = b, a + b
        return sequence
    
print("FIBONACCI SEQUENCE EXAMPLE:")
fib = Fibonacci(10)
print(fib.generate())