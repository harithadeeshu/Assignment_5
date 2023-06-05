#3: Implement the Complete Student Class
class Student:
    def setName(self):
        self.name = "Deeshu"
        print(self.name)

    def getName(self):
        return self.name
    
    def setRollNumber(self):
        self.rollNumber = 29
        print(self.rollNumber)

    def getRollNumber(self):
        return self.rollNumber
    
obj = Student()
obj.name = "Haritha"
obj.rollNumber = 24
obj.getName()
obj.setName()
obj.getRollNumber()
obj.setRollNumber()