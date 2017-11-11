import uuid

class User(object):
	"""docstring for User"""
	def __init__(self, fullname, username, email, phonenumber, address, id=None):
		self.id = uuid.uuid4().hex if id is None else id
		self.fullname = fullname
		self.username = username
		self.email = email
		self.phonenumber = phonenumber
		self.address = address
		