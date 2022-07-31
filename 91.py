class Employee:
    company = "Google"
    salary = 100

Jash = Employee()
rajni = Employee()
Jash.salary = 300
rajni.salary = 400

print(Jash.company)
print(rajni.company)
Employee.company = "YouTube"
print(Jash.company)
print(rajni.company)
print(Jash.salary)
print(rajni.salary)