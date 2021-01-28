Tasklist = [23 , "Jane", ["lesson 23",560,{"Currency":"KES"}],987,(76,"John")]
print(type(Tasklist))
print(Tasklist[2][2]["Currency"])
print(Tasklist[2][1])
print(len(Tasklist))
Tasklist[3] = 789
print(Tasklist)
Tasklist[4][1].lower()
print(Tasklist)

newlist = (20,30,[7, "tech"], "test")
newlist[2][1] = 'camp'
print(newlist)