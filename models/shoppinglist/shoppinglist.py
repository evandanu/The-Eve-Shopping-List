import uuid

class Shoppinglist(object):
	"""docstring for Shoppinglist"""
	def __init__(self, user_id, name,items, date, id=None):
		self.id = uuid.uuid4().hex if id is None else id
		self.user_id = user_id
		self.name= name
		self.items = {}
		self.date = date

		