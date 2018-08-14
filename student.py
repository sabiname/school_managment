class Student:
# 	def  __int__(find,name,address):
# 		self.name = name
# 		self.address = address
# 		appendThis()
# 	def getStudentname(stdname):
# 		return stdname.Studentname

# 	def appendThis(self):
# 		studentList.append(self)
# 		pass
class student:
	"""docstring for student"""
	def __init__(self,name,address):
		self.name=name
		self.address=address
	def getStudentname(self):
		return self.Studentname
	def getAddress(place):
		return place.address
count=int(input("enter number of students:"))
studentList=[]
while count!=0:
	name=input("enter Studentname:")
	address=input("enter address")
	student=student(name,address)
	studentList.append(Student)
	count=count-1
StudentMap=map(lambda stud:stud.getStudentname()+""+stud.getAddress(),studentList)
print(list(StudentMap))

						
