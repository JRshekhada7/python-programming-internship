class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        if self.num2 == 0:
            return "Error! Division by zero."
        return self.num1 / self.num2

def main():
    print("Simple Calculator using Python")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    calc = Calculator(num1, num2)

    print("\nChoose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    choice = input("Enter choice (1/2/3/4): ")

    if choice == '1':
        print(f"Result: {calc.add()}")
    elif choice == '2':
        print(f"Result: {calc.subtract()}")
    elif choice == '3':
        print(f"Result: {calc.multiply()}")
    elif choice == '4':
        print(f"Result: {calc.divide()}")
    else:
        print("Invalid choice! Please enter a valid option.")

if __name__ == "__main__":
    main()
