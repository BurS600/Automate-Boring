


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


emp_1 = Employee("Adam","Driver",50000)
emp_2 = Employee("Joseph", "Ramos", 60000)

print(emp_1.firstname + emp_1.lastname + "\n" + emp_1.email())

# remember class var and instance var are different

print(Employee.email(emp_2))
