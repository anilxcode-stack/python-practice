# Match Case Statements -> like Switch Case statement in C++

# def check_number(x):
#     match x:
#         case 10: print("It's 10")
#         case 20: print("It's 20")
#         case _: print("It's neither 10 not 20")


# check_number(10)
# check_number(30)

# Another Example

# def greet(person):
#     match person:
#         case "A":
#             print("Hello, A!")
#         case "B":
#             print("Hello B!")
#         case _:
#             print("Hello Stranger!")

# greet("A")
# greet("B")


# Example

# def num_check(x):
#     match x:
#         case 10 | 20 | 30:
#             # Matchex 10 , 20 or 30
#             print((f"Match :{x}"))
#         case _:
#             print("No match found")

# num_check(10)
# num_check(20)
# num_check(30)


# Example 

def num_check(x):
    match x:
        case 10 if x % 2 == 0:
            #match 10 only if It's even\
            print("Matched 10 and it's even")
        case 10:
            print("Match 10, but it's is not even.")
        case _:
            print("No match fround")
num_check(10)
num_check(15)