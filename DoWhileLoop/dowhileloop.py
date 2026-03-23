# Python does't have a built-in do while loop like C, C++ or Java
# But you can easily emulate it using a while True Loop with break


while True:
    num = int(input("Enter the value greater than 10: "))
    if num > 10:
        break