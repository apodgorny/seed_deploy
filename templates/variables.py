class Variables:
	def __init__(self):
		...

	def get(self, name, default=None):
		match name:
			case 'var1':
				return 'variable1_value'
			case 'var2':
				return 'variable2_value'
			case _:
				return default