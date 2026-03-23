# Using For with Else

# for i in range(5):
#     print(i)
# else:
#     print("Loop finished successfully")


# for i in range(5):
#     if i == 3:
#         break
#     print(i)
# else:
#     print("Loopfinished successfully")


numbers = [1, 3, 5, 7, 9]

for num in numbers:
    if num == 4:
        print("Found")
        break
else:
    print("No found")