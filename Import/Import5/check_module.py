# check_module.py

def is_even(n):
    return n%2 == 0

def is_odd(n):
    return n%2 != 0
num = 9
if __name__ == "__main__":
    print("Running check_module directly")
    print("Is Even:", is_even(num))
    print("Is Odd: ", is_odd(num))