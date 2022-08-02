class Employee:
    company = "Google"
    def getSalary(self):
        print(f"Salary for this employee working in {self.company} is {self.salary}")

jash = Employee()
jash.salary = 100000
jash.getSalary()