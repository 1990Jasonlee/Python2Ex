def greet(name):
    print(f"Hello {name}")

def name_input():
    input_name = input("Enter a name:")
    greet(input_name)

name_input()