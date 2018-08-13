class Book:
	"""docstring for ClassName"""
	def __init__(self,bname,bid,aurthor,edition):
		self.bname = bname
		self.bid=bid
		self.aurthor=aurthor
		self.edition=edition
	def getBookname(self):
		return self.bname
	def getBookid(self):
		return self.bid
	def getBookaurthor(self):
		return self.aurthor
	def getBookedition(self):
		return self.edition
count=int(input("number of book required"))
BookList=[]
while count!=0:
	Bookname=input("enter book name:")
	Bookid=int(input("enter book id:"))
	Bookaurthor=input("enter book aurthor:")
	Bookedition=input("enter book edition")
	bookstore=Book(bname,ids,aurthor,edition)
	BookList.append(bookstore)
count=count-1
BookMap=map(lambda bookstore:bookstore.getBookname()+""+bookstore.getBookid()+""+bookstore.getBookaurthor+""+bookstore.Bookedition,BookList)
print(list(BookMap))

	
		