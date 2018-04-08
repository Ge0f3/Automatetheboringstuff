class contact_ditct(object):
	"""docstring for contact_ditct"""
	def __init__(self):
		self.contacts={'amit':"(806)-317-6670", "abhishek":"(806)-730-8229","addy":"(806)-283-0449", "kavya":"(806)-451-7576","agnes":"(512) 783-8999"}
		print("This is a dict to store Contact Details")
	def printdict(self):
		for key,values in self.contacts.items():
			print("{}'s Phone number is {}".format(key,values))
	def search(self):
		while True:
			name = str(input("Enter a name to search: ")).lower()
			if name == '':
				break
			if name in self.contacts:
				print("{}'s phone number is {}".format(name,self.contacts[name]))
			else:
				print("The name is not found in the database !!")
				contact_no = str(input("Enter respective phone number"))
				self.contacts[name]=contact_no
				print("Phone number updated")



contact = contact_ditct()
contact.search()
contact.printdict()
		