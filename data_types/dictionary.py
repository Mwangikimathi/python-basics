""" Dictionaries are unordered collection of items.
    They are mutable/changeable.
    Instead of using indexes, we use keys to number them
    The keys contain the values 
    They are denoted using '{}'
    """ 

month = {
    1.000001 : "January",
    1 : "March",
    2 : "February",
    "name": "Nelson"
}
#print(month[2])
print(month[1.000001])
print(month[1])
print(1.0 == 1)
txt = (month.get("name", default = None))
print(txt)
#print(month["name"])