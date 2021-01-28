class Employee:
   
    
    name = "Mark"
    def __init__(self, age, name, department, salary):
        
        self.age = age
        self.name = name 
        self.department = department
        self.salary = salary


    def print_name(self):
        print(self.age)

    def get_details(self):
        print(self)
        # s = "{} is {} years old and works in {} department and earns Kshs. {}".format(self.name, self.age, self.department, self.salary)
        # return s
        return f"{self.name} is {self.age} years old and works in {self.department} department and earns Kshs{self.salary}."

m1 = Employee(45, "Mark", "IT", 59000)
m2 = Employee(50, "John", "Procurement", 20000)
print("John's salary is " ,m2.salary)
print(m2.get_details())
# print(m1.print_name())
# print (type(m1))

# print(Employee.name) 
# print(Employee.print_name())