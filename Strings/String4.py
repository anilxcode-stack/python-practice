# len -> returns length of string

# s = "GeeksforGeeks"
# print(len(s))


#Upper() and lower()

# s = "Hello world"
# print(s.upper())
# print(s.lower())


# Concatenation & Repetation

# s1 = "Hello"
# s2 = "World"
# print(s1+ " "+s2)

# title() -> used to capitalized first characters and

# a = "hello geek"
# b = a.title()
# print(b)

#swapecase -> used to convert all uppercase into lowercase and all lowercase intpo upopercase

# s = " I love python"
# print(s.swapcase())

# capitilize() -> capitilize first character

# s = "hello WORLD"
# res = s.capitalize()
# print(res)


# center()  -> align center

# s1 = "hello"
# s2 = s1.center(20)
# print(s2)


# More Examples

# h1 = "Name"
# h2 = "Age"
# h3 = "Location"

# s1 = h1.center(20, '-')
# s2 = h2.center(20, '-')
# s3 = h3.center(20, '-')

# print(s1)
# print(s2)
# print(s3)


# find() -> returns the index of the string if not found then return -1

# s = "welcome to GeeksForGeeks!"
# index = s.find("GeeksForGeeks")
# print(index)

# At Specific portion of string

# s = "abc abc abc"
# index = s.find("abc", 4)
# print(index)


# s = "Python is fun"
# index = s.find("python")
# print(index)


# isnumeric() -> It returns true if all the characters in the string is numberic or not

# string = '123ayu4R'
# print(string.isnumeric())
# string = '123456'
# print(string.isnumeric())


# join()

# t = ("Learns", "Python", "Fast")
# res = "-".join(t)
# print(res)

#count() -> counts the number of specific character in string

# print("banana".count("a"))


# split() -> split like a list
s = "a b c"
print(s.split())