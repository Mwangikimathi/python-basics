class Employee:

    basicSalary = 0
    allowances = 0
    pension = 0
    tax = 0
    personal_relief = 2400
    nhif = 0
    individual_tax = 0
    net_salary = 0
    deductions = 0
    paye = 0
    taxable_income = 0
    nssf = 0
    
 
    def __init__(self, basicSalary, allowances, nssf, pension):
        self.basicSalary = basicSalary
        self.allowances = allowances
        self.nssf = nssf
        self.pension = pension
        self.get_deductions()
        self.get_individual_tax()
        self.get_taxable_income()
        self.get_nhif()
        self.get_net_salary()
        self.get_paye()

    def get_taxable_income(self):
        taxable_income = (self.basicSalary + self.allowances)
        self.taxable_income = taxable_income
        return taxable_income

    def get_deductions(self):
        deductions = (self.nssf + self.pension)
        self.deductions = deductions
        return deductions

    def get_details(self):
        return f"My Basic salary is {self.basicSalary} and my total allowances are {self.allowances}.My NSSF is {self.nssf} and pension is {self.pension}"
    
    def get_individual_tax(self):
        
        self.p1 = (24000 * 0.10) + ((self.taxable_income - 24000) * 0.25)
       

        self.p2 = 24000 * 0.1 + 8333 * 0.25 + (self.taxable_income - 24000 - 8333) * 0.30
        

        if self.taxable_income >= 24000 and self.taxable_income <= 32333:
             tax = (self.p1)
             self.tax = tax
             return tax
        elif self.taxable_income >= 32333:
             tax = (self.p2)
             self.tax = tax
             return tax
        elif self.taxable_income <= 23999:
             tax = 0
             self.tax = tax
             return tax
    

    def get_nhif(self):
        
        if self.taxable_income in range (0, 5999):
            nhif = 150
            return nhif
        elif self.taxable_income in range (6000, 7999):
            nhif = 300
            return nhif
        elif self.taxable_income in range (8000, 11999):
            nhif = 400
            return nhif
        elif self.taxable_income in range (12000, 14999):
            nhif = 500
            return nhif
        elif self.taxable_income in range (15000, 19999):
            nhif = 600
            return nhif
        elif self.taxable_income in range (20000, 24999):
            nhif = 750
            return nhif
        elif self.taxable_income in range (25000, 29999):
            nhif = 850
            return nhif
        elif self.taxable_income in range (30000, 34999):
            nhif = 900
            return nhif
        elif self.taxable_income in range (35000, 39999):
            nhif = 950
            return nhif
        elif self.taxable_income in range (40000, 44999):
            nhif = 1000
            return nhif
        elif self.taxable_income in range (45000, 49999):
            nhif = 1100
            return nhif
        elif self.taxable_income in range (50000, 59999):
            nhif = 1200
            return nhif
        elif self.taxable_income in range (60000, 69999):
            nhif = 1300
            return nhif
        elif self.taxable_income in range (70000, 79999):
            nhif = 1400
            return nhif
        elif self.taxable_income in range (80000, 89999):
            nhif = 1500
            return nhif
        elif self.taxable_income in range (90000, 99999):
            nhif = 1600
            return nhif
        elif self.taxable_income >= 100000:
            nhif = 1700
            return nhif
        else:
            nhif = 0
            return nhif

    def get_net_salary(self):

        net_salary = ((self.taxable_income) - (self.deductions + self.tax + self.paye + self.nhif))
        self.net_salary = net_salary 
        return net_salary

    def get_paye(self):

        paye = self.tax - self.personal_relief
        self.paye = paye 
        return paye

emp1 = Employee(78000,12000,1000,7000)
print(emp1.get_details())
print(emp1.get_deductions())
print(emp1.get_individual_tax())
print(emp1.get_net_salary())
print(emp1.get_paye())
print(emp1.get_nhif())
