"""
String indexing is retrieving a character from a string

"""

"""
Syntax [x] where x is the index

"""

institution = "techcamp"
x = institution[0:4] # String Slicing #
print(x)
y = institution[4:] # String Slicing #
print(y)
# print #
print(institution[2])# positive indexing #
print(institution[-6])# negative indexing #

p = "Tech"
q = "camp"
r = p + q
print (r)

ds = "data science kenya"
# print (ds[13])
# print (ds[-5])

# print (ds[7])
# print (ds[-11])

g = ds[::3] # step in python
print(g)

a = ds[0:4]
b = ds[5:12]
c = ds[13:]
print(a)
print(b)
print(c)

# Format Dynamically
ques = input("what's your name\n")
response = 'Hello, {}. Thank you for reaching us.'.format(ques)
#response = f"Hello,{ques}. Thank you for reaching us."
print(response)