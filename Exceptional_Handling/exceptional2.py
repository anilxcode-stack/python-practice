# Catchiong Specific Exceptions

# try:
#     x = int("str")
#     inv = 1/x
# except ValueError:
#     print("Not Valid!")
# except ZeroDivisionError:
#     print("zero has no inverse!")


# Catching Multiple Exceptions Together
# a = ["10", "twenty", 30]

# try:
#     total = int(a[0] + int(a[1]))
# except (ValueError, TypeError) as e:
#     print("Error: ", e)
# except IndexError:
#     print("Index out of range.")



# Catch-All Exception (Not Recommended)
# try:
#     res = "100"/20
# except:
#     print("Something went wrong!")

