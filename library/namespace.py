import os

from library.files import Files


class Namespace:
	def __init__(self, name):
		self.name     = name
		self.base_dir = os.path.join('ROOT_DIR', 'namespaces', self.name)

	def create(self):
		# Create namespace directory
		Files.mkdir(self.base_dir)
		
		# Create empty constants.json and variables.py
		constants_path = os.path.join(self.base_dir, 'constants.json')
		variables_path = os.path.join(self.base_dir, 'variables.py')

		# Create empty constants.json file
		with open(constants_path, 'w') as f:
			f.write('{}')

		# Create empty variables.py file
		with open(variables_path, 'w') as f:
			f.write('# variables.py')

		print(f'Created Namespace "{self.name}" with empty constants.json and variables.py')
