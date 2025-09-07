#### OOPs in PYTHON ####

# class Student:
#     college_name = "Veltech college"
#     name = "Sai Vamsi"
#     rollno = "19343"

#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
#         print("Adding to the database")
    
# s1 = Student("Sai Vamsi","97")
# print(s1.name , s1.marks)

# s2 = Student("Arjun","67")
# print(s2.name , s2.marks)

# print(Student.college_name)
# print(s1.name)

# s2 = Student()
# print(s2.rollno)


#Methods#########

# class Student:
#     name = "Karan"

#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks

#     def welcome(self):
#         print("welcome student")

#     def getmarks(self):
#         return self.marks

# s1 = Student("Karan",97)
# s1.welcome()
# print(s1.getmarks())


#Q1(practice)####static method#####

# class Student:
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks

#     @staticmethod
#     def hello():
#         print("Hello")

#     def get_avg(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#         print("Hi",self.name,"Your avg score is: ",sum/3)

# s1 = Student("Karan,",[98,99,97])
# s1.get_avg()
# s1.hello()


#Abstraction example###########

# class Car:
#     def __init__(self):
#         self.acc = False
#         self.brk = False
#         self.clutch = False

#     def start(self):
#         self.clutch = True
#         self.acc = True
#     print("car started..")

# car1 = Car()
# car1.start()

#Practice#########

# class Account:
#     def __init__(self,bal,acc):
#         self.balance = bal
#         self.account_no = acc

#     def debit(self,amount):
#         self.balance -= amount
#         print("Rs.",amount ,"was debited")
#         print("Total balance = ",self.get_balance())

#     def credit(self,amount):
#         self.balance += amount
#         print("Rs.",amount,"was credited")
#         print("Total balance = ",self.get_balance())
#     def get_balance(self):
#         return self.balance

# acc1 = Account(10000,12300)
# acc1.debit(1000)
# acc1.credit(1230)

##########
# class Student:
#     def __init__(self,name):
#         self.name = name


# s1 = Student("Sai Vamsi")
# print(s1.name)
# del s1.name
# print(s1.name)

#########

# class Account:
#     def __init__(self,acc_no,acc_pass):
#         self.acc_no = acc_no
#         self.acc_pass = acc_pass

# class AMOUNT:
#         def __init__(self) -> None:
#              pass
        

class Employee:
    def __init__(self,fullname):
        self.name = fullname
        print("Adding employee to the database")

e1 = Employee("Sai Vamsi")
print(e1.name)