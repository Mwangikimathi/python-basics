""" Lists are Ordered Collection of items.They are Mutable/Changeable.
    They are denoted by '[]'
    They can store any type of element.
    """


# list = ['Physics','chemistry',3000,40]
# print(list)
# del list[2] #deleting lists
# list[2] = 201 #updating lists
#print(list[0]) #Accessing values in lists
#print (list)
# list.count()

list1 = ["Physics,Chemistry,Biology,Mathematics"]# String list
list2 = [26,56,78,98,45,34]# Integer list
list3 = [34.5,65.4,56.7,34.5,23.4,12.3]# Float list
list4 = [True,False,True,False]# Boolean list
list5 = ["Mon","Tue","Wed","Tue","Mon"]# Days string list
list6 = [100,"Ben",[True,10.5,"Ken"],False]# String,float,boolean,integer list
list6.append("Mathematics") # appending an object in a list
print(list6[1])# printing object "Ben" from list6(Indexing)
print(list6[2][2])# printing element "Ken" from list6(Indexing)
print (list6[1:3])# List slicing
print (list6)
elem = 'Mon'
print("Given element\n",elem)
cnt = list5.count("Mon")
print("number of times the element is present in the list:\n",cnt)


