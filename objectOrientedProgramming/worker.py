from paye_tax import Employee

m1 = Employee(78000, 12000, 1500, 5000)
print("Your Taxable income is :", m1.get_taxable_income())
print("Your Income tax is :", m1.get_individual_tax())
print("Your Paye is :", m1.get_paye())
print("Your NHIF is :", m1.get_nhif())
print("Your Deductions are :", m1.get_deductions())
print("Your Net Pay is :", m1.get_net_salary())
