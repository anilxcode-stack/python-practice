# Practice Questions Solution (By Shraddha Khapra)

"""
Let‘s Practice

Create a new file “practice.txt” using python. Add the following data in it:
Hi everyone
we are learning File I/O

using Java.

I like progranmming in Java.

WAF that replace all occurrences of “java” with “python” in above file.

Search if the word “learning” exists in the file or not.

"""

# with open("File_Handling/PracticeQu1/practice.txt", "a") as file:
#     file.write("Hi everyone")
#     file.write("\nwe are learning File I/O\nusing Java.")
#     file.write("\nI like programming in Java")

# with open("File_Handling/PracticeQu1/practice.txt", "r") as f:
#     data = f.read()
#     Python = data.replace("Java", "Python")
#     print(Python)


# word = "learning"
# with open("File_Handling/PracticeQu1/practice.txt", "r") as f:
#     data = f.read()

#     if(word in data):
#         print("Found")
#     else:
#         print("Not Found!")

    
"""
1) WAF to find in which line of the file does the word “learning” occur first.
Print -1 if word not found.

2) From a file containing numbers separated by comma, print the count of even numbers.

"""

# First
# def printLineIdx():
#     count = 0
#     word = "learning"

#     with open("File_Handling/PracticeQu1/practice.txt", "r") as f:
#         while True:
#             data = f.readline()

#             if not data:   # end of file
#                 return -1

#             if word in data:
#                 return count + 1

#             count += 1

# print(printLineIdx())


# Second
with open("File_Handling/PracticeQu1/numbers.txt", "r") as f:
    count = 0
    data = f.read()
    numbers = data.split(",")
    print(numbers)
    for i in numbers:
        if int(i) % 2 == 0:
            count += 1
    print(count)