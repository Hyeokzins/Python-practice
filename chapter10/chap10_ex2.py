class Person(object):
    def __inin__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender

    def about_me(self):
        print("My name is", self.name ,"and I am",self.age ,'years old.')
    
class Employee(Person):
    def __init__(self,name,age,gender,salary,hire_date):
        super().__init__(name,age,gender)
        self.salary=salary
        self.hire_date=hire_date


    def do_work(self):
        print("I am working on")

    def about_me(self):
        super().about_me()
        print("My salary is", self.salary,'and my hire date is', self.hire_date)


