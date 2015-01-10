# solution_8.py
#     A program to convert Fahrenheit temps to Celsius


def main():
    fahrenheit = eval(input("What is the Fahrenheit temperature? "))
    celsius = 5/9 * (fahrenheit - 32)
    print("The temperature is", celsius, "degrees Celsius.")

main()
