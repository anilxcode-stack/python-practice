# math_module.py

def add(a, b):
    return a+b

def multiply(a, b):
    return a*b

# This block runs only when this file is excuted directly

if __name__ == "__main__":
    print("math_module is running directly")
    print("Add: ", add(2, 3))
    print("Multiply: ", multiply(2, 3))