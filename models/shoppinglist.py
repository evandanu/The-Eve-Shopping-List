class Shoppinglist(object):
	"""docstring for Shoppinglist"""
	def __init__( self, id, name, user_id):
		self.id = id
		self.name= name
		self.user_id = user_id
		self.items = {}
		

		