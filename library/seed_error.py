class SeedError(Exception):
	def __init__(self, message='A custom error occurred'):
		super().__init__(message)