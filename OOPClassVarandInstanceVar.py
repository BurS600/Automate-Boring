
class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    # initialisation method(this is a method of a class)
    # self here is a generic way of representing instances of a class (i.e emp_1 , emp_2)
    # We are assigning arguments passed to this method as values for the variables of the instances
    
    def __init__(self,firstname,lastname,pay):
        self.firstname = firstname
        self.lastname = lastname
        self.pay = pay

        Employee.num_of_emps += 1

    def email(self):
        return self.firstname + self.lastname + "@email.com"

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)
        # can also use self.raise_amount to access it as an instance variable
        # Employee.raise_amount says to use class variable "raise_amount"


print("num of employees: " + str(Employee.num_of_emps))

emp_1 = Employee("Adam","Driver",50000)
emp_2 = Employee("Joseph", "Ramos", 60000)

#print(emp_1.pay)
#emp_1.apply_raise()
#print(emp_1.pay)

print(emp_1.__dict__)
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)


emp_1.raise_amount = 1.05


print(emp_1.__dict__)
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

Employee.raise_amount = 1.06

print(emp_1.__dict__)
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)


print("num of employees: " + str(Employee.num_of_emps))
# one print before instances were intiialized and after to show how many employee instances were intialized ; stored in num_of_emps


## key concept to note: 1) first the variable will be searched within instance's dict to see if it's initialised in there
## 2) if var not initialised in instance dict, then it will look for the var in employee dict and return that
## 3) all instances that do not have var initialized will "INHERIT" the class variable of same name
## 4) If an instance has var initialized, it won't return class var, and so if you change class var value,
## it won't automatically get inherited and change the value of the instance variable as instance var already has its own
## value initialized
## 5) Therefore, need to be careful if you specify self.raise_amount or Employee.raise_amount in any class methods
