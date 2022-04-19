
class Employee:

    # initialisation method(this is a method of a class)
    # self here is a generic way of representing instances of a class (i.e emp_1 , emp_2)
    # We are assigning arguments passed to this method as values for the variables of the instances
    
    def __init__(self,firstname,lastname,pay):
        self.firstname = firstname
        self.lastname = lastname
        self.pay = pay

    def email(self):
        return self.firstname + self.lastname + "@email.com"

    def apply_raise(self):
        self.pay = int(self.pay * 1.04)


emp_1 = Employee("Adam","Driver",50000)
emp_2 = Employee("Joseph", "Ramos", 60000)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)
