# Dictionaries in Python 

# info = {"name":"karan", "age":19, "eligible":True}
# print(info["name"])
# print(info.get("eligible"))


# Accessing multiple values

# info = {"name":"karan", "age":19, "eligible":True}
# print(info.values())

# Accessing keys

# info = {"name":"Karan", "age":19, "eligible":True}
# print(info)
# info.update({"age":20})
# info.update({"DOB":2001})
# print(info)



# Removing items from dictonary

# clear()
# info = {"name":"karan", "age":19, "eligible":True}
# info.clear()
# print(info)

# pop("")

# info = {"name":"Karan", "age":19, "eligible":True}
# info.pop("eligible")
# print(info)


# popitem():
# info = {"name":"Karan", "age":19, "eligible":True, "DOB":2003}
# info.popitem()
# print(info)


# delete the dictionary ( del keyword )
info = {"name":"Karan", "age":19, "eligible":True, "DOB":2003}
del info
print(info)