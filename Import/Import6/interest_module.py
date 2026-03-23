def simple_interest(p, r, t):
    return (p * r * t)/100

if __name__ == "__main__":
    print("Running interest_module directly")
    si = simple_interest(1000, 5, 2)
    print("Simple Interest: ", si)