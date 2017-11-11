import uuid

class Item(object):
	"""docstring for Item"""
	def __init__(self, name,shoppinglist_id, description, id=None):
		self.id = uuid.uuid4().hex if id is None else id
		self.name = name
		self.shoppinglist_id = shoppinglist_id
		self.description = description
		